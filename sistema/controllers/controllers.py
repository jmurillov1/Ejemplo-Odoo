# -*- coding: utf-8 -*-
# from odoo import http


# class Sistema(http.Controller):
#     @http.route('/sistema/sistema/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sistema/sistema/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sistema.listing', {
#             'root': '/sistema/sistema',
#             'objects': http.request.env['sistema.sistema'].search([]),
#         })

#     @http.route('/sistema/sistema/objects/<model("sistema.sistema"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sistema.object', {
#             'object': obj
#         })
