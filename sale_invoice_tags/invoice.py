# -*- coding: utf-8 -*-

from openerp import fields, models, api, _

class account_invoice(models.Model):
    _inherit = 'account.invoice'
    
    categ_ids = fields.Many2many('crm.lead.tag', 'sale_invoice_category_rel', 'invoice_id', 'category_id', 'Sale Tags')

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    @api.multi
    def _prepare_invoice(self):
        result = super(SaleOrder, self)._prepare_invoice()
        tags = self.tag_ids
        result.update({'categ_ids': [(6, 0, tags.ids)]})
        return result

class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"
    
    @api.multi
    def _create_invoice(self, order, so_line, amount):
        res = super(SaleAdvancePaymentInv, self)._create_invoice(order, so_line, amount)
        tags = order.tag_ids
        res.categ_ids = tags
        return res

