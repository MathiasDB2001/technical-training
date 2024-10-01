from odoo import fields, models
from dateutil import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "description"

    name = fields.Char(string='Title',required=True)
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'), ('offer_received', 'Offer Received'), 
                  ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        default='new'
    )
    description = fields.Text()
    last_seen = fields.Datetime('last seen', default=fields.Datetime.now())
    postcode = fields.Char()
    date_availability = fields.Date(default=fields.Date.today()+relativedelta.relativedelta(months=3))
    expected_price = fields.Float()
    selling_price = fields.Float(required=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='garden orientation',
        selection=[('north', 'North'), ('east', 'East'), ('south', 'South'), ('West', 'West')]
    )
    property_type_id = fields.Many2one("estate.property.type")
    salesperson_id = fields.Many2one("res.users", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", copy=False)
    tag_ids = fields.Many2many("estate.property.tag")
    #offer_ids = fields.One2Many("estate.property.offer", "property_id")


