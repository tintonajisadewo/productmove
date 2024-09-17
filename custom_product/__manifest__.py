# -*- coding: utf-8 -*-
{
    'name': "Custom Product move view Partner Name and Cost Unit",
    'version': "11.0.0.0",
    'category': "Product",
    'license': 'OPL-1',
    'price': '30.0',
    'currency': 'USD',
    'summary': """
        View Product move tree view partner name and cost unit in odoo 11""",

    'description': """
         View Product move tree view partner name and cost unit in odoo 11
         Unit price in view product move 
         Partner name in view product move
    """,

    'author': "Tinton Aji Sadewo",
    'website': "https://tintonajisadewo.github.io/",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'security/security.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/stock_move_line_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    "images": ['static/description/banner.png'],
}


# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
