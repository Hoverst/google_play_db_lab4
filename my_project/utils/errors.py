from flask import jsonify
from sqlalchemy.exc import IntegrityError

def register_error_handlers(app):

    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({"error": str(e.description) if hasattr(e, 'description') else "Bad request"}), 400

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": str(e.description) if hasattr(e, 'description') else "Not found"}), 404

    @app.errorhandler(409)
    def conflict(e):
        return jsonify({"error": str(e.description) if hasattr(e, 'description') else "Conflict"}), 409

    @app.errorhandler(IntegrityError)
    def handle_integrity_error(e):
        from my_project import db
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({"error": "Internal server error"}), 500
