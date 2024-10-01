from odoo import fields, models

class PropertyTag(models.Model):
    _name='estate.property.tag'
    _description = 'Estate Property Tag'

    name = fields.Char(string='Property Tag')

    _sql_constraints = [
        ("unique_name", "UNIQUE(name)", "Tag name should be unique.")
    ]
