# Copyright (C) 2020 ID42 Sistemas (<http://id42.com.br>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': 'Document Page Portal',
    'version': '12.0.1.0.0',
    'category': 'Knowledge Management',
    'author': 'ID42 Sistemas, Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/knowledge',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'portal',
        'document_page'
    ],
    'data': [
        'security/document_page_portal_security.xml',
        'security/ir.model.access.csv',
        'views/document_page_portal_templates.xml',
    ],
}
