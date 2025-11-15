import frappe
from frappe import _


def execute(filters=None):
    filters = filters or {}
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {
            "label": _("Manufacturer"),
            "fieldname": "manufacturer",
            "fieldtype": "Link",
            "options": "Manufacturers",
            "width": 180,
        },
        {
            "label": _("Item"),
            "fieldname": "item_code",
            "fieldtype": "Link",
            "options": "Item",
            "width": 160,
        },
        {
            "label": _("Part Number"),
            "fieldname": "part_number",
            "fieldtype": "Data",
            "width": 160,
        },
        {
            "label": _("GTIN"),
            "fieldname": "gtin",
            "fieldtype": "Data",
            "width": 160,
        },
    ]


def get_data(filters):
    conditions = {}

    # optional filters: manufacturer, item_code
    if filters.get("manufacturer"):
        conditions["manufacturer"] = filters["manufacturer"]
    if filters.get("item_code"):
        conditions["item_code"] = filters["item_code"]

    return frappe.get_all(
        "Manufacturer Item",
        filters=conditions,
        fields=["manufacturer", "item_code", "part_number", "gtin"],
        order_by="manufacturer asc, item_code asc",
    )
