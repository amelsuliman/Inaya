import frappe
from frappe import _


def execute(filters=None):
    filters = frappe._dict(filters or {})
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {
            "label": _("Agency"),
            "fieldname": "agency",
            "fieldtype": "Link",
            "options": "Agency",
            "width": 180,
        },
        {
            "label": _("Item"),
            "fieldname": "item_code",
            "fieldtype": "Link",
            "options": "Item",
            "width": 180,
        },
        {
            "label": _("Min Order Qty"),
            "fieldname": "min_order_qty",
            "fieldtype": "Float",
            "width": 120,
        },
        {
            "label": _("Lead Time (Days)"),
            "fieldname": "lead_time_days",
            "fieldtype": "Int",
            "width": 140,
        },
    ]


def get_data(filters):
    """
    Reads from child table "Agency Item" and returns:
      - parent (Agency)       -> agency
      - <item-link-field>     -> item_code
      - min_order_qty
      - lead_time_days

    It does NOT assume the item field is called 'item_code'.
    Instead, it looks for the first Link field whose options == 'Item'.
    """

    # Find the actual item fieldname dynamically
    meta = frappe.get_meta("Agency Item")
    item_fieldname = None
    for df in meta.fields:
        if df.fieldtype == "Link" and df.options == "Item":
            item_fieldname = df.fieldname
            break

    if not item_fieldname:
        # No Link-to-Item field found; tell the user clearly
        frappe.throw(
            _(
                "No Link field to Item found in 'Agency Item' DocType. "
                "Please add a Link field pointing to Item, or update the report logic."
            )
        )

    conditions = {"parenttype": "Agency"}

    # Optional filter by Agency (if you add it as a filter in the report)
    if filters.get("agency"):
        conditions["parent"] = filters.agency

    # Build fields list using the detected item_fieldname
    fields = [
        "parent as agency",
        f"{item_fieldname} as item_code",
        "min_order_qty",
        "lead_time_days",
    ]

    rows = frappe.get_all(
        "Agency Item",
        fields=fields,
        filters=conditions,
        order_by="agency asc, item_code asc",
    )

    return rows

