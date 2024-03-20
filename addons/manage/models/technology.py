# -*- coding: utf-8 -*-

from odoo import models, fields, api


class technology(models.Model):
     _name = 'manage.technology'
     _description = 'manage.technology'

     name = fields.Char()
     description = fields.Char()
     photo = fields.Image()
     task_ids = fields.Many2many('manage.task', string='tasks')


