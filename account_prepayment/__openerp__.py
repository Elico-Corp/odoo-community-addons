# -*- coding: utf-8 -*-
# © 2017 - Shanghai SITA Waste Treatment Services Company Limited.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Account Prepayment',
    'version': '7.0.1.0.0',
    'category': 'Account',
    'summary': 'Account Prepayment',
    'description': """
Create the possibility to generate the prepayment  directly from the payment wizard:

 * add a check box in the payment form Prepayment: if checked the prepayment account in the partner will be chosen

 * Usage for Supplier:

 * Prepayment Move (At money reception, use the payment form with prepayment and select no invoice). It creates:

 * Create an Invoice

 * New Payment (after invoice is created),use the payment form (no prepayment option and select the invoice and already existing Prepayment move)

    """,
    'author': 'Elico Corp',
    'website': 'https://www.elico-corp.com',
    'depends': ['account', 'account_voucher'],
    'data': [
        'account_view.xml',
    ],
    'installable': True,
}

