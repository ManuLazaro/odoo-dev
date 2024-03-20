# -*- coding: utf-8 -*-

from odoo import models, fields, api


class history(models.Model):
    _name = 'manage.history'
    _description = 'manage.history'

    name = fields.Char()
    description = fields.Char()
    project_id = fields.Many2one('manage.project', string='project')
    tasks_ids = fields.One2many('manage.task', 'history_id', string='task')
    used_technologies = fields.Many2many('manage.technology', compute="_get_used_technologies")

    def _get_used_technologies(self):
        for history in self:
            technologies = None
            for task in history.tasks_ids:
                if not technologies:
                    technologies = task.technologies
                else:
                    technologies = technologies + task.technologies
            history.used_technologies = technologies
            