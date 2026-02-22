def greet(username : str) -> None:
    """A simple function to greet a person."""
    print(f"Hello, {username}!")


greet("Alice")

#keyword arguments

def describe_pet(animal_type : str, pet_name : str) -> None:
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")



describe_pet(animal_type="hamster", pet_name="Harry")
#describe_pet("Willie", "dog") # ordering the arguments is important when not using keyword arguments
describe_pet(pet_name="Willie", animal_type="dog")


#optional parameters with return type
def get_formatted_name(first_name : str, last_name : str, middle_name : str = "") -> str:
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()



musician = get_formatted_name("jimi", "hendrix")
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


# functions with list arguments - the list are mutable objects, so they can be modified within the function
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

def print_models(unprinted_designs : list, completed_models : list) -> None:
    """Simulate printing each design, until none are left. Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models : list) -> None:
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_designs[:], completed_models) # In order to avoid modifying the original list, we can pass a copy of the list using slicing [:]
print(unprinted_designs)
show_completed_models(completed_models)


# passing arbitrary number of arguments
def make_pizza(*toppings) -> None:
    """Print the list of toppings that have been requested."""
    
    if isinstance(toppings, tuple):
        print('Processing toppings as a tuple')
    
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#using arbitrary keyword arguments
def build_profile(first : str, last : str, **user_info) -> dict:
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
