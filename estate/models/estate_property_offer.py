from odoo import fields, models

class PropertyOffer(models.Model):
    _name='estate.property.tag'
    _description = 'Estate Property Tag'

    price = fields.Float()
    state = fields.Selection(
        string="state",
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')]
    )
    partner_id = fields.Many2one('res_partner')
    property_id = fields.Many2one('estate_property')
