# -*- coding: utf-8 -*-
from odoo import http

# class EdariTimesheet(http.Controller):
#     @http.route('/edari_timesheet/edari_timesheet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edari_timesheet/edari_timesheet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('edari_timesheet.listing', {
#             'root': '/edari_timesheet/edari_timesheet',
#             'objects': http.request.env['edari_timesheet.edari_timesheet'].search([]),
#         })

#     @http.route('/edari_timesheet/edari_timesheet/objects/<model("edari_timesheet.edari_timesheet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edari_timesheet.object', {
#             'object': obj
#         })