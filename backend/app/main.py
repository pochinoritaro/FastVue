import data

data.create_db()
#data.set_user('testUser1', 'TestUser1')

for i in range(50000):
    name = ('testUser' + str(i))
    pswd = ('TestUser' + str(i))
    data.set_user(name, pswd)
