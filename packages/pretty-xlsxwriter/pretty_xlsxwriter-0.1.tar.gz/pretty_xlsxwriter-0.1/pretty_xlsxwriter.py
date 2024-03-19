from operator import ior
from functools import reduce

from xlsxwriter.worksheet import Worksheet
from xlsxwriter.workbook import Workbook
from xlsxwriter.format import Format


def union_dicts_list(l):
    return reduce(ior, l)


class CellFormat:
    def __init__(self, **kwargs):
        self._data = kwargs

    def __add__(self, other):
        return CellFormat(**union_dicts_list([self._data, other._data]))


def calculate_style(self, style):
    if isinstance(style, list):
        dict_style = union_dicts_list(style)
    elif isinstance(style, dict):
        dict_style = style
    elif isinstance(style, CellFormat):
        dict_style = style._data
    elif isinstance(style, Format):
        return style
    elif not style:
        dict_style = {}
    else:
        raise ValueError(f"Can't calculate style from {type(style)}")

    result = self.add_format(dict_style)
    return result


Workbook.calculate_style = calculate_style


class Section:
    def __init__(self, data=None):
        self.x = None
        self.y = None
        self.last_x = None
        self.last_y = None

        self.data = data or []
        self.merge = list()

    def add_merge(self, x1, y1, x2, y2):
        self.merge.append([x1, y1, x2, y2])

    def add_row(self, *args):
        self.data.append(args)

    def _find_value_for_merge(self, x1: int, y1: int, x2: int, y2: int):
        """
        Поиск значения для записи в объединенную ячейку.
        Записывается первое значение из выбранных ячеек для объединения
        """
        for x, row in enumerate(self.data):
            for y, col in enumerate(row):
                if x1 <= x <= x2 and y1 <= y <= y2:
                    if self.data[x][y]:
                        return self.data[x][y]

        return None


class SectionsWorksheet(Worksheet):
    """
    Класс для добавления данных в форме двумерной матрицы в xlsx-таблицу
    """

    def add_section(
        self, section, x, y=None, style=None, bottom_indent=0, right_indent=0
    ):
        """
        :param section: двумерная матрица список списков
        :param x: координата по вертикали
        :param y: по горизонтали
        :param style: базовый стиль, который будет применен если у конкретной ячейки не указан свой стиль
            Если необходимо, чтобы у столбца двумерной матрицы был иной стиль, можно сделать так:
                cell_format = workbook.calculate_style(CellFormat(size=10))
                cell_format2 = workbook.calculate_style(CellFormat(size=10, border=1))

                section = Section()

                for record in records:
                    info = [
                        data1,
                        data2,
                        [data3, cell_format2], #Так как элемент является списком, программа примет особый стиль
                        ...,
                        data(n)
                    ]
                    section.add_row(*info)
                sheet.add_section(section, number_row, style=cell_format)

        :param bottom_indent: отступ снизу
        :param right_indent: отступ справа
        :return:
        """
        if y is None:
            y = 0

        start_x = x
        start_y = y

        for row in section.data:
            temp_y = y
            for col in row:
                if isinstance(col, list):
                    value = col[0]
                    concrete_style = col[1]
                else:
                    value = col
                    concrete_style = None
                self.write(x, temp_y, value, concrete_style or style)
                temp_y += 1
            x += 1

        for merge in section.merge:  #
            col = section._find_value_for_merge(*merge)

            x1, y1, x2, y2 = merge

            if isinstance(col, list):
                value = col[0]
                concrete_style = col[1]
            else:
                value = col
                concrete_style = None

            self.merge_range(
                x1 + start_x,
                y1 + start_y,
                x2 + start_x,
                y2 + start_y,
                value,
                concrete_style or style,
            )

        section.x = start_x
        section.y = start_y

        section.last_x = x + bottom_indent

        if section.data:
            max_length = max(len(_) for _ in section.data)
        else:
            max_length = 0

        section.last_y = y + max_length + right_indent


Workbook.worksheet_class = SectionsWorksheet
