"""This module contains the endpoints for the workbook API."""


def worksheets(drive_id, file_id):
    """Get worksheets field."""
    return f"/drivses/{drive_id}/items/{file_id}/workbook/worksheets"


def get_row_data(drive_id, file_id, sheet_name, max_row, max_column="Z"):
    """Get row data field."""
    return (
        f"/drives/{drive_id}/items/{file_id}/workbook/worksheets/{sheet_name}/range(address='A1:{max_column}{max_row}')"
    )


def get_specific_row(drive_id, file_id, sheet_name, row, max_column):
    """Get specific row data field."""
    return (
        f"/drives/{drive_id}/items/{file_id}/workbook/worksheets/{sheet_name}/range(address='A{row}:{max_column}{row}')"
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
