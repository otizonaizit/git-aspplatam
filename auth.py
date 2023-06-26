import json

def get_credentials():
    user = input('Type user name: ')
    password = input('Type password: ')
    return user, password

def write_pwdb(user, password):
    pwdb = {}
    pwdb[user] = password
    fn = 'database.json'
    with open(fn, 'w') as f:
        json.dump(pwdb, f)

#def read_pwdb():

def add_user(user, password, pwdb):
    if user not in pwdb:
        pwdb[user] = password
    return pwdb


if __name__ == '__main__':
    user, password = get_credentials()
    write_pwdb(user, password)
