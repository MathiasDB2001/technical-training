from odoo import fields, models

class PropertyTag(models.Model):
    _name='estate.property.Tag'
    _description = 'Estate Property Tag'

    name = fields.Char(string='Property Tag')
    