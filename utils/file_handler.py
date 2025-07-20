# utils/file_handler.py

import openpyxl


def read_song_list(file_path):
    """Reads a list of songs from a .txt or .xlsx file."""
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    elif file_path.endswith('.xlsx'):
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        return [cell.value for row in sheet.iter_rows() for cell in row if cell.value]
    else:
        raise ValueError("Unsupported file type.")
