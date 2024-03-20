from odoo import models, fields, api


class customer(models.Model):  
    _name = 'manage.customer'
    _description = 'manage.customer'

    name = fields.Char(string='Name')
    description = fields.Char()
    projects = fields.One2many('manage.project', 'customer_id', string='Projects')  

