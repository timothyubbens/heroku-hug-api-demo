#!/usr/bin/env python
"""A simple API to do almost nothing"""
import hug

users = [
    {
        'uid': u'jsmith',
        'name': u'John Smith',
        'email': u'jsmith@example.com',
        'phone': u'123-456-7890'
    },
    {
        'uid': u'jdoe',
        'name': u'Jane Doe',
        'email': u'jdoe@example.com',
        'phone': u'234-567-8901'
    },
    {
        'uid': u'ssample',
        'name': u'Sally Sample',
        'email': u'ssample@example.com',
        'phone': u'345-678-9012'
    }
]

@hug.get('/users', versions=1)
def user(user_id):
    return 'I do nothing useful.'
    #return user_id

@hug.local()
@hug.get('/users', versions=2)
def user():
    return {'users': users}

if __name__ == '__main__':
    user.interface.local()
