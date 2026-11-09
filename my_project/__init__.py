"""Core application package. Creates and configures the Flask app."""
import os
import yaml
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Declare db at module level BEFORE create_app
db = SQLAlchemy()


def create_app():
    """Factory function that creates and configures the Flask application."""
    app = Flask(__name__)

    # Build absolute path to config/app.yml
    # Current file is my_project/__init__.py, go up one level to get project root
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    config_path = os.path.join(project_root, 'config', 'app.yml')

    # Read configuration from YAML
    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)

    db_cfg = config['db']

    # Build SQLAlchemy database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{db_cfg['user']}:{db_cfg['password']}"
        f"@{db_cfg['host']}:{db_cfg['port']}/{db_cfg['name']}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize SQLAlchemy with the app
    db.init_app(app)

    # Import and register blueprints INSIDE create_app to avoid circular imports
    from my_project.auth.route.accounts_route import accounts_bp
    from my_project.auth.route.devices_route import devices_bp
    from my_project.auth.route.accounts_devices_route import accounts_devices_bp
    from my_project.auth.route.companies_route import companies_bp
    from my_project.auth.route.apps_route import apps_bp
    from my_project.auth.route.categories_route import categories_bp
    from my_project.auth.route.apps_categories_route import apps_categories_bp
    from my_project.auth.route.installations_route import installations_bp
    from my_project.auth.route.apps_versions_route import apps_versions_bp
    from my_project.auth.route.apps_discounts_route import apps_discounts_bp
    from my_project.auth.route.reviews_route import reviews_bp
    from my_project.auth.route.payment_cards_route import payment_cards_bp
    from my_project.auth.route.bills_route import bills_bp
    from my_project.auth.route.library_route import library_bp

    app.register_blueprint(accounts_bp)
    app.register_blueprint(devices_bp)
    app.register_blueprint(accounts_devices_bp)
    app.register_blueprint(companies_bp)
    app.register_blueprint(apps_bp)
    app.register_blueprint(categories_bp)
    app.register_blueprint(apps_categories_bp)
    app.register_blueprint(installations_bp)
    app.register_blueprint(apps_versions_bp)
    app.register_blueprint(apps_discounts_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(payment_cards_bp)
    app.register_blueprint(bills_bp)
    app.register_blueprint(library_bp)

    # Register centralized error handlers
    from my_project.utils.errors import register_error_handlers
    register_error_handlers(app)

    return app
