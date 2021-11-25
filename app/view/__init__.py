from flask import session

def check_login():
    try:
        print(session['user_id'])
    except:
        return False