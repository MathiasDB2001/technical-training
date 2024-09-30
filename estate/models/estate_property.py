from odoo import fields, models
from dateutil import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "description"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
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
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'), ('offer_received', 'Offer Received'), 
                  ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        default='new'
    )

