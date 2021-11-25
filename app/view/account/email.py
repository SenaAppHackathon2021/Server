from flask import request, jsonify, session
from flask_restful import Resource
from random import *
from flask_mail import Mail, Message
from app.extexsion import mail

class Email(Resource):
    def post(self):
        email = request.json['email']
        email_code = randint(100000, 999999)
        print(email_code)
        session.pop('code', None)
        #session['code'] = False
        session.clear()
        session['email'] = email
        session['code'] = email_code
        print(session['code'])
        session
        title = 'Mungshil Cloud Email Verification Code: {}'.format(email_code)
    
        msg = Message(title, sender='reart.senaapp@gmail.com', recipients=[email])
        mail.send(msg) 
        #print("----------EMAIL-----------")
        return jsonify({"message" : "send verification code success", "status_code" : "200"})


class CheckEmail(Resource):
    def post(self):
        auth_code = request.json['auth_code']
        check_code = session.get('code')
        if check_code == check_code:
            return jsonify({"message" : "send verification code success", "status_code" : "200"})
        else:
            return jsonify({{"message" : "send verification code fail", "status_code" : "400"}})
