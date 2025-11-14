# inaya/inaya/doctype/agency/agency.py

import frappe
from frappe.model.document import Document
from frappe import _


class Agency(Document):
    def before_save(self):
        """Runs before every save."""
        self.ensure_default_active()
        self.prevent_deactivation_if_items()

    def ensure_default_active(self):
        """Make sure new Agency is Active by default."""
        if self.is_new() and not self.is_active:
            self.is_active = 1

    def prevent_deactivation_if_items(self):
        """
        If an existing Agency is being changed from Active -> Inactive
        AND there are items in the child table, block the save.
        """
        # New doc: nothing to compare
        if self.is_new():
            return

        old = self.get_doc_before_save()

        # WAS active, NOW trying to set inactive
        if old.is_active and not self.is_active:
            # IMPORTANT: if your child table fieldname is not "items",
            # change "items" below to your actual fieldname.
            items = self.get("items") or []

            if items:
                frappe.throw(
                    _(
                        "Cannot deactivate Agency {0} because it has linked items. "
                        "Remove items or keep the Agency Active."
                    ).format(self.name)
                )


@frappe.whitelist()
def create_supplier(agency_name: str):
    """Create a Supplier from an Agency and link it back."""
    agency = frappe.get_doc("Agency", agency_name)

    # Check that the Agency doc has a 'supplier' field
    if not hasattr(agency, "supplier"):
        frappe.throw(
            _(
                "Field 'supplier' (Link to Supplier) is missing on Agency DocType. "
                "Please add a Link field named 'supplier' pointing to Supplier."
            )
        )

    # Avoid duplicates
    if agency.supplier:
        frappe.throw(_("Supplier already linked: {0}").format(agency.supplier))

    # Use Agency Name as Supplier Name
    supplier_name = getattr(agency, "agency_name", None) or agency.name

    # Territory is optional; include it if present
    supplier_data = {
        "doctype": "Supplier",
        "supplier_name": supplier_name,
        # supplier_type will use the default (usually "Company")
    }
    if getattr(agency, "territory", None):
        supplier_data["territory"] = agency.territory

    supplier = frappe.get_doc(supplier_data)
    supplier.insert(ignore_permissions=True)

    # Link back to Agency
    agency.supplier = supplier.name
    agency.save(ignore_permissions=True)

    frappe.msgprint(
        _("Supplier {0} created and linked to Agency {1}.").format(
            supplier.name, agency.name
        ),
        alert=True,
    )

    return supplier.name

