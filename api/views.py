from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timezone
import requests, logging
from decouple import config

# Setup logging
logger = logging.getLogger(__name__)

@api_view(['GET'])
def me(request):
    """
    GET /api/me/
    Returns user profile info and a random cat fact.

    - Uses environment variables for configuration
    - Handles API/network errors gracefully
    - Logs issues for debugging
    """

    api_url = config('CATFACT_API_URL', default='https://catfact.ninja/fact')
    timeout = config('API_TIMEOUT', default=5, cast=int)

    try:
        res = requests.get(api_url, timeout=timeout)
        res.raise_for_status()
        cat_fact = res.json().get("fact", "No cat fact available.")
    except requests.Timeout:
        logger.warning("Cat fact API request timed out.")
        cat_fact = "Timeout: Cat fact service is slow. Try again later."
    except requests.RequestException as e:
        logger.error(f"Cat fact API error: {e}")
        cat_fact = "Could not fetch a cat fact at the moment."

    data = {
        "status": "success",
        "user": {
            "email": "akpannath@yahoo.com",
            "name": "Joseph Akpan",
            "stack": "Python/Django"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return Response(data)
