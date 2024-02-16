from odoo import http
from odoo.http import Response, request
from odoo.tools import json_default
import json


#Rest Api for returning the patient passed in the path
class patientController(http.Controller):
    @http.route('/pacientes/consulta/<string:name>', type='http', auth="none", crsf=False, methods=['GET'])
    def get_patient(self, name):
        # get the patient based in the seq(name field)
        patients_rec = request.env['patient.hospital'].sudo().search([('name', '=', name)])
        vals = {}
        if patients_rec:
            for rec in patients_rec:
                vals = {
                    'seq': rec.name,
                    'name': rec.first_name,
                    'rnc': rec.nif,
                    'state': rec.state,
                }
        return Response(json.dumps(vals, default=json_default), content_type='application/json;charset=utf-8',status=200)