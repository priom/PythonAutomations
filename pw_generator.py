import random, string

n = 32

value = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, n))

print("Your generated password is: %s" % value)
