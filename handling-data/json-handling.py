# writing data to numbers
from pathlib import Path
import json

numbers = [2,3,5,7,11,13]

path = Path(__file__).parent / 'numbers.json'
path.write_text(json.dumps(numbers))