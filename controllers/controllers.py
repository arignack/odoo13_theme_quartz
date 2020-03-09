# -*- coding: utf-8 -*-
from odoo import http

# class Odoo13ThemeQuartz(http.Controller):
#     @http.route('/odoo13_theme_quartz/odoo13_theme_quartz/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo13_theme_quartz/odoo13_theme_quartz/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo13_theme_quartz.listing', {
#             'root': '/odoo13_theme_quartz/odoo13_theme_quartz',
#             'objects': http.request.env['odoo13_theme_quartz.odoo13_theme_quartz'].search([]),
#         })

#     @http.route('/odoo13_theme_quartz/odoo13_theme_quartz/objects/<model("odoo13_theme_quartz.odoo13_theme_quartz"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo13_theme_quartz.object', {
#             'object': obj
#         })