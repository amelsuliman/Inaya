import frappe
from frappe.model.document import Document
from frappe import _


class ManufacturerItem(Document):
    def validate(self):
        self.validate_manufacturer_not_blocked()
        self.ensure_unique_pair()
        self.set_default_part_number()

    def validate_manufacturer_not_blocked(self):
        """Block adding/updating if Manufacturer is blocked."""
        if self.manufacturer:
            manufacturer = frappe.get_cached_doc("Manufacturers", self.manufacturer)
            if getattr(manufacturer, "is_blocked", 0):
                frappe.throw(
                    _("Cannot add item for blocked Manufacturer {0}.").format(self.manufacturer)
                )

    def ensure_unique_pair(self):
        """Ensure (manufacturer, item_code) pair is unique across Manufacturer Item."""
        if not (self.manufacturer and self.item_code):
            return

        exists = frappe.db.exists(
            "Manufacturer Item",
            {
                "manufacturer": self.manufacturer,
                "item_code": self.item_code,
                "name": ["!=", self.name],
            },
        )

        if exists:
            frappe.throw(
                _("Manufacturer {0} is already mapped to Item {1}.").format(
                    self.manufacturer, self.item_code
                )
            )

    def set_default_part_number(self):
        """If part_number is empty, auto-fill from item_code."""
        if not self.part_number and self.item_code:
            self.part_number = self.item_code


@frappe.whitelist()
def get_mappings(item_code: str):
    """
    REST API: return all manufacturer mappings for a given item_code.

    Example:
    /api/method/inaya.inaya.doctype.manufacturer_item.manufacturer_item.get_mappings?item_code=ITEM-0001
    """
    if not item_code:
        return []

    rows = frappe.get_all(
        "Manufacturer Item",
        filters={"item_code": item_code},
        fields=["name", "manufacturer", "item_code", "part_number", "gtin"],
        order_by="manufacturer asc",
    )
    return rows
