# -*- coding: utf-8 -*-
{
    'name': "Gestión Taller",

    'summary': """Gestión de Vehiculos y Reparación""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Aldaba Servicios Profesionales",
    'website': "http://www.aldaba.es",
    'version': '0.1',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Gestión Vehiculo',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        "security/ir.model.access.csv",
        "views/vehiculo_view.xml",
    ],
}