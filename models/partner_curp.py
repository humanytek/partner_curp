from openerp import api, exceptions, fields, models, _


class PartnerCURP(models.Model):
    _inherit = 'res.partner'

    curp = fields.Char('CURP')

    @api.one
    @api.constrains('curp')
    def _check_curp(self):
        if self.curp:
            if len(self.curp) != 18:
                raise exceptions.ValidationError(_('Invalid CURP'))
