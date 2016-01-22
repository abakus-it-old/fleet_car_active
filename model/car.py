from openerp import models, fields

class CarWithAttachment(models.Model):
    _inherit = 'fleet.vehicle'
    
    active = fields.Boolean(string="Active")