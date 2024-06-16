my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

keys_to_check = ['age', 'country']

key_existence = [key in my_dict for key in keys_to_check]

print("Existence of keys in the dictionary:", key_existence)
