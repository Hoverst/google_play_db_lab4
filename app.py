"""Entry point for the Flask application."""
from my_project import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
