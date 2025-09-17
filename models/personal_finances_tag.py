from odoo import fields, models

class PersonalFinancesTag(models.Model):
    _name = "personal.finances.tag"
    _description = "Personal Finances Tag"

    name = fields.Char(string="Name", required=True)
    color = fields.Integer(string="Color")
    type = fields.Selection([
        ('income', 'Income'),
        ('expense', 'Expense')
    ], string='Type', required=True, default='expense')
