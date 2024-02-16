from odoo import api, fields, models
from odoo.exceptions import ValidationError


class patientHospital(models.Model):
    _name = 'patient.hospital'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Gestión de pacientes'
    
    name = fields.Char(string='Nombre')
    first_name = fields.Char(string="Nombre del paciente")
    last_name = fields.Char(string="Apellido del paciente")
    nif = fields.Char(string="Documento de identidad", tracking=True)
    treatment_id = fields.Many2one('treatment.hospital', "Tratamiento Realizado")
    treatment_code = fields.Char(related='treatment_id.code', store=True)
    treatment_name = fields.Char(related='treatment_id.name', store=True)
    entry_date = fields.Datetime(string="Fecha de alta")
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('entry', 'Alta'),
        ('discharge', 'Baja'),
    ], string='Estado', default='draft', tracking=True)
    
    #Generate sequence for name field when the record is created
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('seq.patient')
        res = super(patientHospital, self).create(vals)
        return res
    
    @api.constrains('nif')
    def _validation_nif(self):
        for i in self.nif:
            if i.isalpha():
                raise ValidationError("El documento de identidad no puede contener letras")
        
        