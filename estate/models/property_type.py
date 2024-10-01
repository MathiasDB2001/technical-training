from odoo import fields, models

class PropertyType(models.Model):
    _name='estate.property.type'
    _description = 'Estate Property Type'

    name = fields.Char(string='Property Type')


    _sql_constraints = [
        ("unique_name", "UNIQUE(name)", "Type name should be unique.")
    ]