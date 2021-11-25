mail_pw = 'reart1234'
secret_key = 'reart'

db = {
    'user'     : 'root',
    'password' : 'moon',
    'host'     : '127.0.0.1',
    'port'     : '3306',
    'database' : 'reartdb'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"