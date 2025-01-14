
{
    'name': 'Mi Módulo de Prueba',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Un módulo de prueba básico para Odoo',
    'description': """
    Este es un módulo de prueba que crea un modelo básico con un campo de texto.
    """,
    'author': 'Tu Nombre',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/mi_prueba_views.xml',
    ],
    'installable': True,
    'application': False,
}
