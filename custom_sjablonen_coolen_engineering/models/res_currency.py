from odoo import models
from odoo.tools.misc import formatLang, get_lang, format_amount


class ResCurrency(models.Model):
    _inherit = "res.currency"

    def format_amout(self, amount):
        self.ensure_one()
        return format_amount(self.env, amount, self)
