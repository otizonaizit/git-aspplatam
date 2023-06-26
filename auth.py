def get_credentials():
    user = input('Type user name: ')
    password = input('Type password: ')
    return user, password

#def write_pwdb():

#def read_pwdb():

def add_user(user, password, pwdb):
    if user not in pwdb:
        pwdb[user] = password
    return pwdb


if __name__ == '__main__':
    get_credentials()

