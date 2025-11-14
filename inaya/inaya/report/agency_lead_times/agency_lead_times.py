# inaya/inaya/report/agency_lead_times/agency_lead_times.py

import frappe
from frappe import _


def execute(filters=None):
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
            "width": 200,
        },
        {
            "label": _("Item"),
            "fieldname": "item_code",
            "fieldtype": "Link",
            "options": "Item",
            "width": 200,
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


def get_data(filters=None):
    return frappe.db.sql(
        """
        SELECT
            ai.parent        AS agency,
            ai.item_code     AS item_code,
            ai.min_order_qty AS min_order_qty,
            ai.lead_time_days
        FROM `tabAgency Item` ai
        INNER JOIN `tabAgency` a
            ON a.name = ai.parent
        WHERE a.docstatus < 2
        ORDER BY a.agency_name, ai.item_code
        """,
        as_dict=True,
    )
