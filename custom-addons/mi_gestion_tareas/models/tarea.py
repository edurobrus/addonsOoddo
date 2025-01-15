from odoo import models, fields

class Tarea(models.Model):
    _name = 'mi_gestion_tareas.tarea'
    _description = 'Modelo para gestionar tareas'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    state = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada')
    ], string='Estado', default='pendiente')
