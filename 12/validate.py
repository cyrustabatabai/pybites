from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here


class UserDoesNotExist(Exception):
    pass


class UserAccessExpired(Exception):
    pass

class UserNoPermission(Exception):
    pass

def get_secret_token(username):


    if username not in [user.name for user in USERS]:
        raise UserDoesNotExist

    
    
    user = [user for user in USERS if user.name == username][0]
    if user.expired:
        raise UserAccessExpired
    


    if user.role != ADMIN:
        raise UserNoPermission



    return SECRET


