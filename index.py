import connexion
from controllers.users import get

def setup_app():
    app = connexion.FlaskApp(
        'learning_openapi',
        host='0.0.0.0',
        port=10080,
        specification_dir='./build',
        debug=True,
    )
    app.add_api(
        'openapi.yml',
        validate_responses=True,
    )
    return app


if __name__ == '__main__':
    app = setup_app()
    app.run()
