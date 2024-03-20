# -*- coding: utf-8 -*-


from odoo import models, fields, api
import datetime

class task(models.Model):
     _name = 'manage.task'
     _description = 'manage.task'

     code = fields.Char(compute="_get_code")
     name = fields.Char()
     description = fields.Char()
     start_date = fields.Datetime()
     end_date = fields.Datetime()
     is_paused = fields.Boolean()
     sprint_id = fields.Many2one('manage.sprint', string='Sprint')
     technology_ids = fields.Many2many('manage.technology', string='technologys')
     history_id = fields.Many2one('manage.history', string='history')
     sprint = fields.Many2one("manage.sprint", compute="_get_sprint", store=True)
     project = fields.Many2one('manage.project', related='history_id.project_id', readonly=True)
     definition_date = fields.Datetime(default=lambda p: datetime.datetime.now())
     
     
     
     def _get_code(self):
        for task in self:
            if len(task.sprint_id) == 0:
                task.code = "TSK_"+str(task.id)
            else:
                task.code = str(task.sprint_id.name).upper()+ "_"+str(task.id)
    
     @api.depends('code')
     def _get_sprint(self):
         for task in self:
             sprints = self.env['manage.sprint'].search([('project_id', '=', task.history_id.project_id.id)])
             found = False
             for sprint in sprints:
                 if isinstance(sprint.end_date, datetime.datetime) and sprint.end_date > datetime.datetime.now() :
                     task.sprint = sprint.id
                     found = True
                 if not found:
                     task.sprint = False