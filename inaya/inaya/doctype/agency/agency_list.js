// inaya/inaya/doctype/agency/agency_list.js

frappe.listview_settings['Agency'] = {
    get_indicator(doc) {
        if (!doc.is_active) {
            // label, color, filter
            return [__('Inactive'), 'red', 'is_active,=,0'];
        } else {
            return [__('Active'), 'green', 'is_active,=,1'];
        }
    },
};
