# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True
}

user2 = {
    'name': 'iliana',
    'valid': False
}

def authenticated(fn):
    def wrapper(*args):
        if args[0]['valid']:
            return fn(*args)
        else:
            print('user is invalid')
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
message_friends(user2)