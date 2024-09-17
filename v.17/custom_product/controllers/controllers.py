# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAccountReports(http.Controller):
#     @http.route('/custom_account_reports/custom_account_reports', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_account_reports/custom_account_reports/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_account_reports.listing', {
#             'root': '/custom_account_reports/custom_account_reports',
#             'objects': http.request.env['custom_account_reports.custom_account_reports'].search([]),
#         })

#     @http.route('/custom_account_reports/custom_account_reports/objects/<model("custom_account_reports.custom_account_reports"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_account_reports.object', {
#             'object': obj
#         })
