from odoo import fields, models

class PropertyType(models.Model):
    _name='estate.property.type'
    _description = 'Estate Property Type'

    name = fields.Char(string='Property Type')
    property_ids = fields.One2many('estate.property', 'property_type_id')


    _sql_constraints = [
        ("unique_name", "UNIQUE(name)", "Type name should be unique.")
    ]