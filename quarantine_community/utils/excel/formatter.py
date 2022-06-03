import pathlib

import openpyxl
from string import ascii_uppercase
from openpyxl.styles import Font
from openpyxl.styles import DEFAULT_FONT


def format(file_path: pathlib.Path):
    newFile = file_path

    wb = openpyxl.load_workbook(filename=newFile)
    worksheet = wb.active
    # _font = Font(name="Arial", sz=16, b=True)
    # {k: setattr(DEFAULT_FONT, k, v) for k, v in _font.__dict__.items()}

    for col in worksheet.columns:
        max_length = 0
        column = col[0].column_letter  # Get the column name
        for cell in col:
            try:  # Necessary to avoid error on empty cells
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2) * 1.5
        worksheet.column_dimensions[column].width = adjusted_width

        # worksheet[col].font = font
    # DEFAULT_FONT.name = "Microsoft YaHei UI"

    wb.save(newFile)
