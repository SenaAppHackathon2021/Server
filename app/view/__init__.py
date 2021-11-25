from flask import session

def check_login():
    if session['user'] == None:
        return False