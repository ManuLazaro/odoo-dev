# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class sprint(models.Model):
     _name = 'manage.sprint'
     _description = 'manage.sprint'

     name = fields.Char()
     description = fields.Char()
     duration = fields.Integer()
     start_date = fields.Datetime()
     end_date = fields.Datetime(compute="_get_end_date")
     tasks_ids = fields.One2many('manage.task', 'sprint_id', string='tasks')
     project_id = fields.Many2one('manage.project', string='project')
     #sprint = fields.Many2one("manage.sprint", compute = "_get_sprint", store=True)

     @api.depends("start_date", "duration")
     def _get_end_date(self):
        for sprint in self:
            if isinstance(sprint.start_date, datetime.datetime) and sprint.duration > 0:
                sprint.end_date = sprint.start_date + datetime.timedelta(days=sprint.duration)
            else:
                sprint.end_date = sprint.start_date   

    