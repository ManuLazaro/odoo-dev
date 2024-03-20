# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json


class TaskController(http.Controller):
    @http.route('/api/task', auth='public', method=['GET'], csrf=False)
    def get_task(self, **kw):
        try:
            task = http.request.env['manage.task'].sudo().search_read([], ['id', 'name', 'color'])
            res = json.dumps(task, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error':str(e)}), content_type ='application/json;charset=utf-8', status=505)

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
