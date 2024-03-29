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
    names = [x.name for x in USERS]

    for x in USERS:
        if username not in names:
             raise UserDoesNotExist
        elif x.name == username:
              users_name, users_role, users_exspired = x
              break
         
         
    if users_exspired == True:
         raise UserAccessExpired
    elif users_role == USER:
         raise UserNoPermission
    elif users_role == ADMIN:
         return SECRET