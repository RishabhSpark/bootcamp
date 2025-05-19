import requests
import time
from typing import List, Dict, Optional
from src.utils.logger import get_logger
from src.config.config_loader import load_config

config = load_config()
logger = get_logger(__name__, level=config.log_level, log_to_file=config.log_to_file, log_file_path=config.log_file_path)

PUBTATOR3_REQUEST_URL = "https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/RESTful/request.cgi"
PUBTATOR3_RETRIEVE_URL = "https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/RESTful/retrieve.cgi"

def extract_entities_pubtator3(text: str, bioconcept: Optional[str] = None) -> List[Dict[str, str]]:
    entities: List[Dict[str, str]] = []
    request_params = {'text': text}
    if bioconcept:
        request_params['bioconcept'] = bioconcept

    logger.debug(f"Submitting PubTator3 request for text: '{text}'")

    try:
        # Submit the text for annotation
        request_response = requests.post(PUBTATOR3_REQUEST_URL, data=request_params, timeout=10)
        request_response.raise_for_status()
        session_id = request_response.text.strip()
        logger.info(f"PubTator3 request submitted, session ID: {session_id}")

        # Poll for result
        max_attempts = 10
        wait_seconds = 5
        for attempt in range(max_attempts):
            retrieve_response = requests.post(PUBTATOR3_RETRIEVE_URL, data={'id': session_id}, timeout=10)

            logger.debug(f"PubTator3 retrieve attempt {attempt + 1}: status {retrieve_response.status_code}")

            if retrieve_response.status_code == 200:
                # Parse PubTator output format (tab-separated)
                for line in retrieve_response.text.strip().split('\n'):
                    parts = line.split('\t')
                    if len(parts) >= 5:
                        entity_text = parts[3]
                        entity_type = parts[4]
                        entities.append({'text': entity_text, 'type': entity_type})
                logger.info(f"Entities extracted successfully for session ID {session_id}")
                logger.debug(f"Extracted entities: {entities}")
                return entities

            elif retrieve_response.status_code == 404 and "Result is not ready" in retrieve_response.text:
                logger.warning(f"PubTator3 result not ready (attempt {attempt + 1}/{max_attempts}), retrying in {wait_seconds}s")
                time.sleep(wait_seconds)
            else:
                logger.error(f"Failed to retrieve PubTator3 result (attempt {attempt + 1}/{max_attempts}): "
                             f"{retrieve_response.status_code} - {retrieve_response.text}")
                return []

        logger.error(f"Max polling attempts reached for session ID {session_id} without result")
        return []

    except requests.RequestException as e:
        logger.error(f"Exception communicating with PubTator3 API: {e}", exc_info=True)
        return []