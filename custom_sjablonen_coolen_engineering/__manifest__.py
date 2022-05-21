{
    "name": "Custom sjablonen Coolen Engineering",
    "summary": "Odoo sjablonen op maat voor Coolen Engineering B.V.",
    "version": "14.0.1.0.0",
    "category": "report",
    "website": "https://odiots.com",
    "author": "Odiots Odoo Partner",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "sale_management",
        "stock",
        "mrp",
        "purchase",
    ],
    "data": [
        # Report
        "reports/delivery_slip_template.xml",
        "reports/report_layout.xml",
        "reports/report_invoice_template.xml",
        "reports/report_purchase_template.xml",
        "reports/report_rfq_template.xml",
        "reports/report_sale_template.xml",
        "reports/report_mo_barcode_template.xml",
        "reports/report_product_barcode_template.xml",
        "reports/report_picking_product_barcode_template.xml",
        # Data
        "data/report_layout.xml",
    ],
}
