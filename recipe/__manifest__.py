# -*- coding: utf-8 -*-
{
    'name': "recipe",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing""",

    'description': """
        Long description of module's purpose
    """,

    # 'author': "pda",
    # 'website': "https://odoo.com",

    'category': 'Uncategorized',
    'version': '15.0.0.0.1',

    'depends': [],

    'data': [
        'views/recipe.xml',
        'views/ingredient.xml',
        'security/ir.model.access.csv',

    ],

    'installable':True,
}
