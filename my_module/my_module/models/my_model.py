# models/my_model.py
from odoo import models, fields

class MyModel(models.Model):
    _name = 'my.model'
    name = fields.Char('Name')
