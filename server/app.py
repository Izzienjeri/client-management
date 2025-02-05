from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Migrate
from config import Config
from models import db
import routes  # Import routes

# Initialize app, database, and migration tools
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)  # Initialize Migrate with the app and db

with app.app_context():
    db.create_all()  # Ensure tables are created initially, this will be handled by migrations after setup

if __name__ == "__main__":
    app.run(debug=True)
