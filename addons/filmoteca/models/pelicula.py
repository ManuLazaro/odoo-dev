# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class pelicula(models.Model):
    _name = 'filmoteca.pelicula'
    _description = 'filmoteca.pelicula'


    code = fields.Char(compute="_get_code")
    name = fields.Char(string="Nombre", readonly = False, required=True, help="Introduzca el nombre")
    description = fields.Text()
    film_date = fields.Date()
    duration = fields.Integer()
    start_date = fields.Datetime()
    end_date = fields.Datetime(compute="_get_end_date", store = True)
    is_spanish = fields.Boolean()
    image = fields.Image()
    language =  fields.Selection([('Es','Español'), ('In','Inglés'), ('De','Alemán'), ('Fr','Francés')], default='Es')
    opinion =  fields.Selection([('0','Mala'), ('1','Regular'), ('2','Buena')], default='1')
    color = fields.Boolean()
    genero_id = fields.Many2one("filmoteca.genero", "Género", required = True, ondelete = "cascade")
    tecnicas_id = fields.Many2many("filmoteca.tecnica")
    
    #@api.one Para recibir un único objeto
    def _get_code(self):
        for pelicula in self:
            if len(pelicula.genero_id) == 0:
                pelicula.code = "FILM_"+str(pelicula.id)
            else:
                pelicula.code = str(pelicula.genero_id.name).upper()+ "_"+str(pelicula.id)

    # Este decorador: @api.depends, permite recibir uno o varios atributos
    @api.depends("start_date", "duration")
    def _get_end_date(self):
        for pelicula in self:
            if isinstance(pelicula.start_date, datetime.datetime) and pelicula.duration > 0:
                pelicula.end_date = pelicula.start_date + datetime.timedelta(days=pelicula.duration)
            else:
                pelicula.end_date = pelicula.start_date

    
# Terminación en _ids para los campos de las tablas en una relación Many2many

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
