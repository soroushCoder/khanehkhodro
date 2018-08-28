# -*- coding: utf-8 -*-
from odoo import http

# class ArtaradKhanehkhodroTheme(http.Controller):
#     @http.route('/artarad_khanehkhodro_theme/artarad_khanehkhodro_theme/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/artarad_khanehkhodro_theme/artarad_khanehkhodro_theme/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('artarad_khanehkhodro_theme.listing', {
#             'root': '/artarad_khanehkhodro_theme/artarad_khanehkhodro_theme',
#             'objects': http.request.env['artarad_khanehkhodro_theme.artarad_khanehkhodro_theme'].search([]),
#         })

#     @http.route('/artarad_khanehkhodro_theme/artarad_khanehkhodro_theme/objects/<model("artarad_khanehkhodro_theme.artarad_khanehkhodro_theme"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('artarad_khanehkhodro_theme.object', {
#             'object': obj
#         })