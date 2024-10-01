from odoo import fields, models, api


class PropertyOffer(models.Model):
    _name='estate.property.offer'
    _description = 'Estate Property Offer'

    price = fields.Float()
    state = fields.Selection(
        string="state",
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')]
    )
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    validity = fields.Integer(default=7)
    partner_id = fields.Many2one('res.partner')
    property_id = fields.Many2one('estate.property')


    def action_accept_offer(self):
        self.state = "accepted"
        for offer in self:
            offer.property_id.selling_price = offer.price


    def action_refuse_offer(self):
        self.state = "refused"



    @api.depends("validity", "create_date")
    def _compute_date_deadline(self):
        for estate in self:
            create_date = estate.create_date or fields.Date.today()
            estate.date_deadline = fields.Date.add(create_date, days=estate.validity)


    def _inverse_date_deadline(self):
        for estate in self:
            estate.validity = (estate.date_deadline - fields.Date.to_date(estate.create_date)).days




