# -*- coding: utf-8 -*-
# from odoo import http


# class Filmoteca(http.Controller):
#     @http.route('/filmoteca/filmoteca', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/filmoteca/filmoteca/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('filmoteca.listing', {
#             'root': '/filmoteca/filmoteca',
#             'objects': http.request.env['filmoteca.filmoteca'].search([]),
#         })

#     @http.route('/filmoteca/filmoteca/objects/<model("filmoteca.filmoteca"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('filmoteca.object', {
#             'object': obj
#         })
