from openerp import api, fields, models


class PartnerCURP(models.Model):
    _inherit = 'res.partner'

    curp = fields.Char('CURP')
