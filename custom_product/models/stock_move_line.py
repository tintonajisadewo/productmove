from odoo import models, fields, api

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    partner_name = fields.Many2one(
        comodel_name='res.partner', 
        string="Partner Name", 
        related="move_id.picking_id.partner_id", 
        store=True, 
        readonly=True)
    cost_price = fields.Monetary(compute="_compute_cost_price", string="Cost Price", currency_field="currency_id")
    currency_id = fields.Many2one("res.currency", string="Currency", related='move_id.company_id.currency_id', required=True)

    @api.depends('move_id.sale_line_id.price_unit', 'move_id.purchase_line_id.price_unit')
    def _compute_cost_price(self):
        for rec in self:
            rec.cost_price = 0
            if rec.move_id.sale_line_id:
                rec.cost_price = rec.move_id.sale_line_id.price_unit
            elif rec.move_id.purchase_line_id:
                rec.cost_price = rec.move_id.purchase_line_id.price_unit
