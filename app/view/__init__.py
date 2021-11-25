from flask import session

def check_login():
    try:
        with session['user']:
            pass
    except:
        return False