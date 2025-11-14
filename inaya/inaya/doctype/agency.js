// inaya/inaya/doctype/agency/agency.js

frappe.ui.form.on('Agency', {
    refresh(frm) {
        // Only show button when document is saved
        if (!frm.is_new()) {
            frm.add_custom_button(__('Create Supplier'), () => {
                frappe.call({
                    method: 'inaya.inaya.doctype.agency.agency.create_supplier',
                    args: {
                        agency_name: frm.doc.name,
                    },
                    callback(r) {
                        if (!r.exc) {
                            frm.reload_doc(); // refresh to show linked supplier
                        }
                    },
                });
            }, __('Actions'));
        }
    },
});
