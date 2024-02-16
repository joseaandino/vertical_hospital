from odoo import http
from odoo.http import Response, request

class patientController(http.Controller):
    @http.route('/pacientes/consulta', type='http', auth="public")
    def get_patient(self):
        # get the patient based in the seq(name field)
        patients_rec = request.env['patient.hospital'].search([])
        for rec in patients_rec:
            vals = {
                'seq': rec.name,
                'name': rec.first_name,
                'rnc': rec.nif,
                'state': rec.state,
            }
        data = {
            'status': "200",
            'message': "success",
            'response': vals,
        }
        return data