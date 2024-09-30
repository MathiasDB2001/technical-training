from odoo import fields, models

class EstateProperty(models.Model):
    _name = "Estate Property"
    _description = "description"

    name = fields.Char(required=True)
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float(required=True)
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='garden orientation',
        selection=[('north', 'North'), ('east', 'East'), ('south', 'South'), ('West', 'West')]
    )

