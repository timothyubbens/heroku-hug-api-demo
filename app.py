#!/usr/bin/env python
"""A simple API to do almost nothing"""
import hug

@hug.local()
@hug.get('/users', versions=1)
def user(user_id):
    return 'I do nothing useful.'
    #return user_id

if __name__ == '__main__':
    user.interface.local()
