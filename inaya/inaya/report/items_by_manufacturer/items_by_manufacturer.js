/* Inaya - Items by Manufacturer report JS */

frappe.query_reports["Items by Manufacturer"] = {
    filters: [
        {
            fieldname: "manufacturer",
            label: __("Manufacturer"),
            fieldtype: "Link",
            options: "Manufacturers"
        },
        {
            fieldname: "item_code",
            label: __("Item"),
            fieldtype: "Link",
            options: "Item"
        }
    ]
};
