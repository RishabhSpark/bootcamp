import logging

logger = logging.getLogger(__name__)

def health_check():
    try:
        # Simulate a health check
        status = "System is healthy"
        logger.info(status)
        return status
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return "System is unhealthy"

print(health_check())
