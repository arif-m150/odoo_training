# -*- coding: utf-8 -*-
{
    'name': "Odoo Training",

    'summary': "Module Training Odoo",

    'description': """
Module Training technical Odoo
    """,

    'author': "Arif M.",
    'website': "https://www.jukesolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','mail'],

    # always loaded
    'data': [
        'data/data.xml',
        'data/scheduler_data.xml',
        'data/sequence_data.xml',
        'report/report_training_session.xml',
        'report/report_action.xml',
        "security/security.xml",
        "security/model_access.xml",
        # 'security/ir.model.access.csv',
        'views/training_views.xml',
        'views/partner_views.xml',
        'wizard/training_wizard_views.xml',
        'views/menuitem.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}

