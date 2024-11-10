## utils.py
import json
import logging
from jsonschema import validate, ValidationError

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path: str) -> dict:
    """
    Load data from a given file path.

    Args:
        file_path (str): The path to the file containing the data.

    Returns:
        dict: The data loaded from the file, expected to be in JSON format.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return {}
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from file: {file_path}")
        return {}

def parse_parameters(params: str) -> dict:
    """
    Parse a string of parameters into a dictionary.

    Args:
        params (str): Parameters in string format, expected to be JSON.

    Returns:
        dict: The parameters parsed into a dictionary.
    """
    if not params:
        logging.error("Empty parameters string.")
        return {}
    try:
        parameters = json.loads(params)
        return parameters
    except json.JSONDecodeError:
        logging.error("Error decoding JSON from parameters string.")
        return {}

def validate_data(data: dict, schema: dict) -> bool:
    """
    Validates the loaded data against a predefined schema.

    Args:
        data (dict): The data to validate.
        schema (dict): The schema to validate against.

    Returns:
        bool: True if data matches the schema, False otherwise.
    """
    try:
        validate(instance=data, schema=schema)
        return True
    except ValidationError as e:
        logging.error(f"Validation error: {e}")
        return False
