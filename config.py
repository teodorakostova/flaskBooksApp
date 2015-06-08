import os

basedir = os.path.abspath(os.path.dirname(__file__))
# activates the cross-site request forgery prevention, makes app more secure
WTF_CSRF_ENABLED = True
# used to create a cryptographic token that is used to validate a form
SECRET_KEY = 'asd'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')