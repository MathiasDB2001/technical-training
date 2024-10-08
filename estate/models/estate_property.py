from odoo import fields, models,api,_
from dateutil import relativedelta
from odoo.exceptions import ValidationError
from odoo.tools.float_utils import float_is_zero, float_compare

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "description"

    name = fields.Char(string='Title',required=True)
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'), ('offer_received', 'Offer Received'), 
                  ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],
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
    total_area = fields.Integer(compute="_compute_total_area")
    best_price = fields.Float(compute="_compute_best_price")
    garden_orientation = fields.Selection(
        string='garden orientation',
        selection=[('north', 'North'), ('east', 'East'), ('south', 'South'), ('West', 'West')]
    )
    property_type_id = fields.Many2one("estate.property.type")
    salesperson_id = fields.Many2one("res.users", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", copy=False)
    tag_ids = fields.Many2many("estate.property.tag")
    offer_ids = fields.One2many("estate.property.offer", "property_id")


    _sql_constraints=[
        ("check_selling_price", "CHECK(selling_price >= 0)", "The selling price must be positive"),
        ("check_expected_price", "CHECK(expected_price >= 0)", "The expected price must be positive")
    ]   



    @api.depends("garden_area", "living_area")
    def _compute_total_area(self):
        for property in self:
            property.total_area = property.garden_area + property.living_area



    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for property in self:
            if property.offer_ids:
                property.best_price = max(property.offer_ids.mapped("price"))
            else:
                property.best_price = 0
    

    @api.onchange("garden")
    def _onchage_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = self.garden_orientation = False


    def action_sell_property(self):
        for property in self:
            if property.state == "canceled":
                raise UserError(_("Canceled properties cannot be sold"))
            property.state = "sold"


    def action_cancel_property(self):
        self.state = "canceled"


    @api.constrains("selling_price", "expected_price")
    def _check_selling_price(self):
        for property in self:
            if (not float_is_zero(property.selling_price, precision_rounding=0.1) and
                float_compare(property.selling_price, 0.9 * property.expected_price, precision_rounding=0.01) < 0):
                raise ValidationError(_('The selling price should not be lower than 90% of the expected price'))

