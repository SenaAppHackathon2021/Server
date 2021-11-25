from flask import session

def check_login():
    try:
        with session['user_id']:
            pass
    except:
        return "You need login", 401