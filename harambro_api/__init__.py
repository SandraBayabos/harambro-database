from harambro_api.blueprints.users.views import users_api_blueprint
from harambro_api.blueprints.sessions.views import sessions_api_blueprint
from harambro_api.blueprints.history.views import history_api_blueprint
from app import app, csrf
from flask_cors import CORS


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##


app.register_blueprint(csrf.exempt(
    users_api_blueprint), url_prefix='/api/v1/users')
app.register_blueprint(csrf.exempt(
    sessions_api_blueprint), url_prefix='/api/v1/sessions')
app.register_blueprint(csrf.exempt(history_api_blueprint),
                       url_prefix='/api/v1/history')
