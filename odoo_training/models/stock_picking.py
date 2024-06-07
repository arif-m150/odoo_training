from odoo import _, api, fields, models

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    def button_validate(self):
        for rec in self:
            rec.user_id = self.env.uid
        return super(StockPicking, self).button_validate()
    