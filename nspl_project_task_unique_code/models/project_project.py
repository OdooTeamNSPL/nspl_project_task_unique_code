from odoo import api, fields, models


class Project(models.Model):
    _inherit = 'project.project'

    project_short_code = fields.Char(
        string='Short Code', required=True)
    sequence_id = fields.Many2one(
        'ir.sequence', 'Reference Sequence', check_company=True, copy=False)

    _sql_constraints = [
        ('project_code_uniq', 'unique(project_short_code, company_id)',
         'The project code must be unique per company!'),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'sequence_id' not in vals or not vals['sequence_id']:
                vals['sequence_id'] = self.env['ir.sequence'].sudo().create({
                    'name': vals['name'] + ' Project Sequence',
                    'prefix': vals['project_short_code'] + '-', 'padding': 3,
                    'company_id': vals.get('company_id') or self.env.company.id,
                }).id
        return super().create(vals_list)
