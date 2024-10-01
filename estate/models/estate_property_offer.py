from odoo import fields, models

class PropertyOffer(models.Model):
    _name='estate.property.offer'
    _description = 'Estate Property Offer'

    price = fields.Float()
    state = fields.Selection(
        string="state",
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')]
    )
    partner_id = fields.Many2one('res.partner')
    property_id = fields.Many2one('estate.property')
