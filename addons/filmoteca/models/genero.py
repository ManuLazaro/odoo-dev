# -*- coding: utf-8 -*-

from odoo import models, fields, api


class genero(models.Model):
    _name = 'filmoteca.genero'
    _description = 'filmoteca.genero'

    name = fields.Char()
    description = fields.Text()

    peliculas_id = fields.One2many(string= "Películas", comodel_name="filmoteca.pelicula", inverse_name="genero_id")



#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
