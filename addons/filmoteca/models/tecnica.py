# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tecnica(models.Model):
    _name = 'filmoteca.tecnica'
    _description = 'filmoteca.tecnica'

    name = fields.Char()
    description = fields.Text()

    photo = fields.Image()
    peliculas_id = fields.Many2many("filmoteca.pelicula")

    

