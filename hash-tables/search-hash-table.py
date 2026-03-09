my_list = [None, None, None, None, None, None, None, None, None, None]

def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)

  return sum_of_chars % 10

def add(name):
    index = hash_function(name)
    my_list[index] = name

add('Pete')
add('Bob')
add('Jones')
add('Lisa')
add('Siri')

def contains(name):
    index = hash_function(name)
    return my_list[index] == name

print("Pete is in the hash table", contains('Pete'))