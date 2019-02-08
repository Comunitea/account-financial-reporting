# Copyright 2018 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Partner Outstanding Statement',
    'version': '11.0.2.1.1',
    'category': 'Accounting & Finance',
    'summary': 'OCA Financial Reports',
    'author': "Eficent, Odoo Community Association (OCA)",
    'website': 'https://github.com/OCA/account-financial-reporting',
    'license': 'AGPL-3',
    'depends': [
        'account_invoicing',
    ],
    'data': [
        'views/statement.xml',
        'wizard/customer_outstanding_statement_wizard.xml',
    ],
    'installable': True,
    'application': False,
}
