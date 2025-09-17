from odoo import _, fields, models

class PersonalFinancesTag(models.Model):
    _name = "personal.finances.tag"
    _description = "Personal Finances Tag"

    name = fields.Char(string=_("Name"), required=True)
    color = fields.Integer(string=_("Color"))
    type = fields.Selection([
        ('income', _('Income')),
        ('expense', _('Expense'))
    ], string=_('Type'), required=True, default='expense')
