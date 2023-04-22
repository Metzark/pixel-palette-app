import pyairtable

def validate_user(username, password):
    users_table = pyairtable.Table("patRuyd0UEreJE4zl.5d2124590b0573216122165bfcc7842b8cb96a3f6bc8627c313b064845e76f19",'app7aUreGEskRcjOb', 'Users')
    user_records = users_table.all(view='Grid view')
    for user in user_records:
        if(user["fields"]["Username"] == username and user["fields"]['Password'] == password):
            return True
    return False

def upload_creation(path, user):
    pass
    # creations_table = pyairtable.Table("patRuyd0UEreJE4zl.5d2124590b0573216122165bfcc7842b8cb96a3f6bc8627c313b064845e76f19",'app7aUreGEskRcjOb', 'Creations')
    # name = path[path.rindex('/') + 1:-4]
    # file = open(path, 'r')
    # contents = file.readlines()
    # file.close()
    # creations_table.create({'Name': name, 'Author': user, 'File': [{
    #     'id': name,
    #     'url': 'www.asdfefd.com' 
    # }]})