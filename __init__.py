import sys
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS
from service.common import log_handlers

app = Flask(__name__)
app.config.from_object("service.config")

# Initialize Security Headers with Talisman
talisman = Talisman(app)

# Initialize CORS policies
CORS(app)

from service import routes, models  # noqa: F401, E402
from service.common import error_handlers, cli_commands  # noqa: F401, E402

# Set up logging
log_handlers.init_app(app)

app.logger.info(70 * "*")
app.logger.info("  A C C O U N T   S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")