def age(_age):
    if _age < 18:
        return 'You are so young'
    return 'Welcome'
def hello(name):
    return f'Hello, {name}'

def prime(digit):
    if all(digit % x != 0 for x in range(2, int(digit**0.5) + 1)):
        return 'YES'
    return 'NO'

