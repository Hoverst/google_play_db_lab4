from flask import jsonify
from sqlalchemy.exc import IntegrityError


def register_error_handlers(app):

    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({"error": str(e.description) if hasattr(e, "description") else "Bad request"}), 400

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": str(e.description) if hasattr(e, "description") else "Not found"}), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        return jsonify({"error": "Method not allowed"}), 405

    @app.errorhandler(409)
    def conflict(e):
        return jsonify({"error": str(e.description) if hasattr(e, "description") else "Conflict"}), 409

    @app.errorhandler(422)
    def unprocessable_entity(e):
        return jsonify({"error": str(e.description) if hasattr(e, "description") else "Unprocessable entity"}), 422

    @app.errorhandler(IntegrityError)
    def handle_integrity_error(e):
        from my_project import db
        db.session.rollback()
        return jsonify({"error": "Conflict: integrity constraint violated"}), 409

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({"error": "Internal server error"}), 500
