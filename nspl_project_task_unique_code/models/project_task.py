from odoo import api, fields, models


class ProjectTask(models.Model):
    """ Inherits project.task """
    _inherit = 'project.task'

    unique_code = fields.Char(string='Unique Code', readonly=True)
    _sql_constraints = [
        ('unique_code', 'unique(unique_code, company_id)',
         'Code must be unique per company!'),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        """ Extends the create method to generate the unique code """
        for vals in vals_list:
            project = self.env['project.project'].browse(vals.get('project_id'))
            if project.sequence_id:
                vals['unique_code'] = project.sequence_id.next_by_id()
        return super().create(vals_list)
