# -*- coding: utf-8 -*-
# from odoo import http


# class Sistema2(http.Controller):
#     @http.route('/sistema2/sistema2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sistema2/sistema2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sistema2.listing', {
#             'root': '/sistema2/sistema2',
#             'objects': http.request.env['sistema2.sistema2'].search([]),
#         })

#     @http.route('/sistema2/sistema2/objects/<model("sistema2.sistema2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sistema2.object', {
#             'object': obj
#         })
