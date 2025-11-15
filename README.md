# Inaya ERPNext App

This is a custom ERPNext v15 application developed as part of a technical assessment.  
It includes two modules:

---

## 📦 Module 1 — Agency Management
- **Agency** DocType (agency_name, territory, primary_contact, is_active)
- **Agency Item** child table (item_code, min_order_qty, lead_time_days)
- Prevent deactivation if linked Agency Items exist
- Button **“Create Supplier”** converts Agency → Supplier
- Inactive agencies highlighted in list view
- Report: **Agency Lead Times**

---

## 📦 Module 2 — Manufacturer–Item Mapping
- **Manufacturer** DocType (manufacturer_name, gln, is_blocked)
- **Manufacturer Item** DocType (manufacturer, item_code, part_number, gtin)
- Block adding mappings if manufacturer is blocked
- Unique pair enforced: **(manufacturer, item_code)**
- Auto-fill `part_number` from `item_code`
- REST API:

- Report: **Items by Manufacturer**

---

## 🛠️ Installation
```bash
bench get-app https://github.com/amelsuliman/Inaya.git
bench --site <site-name> install-app
bench --site <site-name> migrate
 inaya
bench build
bench restart
