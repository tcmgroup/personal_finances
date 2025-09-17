from odoo import api, fields, models

class PersonalFinancesTransaction(models.Model):
    _name = "personal.finances.transaction"
    _description = "Personal Finances Transaction"
    _inherit = ['mail.thread', 'mail.activity.mixin'] # Add chatter

    name = fields.Char(string="Description", required=True, tracking=True)
    date = fields.Date(string="Date", required=True, default=fields.Date.context_today, tracking=True)
    amount = fields.Monetary(string="Amount", required=True, tracking=True)
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    type = fields.Selection([
        ('income', 'Income'),
        ('expense', 'Expense')
    ], string='Type', required=True, default='expense', tracking=True)
    tag_ids = fields.Many2many('personal.finances.tag', string="Tags")
    note = fields.Text(string="Note")
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user, required=True, readonly=True, copy=False, tracking=True)
    amount_absolute = fields.Monetary(string="Absolute Amount", compute='_compute_amount_absolute', store=True, help="Absolute value of the amount, used for graphing.")

    @api.depends('amount')
    def _compute_amount_absolute(self):
        for record in self:
            record.amount_absolute = abs(record.amount)

    @api.model
    def create(self, vals):
        """Ensure expense amount is stored as a negative value."""
        if vals.get('type') == 'expense' and vals.get('amount', 0) > 0:
            vals['amount'] = -vals['amount']
        elif vals.get('type') == 'income' and vals.get('amount', 0) < 0:
            vals['amount'] = abs(vals['amount'])
        return super(PersonalFinancesTransaction, self).create(vals)

    def write(self, vals):
        """Ensure expense amount is stored as a negative value, handling type changes."""
        # To handle batch updates and type changes correctly, we check the target state.
        # This simplified logic works best for UI operations (typically one record at a time).
        if 'amount' in vals or 'type' in vals:
            # Make a copy to modify, preserving the original for the super call if needed.
            vals_copy = vals.copy()
            # Determine the final type and amount after the write.
            final_type = vals_copy.get('type', self[0].type)
            final_amount = vals_copy.get('amount', self[0].amount)

            # If the user is not changing the amount but IS changing the type, we must flip the sign.
            if 'amount' not in vals_copy and 'type' in vals_copy:
                if final_type == 'expense' and final_amount > 0:
                    vals_copy['amount'] = -final_amount
                elif final_type == 'income' and final_amount < 0:
                    vals_copy['amount'] = abs(final_amount)
            # If the user IS changing the amount, ensure it has the correct sign.
            elif 'amount' in vals_copy:
                if final_type == 'expense' and vals_copy['amount'] > 0:
                    vals_copy['amount'] = -vals_copy['amount']
                elif final_type == 'income' and vals_copy['amount'] < 0:
                    vals_copy['amount'] = abs(vals_copy['amount'])
            
            return super(PersonalFinancesTransaction, self).write(vals_copy)

        return super(PersonalFinancesTransaction, self).write(vals)
