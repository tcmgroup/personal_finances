{
    'name': 'Personal Finances',
    'version': '16.0.1.0.0',
    'summary': 'A module to manage personal finances.',
    'description': """
        This module helps you track your income and expenses, allowing for a clear view of your financial status.
    """,
    'author': 'Carlos Espetia',
    'website': 'https://www.carlosespetia.com',
    'category': 'Uncategorized',
    'depends': ['base', 'mail'],
    'data': [
        'security/personal_finances_security.xml',
        'security/ir.model.access.csv',
        'views/bank_account_views.xml',
        'views/personal_finances_transaction_views.xml',
        'views/personal_finances_tag_views.xml',
        'views/personal_finances_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
