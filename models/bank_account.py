from odoo import _, fields, models

class BankAccount(models.Model):
    _name = "bank.account"
    _description = "Bank Account"

    name = fields.Char(string=_("Name"), required=True)
    reference = fields.Char(string=_("Reference"))
    user_id = fields.Many2one('res.users', string=_('User'), default=lambda self: self.env.user, required=True)