{
    'name': 'My Vue.js Module',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Integrates Vue.js into Odoo',
    'description': 'This module integrates a Vue.js application into Odoo.',
    'depends': ['base'],
    'data': [
        'views/vue_app_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'my_module/static/src/js/vue_app.js',
            'my_module/static/src/css/vue_app.css',
        ],
    },
    'installable': True,
    'auto_install': False,
}
