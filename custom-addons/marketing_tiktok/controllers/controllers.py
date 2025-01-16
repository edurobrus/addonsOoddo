# -*- coding: utf-8 -*-
# from odoo import http


# class MarketingTiktok(http.Controller):
#     @http.route('/marketing_tiktok/marketing_tiktok', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/marketing_tiktok/marketing_tiktok/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('marketing_tiktok.listing', {
#             'root': '/marketing_tiktok/marketing_tiktok',
#             'objects': http.request.env['marketing_tiktok.marketing_tiktok'].search([]),
#         })

#     @http.route('/marketing_tiktok/marketing_tiktok/objects/<model("marketing_tiktok.marketing_tiktok"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('marketing_tiktok.object', {
#             'object': obj
#         })

