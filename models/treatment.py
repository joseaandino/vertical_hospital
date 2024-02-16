from odoo import api, fields, models
from odoo.exceptions import ValidationError


class treatmentHospital(models.Model):
    _name = 'treatment.hospital'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Manejo de las diferentes especialidades de los doctores'

    name = fields.Char(string='Nombre del tratamiento', required=True)
    code = fields.Char(string='Codigo del tratamiento', required=True)
    doctor = fields.Char(string='Medico asignado', required=True)


    @api.constrains('code')
    def _validation_code(self):
        if "026" in self.code:
            raise ValidationError("El codigo de tratamiento no puede contener el codigo 026")