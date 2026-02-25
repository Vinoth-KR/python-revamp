from pathlib import Path
import json

path = Path(__file__).parent / 'numbers.json'
contents = path.read_text()
numbers = json.loads(contents)
print(numbers)

print(type(numbers[0]))