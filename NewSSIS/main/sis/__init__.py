from flask import Flask
from flaskext.mysql import MySQL

application = Flask(__name__)

my_sql = MySQL()
application.config["SECRET_KEY"] = "12345"
application.config["MYSQL_DATABASE_HOST"] = "localhost"
application.config["MYSQL_DATABASE_USER"] = "root"
application.config["MYSQL_DATABASE_PASSWORD"] = ""
application.config["MYSQL_DATABASE_DB"] = "flask"

my_sql.init_app(application)

from sis import routes
