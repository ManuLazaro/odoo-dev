# -*- coding: utf-8 -*-

from odoo import models, fields, api


class project(models.Model):
     _name = 'manage.project'
     _description = 'manage.project'

     name = fields.Char()
     description = fields.Char()
     history_ids = fields.One2many('manage.history', 'project_id', string='history')
     sprint_ids = fields.One2many('manage.sprint', 'project_id', string='sprint')
     customer_id = fields.Many2one('manage.customer', string='customer') 

