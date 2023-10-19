import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

pass_length = 12

random_password = generate_password(pass_length)
print("Random Password:", random_password)
