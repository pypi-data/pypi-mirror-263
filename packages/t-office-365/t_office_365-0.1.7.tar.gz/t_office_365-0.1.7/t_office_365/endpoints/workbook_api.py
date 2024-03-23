"""This module contains the endpoints for the workbook API."""


def worksheets(drive_id, file_id):
    """Get worksheets field."""
    return f"/drivses/{drive_id}/items/{file_id}/workbook/worksheets"


def get_row_data(drive_id, file_id, sheet_name, min_row: int = 1, max_row: int = 100, min_column="A", max_column="Z"):
    """Get row data field."""
    return (
        f"/drives/{drive_id}/items/{file_id}/workbook/worksheets/"
        f"{sheet_name}/range(address='{min_column}{min_row}:{max_column}{max_row}')"
    )


def get_cell_value(drive_id, file_id, sheet_name, row, column):
    """Update excel endpoint field.

    Returns:
        str: update excel endpoint
    """
    return f"/drives/{drive_id}/items/{file_id}/workbook/worksheets/{sheet_name}/cell(row={row}, column={column})"


def update_row_data(drive_id, file_id, sheet_name, address):
    """Update row data.

    Returns:
        str: get row data
    """
    return f"/drives/{drive_id}/items/{file_id}/workbook/worksheets/{sheet_name}/range(address='{address}')"
