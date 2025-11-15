app_name = "inaya"
app_title = "Inaya"
app_publisher = "Amel"
app_description = "Inaya App"
app_email = "amel.moh144@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "inaya",
# 		"logo": "/assets/inaya/logo.png",
# 		"title": "Inaya",
# 		"route": "/inaya",
# 		"has_permission": "inaya.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/inaya/css/inaya.css"
# app_include_js = "/assets/inaya/js/inaya.js"

# include js, css files in header of web template
# web_include_css = "/assets/inaya/css/inaya.css"
# web_include_js = "/assets/inaya/js/inaya.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "inaya/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "inaya/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "inaya.utils.jinja_methods",
# 	"filters": "inaya.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "inaya.install.before_install"
# after_install = "inaya.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "inaya.uninstall.before_uninstall"
# after_uninstall = "inaya.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "inaya.utils.before_app_install"
# after_app_install = "inaya.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "inaya.utils.before_app_uninstall"
# after_app_uninstall = "inaya.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "inaya.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"inaya.tasks.all"
# 	],
# 	"daily": [
# 		"inaya.tasks.daily"
# 	],
# 	"hourly": [
# 		"inaya.tasks.hourly"
# 	],
# 	"weekly": [
# 		"inaya.tasks.weekly"
# 	],
# 	"monthly": [
# 		"inaya.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "inaya.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "inaya.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "inaya.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["inaya.utils.before_request"]
# after_request = ["inaya.utils.after_request"]

# Job Events
# ----------
# before_job = ["inaya.utils.before_job"]
# after_job = ["inaya.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"inaya.auth.validate"

fixtures = [
    # Workspaces for Inaya module
    {
        "dt": "Workspace",
        "filters": [
            ["module", "=", "Inaya"]
        ],
    },

    # Client Scripts belonging to Inaya module
    {
        "dt": "Client Script",
        "filters": [
            ["module", "=", "Inaya"]
        ],
    },

    # ---- Sample Data Fixtures (for assignment) ----

    # Agencies: only these two
    {
        "dt": "Agency",
        "filters": [
            ["name", "in", ["AGY-2025-00008", "AGY-2025-00003"]]
        ],
    },

    # Items: only these three
    {
        "dt": "Item",
        "filters": [
            ["item_code", "in", ["RAW-2024-00037", "RAW-2024-00001", "RAW-2024-00002"]]
        ],
    },

    # Manufacturers: only the two you shared
    {
        "dt": "Manufacturers",
        "filters": [
            ["name", "in", ["MAN-2025-00002", "MAN-2025-00003"]]
        ],
    },

    # All Manufacturer Item mappings (for those items/manufacturers)
    {
        "dt": "Manufacturer Item",
    },

    # All Agency Item child rows (for those agencies)
    {
        "dt": "Agency Item",
    },
]

