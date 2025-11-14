frappe.ui.form.on('Agency', {
    refresh(frm) {
        // New record: ensure Is Active is checked in UI
        if (frm.is_new() && !frm.doc.is_active) {
            frm.set_value('is_active', 1);
        }

        // Only show "Create -> Supplier" on saved docs
        if (!frm.is_new()) {
            // only if Supplier not already linked
            if (!frm.doc.supplier) {
                frm.add_custom_button(__('Supplier'), () => {
                    frappe.call({
                        method: 'inaya.inaya.doctype.agency.agency.create_supplier',
                        args: {
                            agency_name: frm.doc.name,
                        },
                        freeze: true,
                        freeze_message: __('Creating Supplier...'),
                        callback(r) {
                            if (!r.exc) {
                                frm.reload_doc(); // show new Supplier link
                            }
                        },
                    });
                }, __('Create')); // appears under the "Create" menu, like "Create Payment"
            }
        }
    },
});
