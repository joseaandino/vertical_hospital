# -*- coding: utf-8 -*-
##############################################################################
#
#    MoviTrack
#    Copyright (C) 2020-TODAY MoviTrack.
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Vertical Hospital",
    "version": "16.0.1",
    "description": "Modulo para gestion y control de pacientes y tratamientos medicos",
    "author": "Jose Antonio Andino",
    "depends": [
        "base", "mail"
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/sequences.xml",
        "views/root_menu.xml",
        "views/patient_view.xml",
        "views/treatment_view.xml",
        "report/patient_report.xml",
        "report/patient_template.xml",
        "views/hospital_settings_form.xml",
    ],
    'installable': True,
}