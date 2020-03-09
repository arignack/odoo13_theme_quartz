# -*- coding: utf-8 -*-
{
    'name': "Odoo Theme Quartz",

    'summary': """
        A theme that resemble the Quartz,
    """,
    'description': """
        Basic theme following the Odoo 13 documentation. 
    """,

    'author': "Alián Rigñack",
    'website': "http://medium.com/@arignack",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Theme',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/layout.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}