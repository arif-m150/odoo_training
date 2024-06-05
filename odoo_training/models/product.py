from odoo import _, api, fields, models

class ProductProduct(models.Model):
    _inherit = 'product.product'
    
    course_id = fields.Many2one('training.course', string='Judul Kursus', required=False, ondelete='cascade')
    