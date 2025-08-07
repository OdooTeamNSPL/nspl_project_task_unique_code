{
    'name': 'Project Task Unique Code',
    'version': '17.0',
    'summary': 'Auto-generated unique code for every project task.',
    'description': """
    This module automatically generates a unique code for each project task.

    ✔ Helps in tracking tasks easily  
    ✔ Ensures uniqueness of task references  
    ✔ Integrated within Odoo project management  
    """,
    'category': 'Project',
    'sequence': 10,
    'author': 'Namah Softech Private Limited',
    'website': 'http://www.namahsoftech.com',
    'license': 'LGPL-3',
    'support': 'support@namahsoftech.com',
    'price': 11.99,
    'currency': 'USD',
    'contributors': ['Shivani Solanki'],
    'license': 'AGPL-3',
    'depends': ['base', 'project'],
    'data': [
        'views/project_project_views.xml',
        'views/project_task_views.xml',
    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
