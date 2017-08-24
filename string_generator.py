import random, string

# r = int(input('Enter your range: '))

# pw = string.ascii_letters + string.digits + string.punctuation
# random = ''.join(random.sample(pw, r))
value = ''.join(random.sample(string.ascii_letters + string.digits, 32))

print("Your generated string is: %s" % value)
