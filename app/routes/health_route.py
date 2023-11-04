# This is a health check route file.
from . import bp
from app.service.health_check_service import HealthCheck

@bp.route("/healthCheck")
def health_check_route():
    return HealthCheck.health_check()
