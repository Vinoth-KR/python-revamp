from pathlib import Path

# basic read text
print(Path(__file__).parent)
path = Path(__file__).parent / 'pi_digits.txt'
#path = Path('pi_digits.txt')
contents = path.read_text().strip()
print(contents)


# Using file contents by lines
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


# With Context manager

with path.open() as file_object:
    contents = file_object.read().rstrip()
    print(contents)


    # writing to a file
    file_path = Path(__file__).parent / 'programming.txt'

    contents = 'I love programming.\n'
    contents += 'I love creating new games.\n'


    file_path.write_text(contents)