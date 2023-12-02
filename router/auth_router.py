import model
from sqlalchemy.orm import Session
from flask import request, make_response
from server import app
from server import engine
import jwt 

@app.after_request
def addCors(response):
    allowed_origins = ['https://remplasveltenew.fly.dev']
    origin = request.headers.get('Origin')
    
    if origin in allowed_origins:
        response.headers['Access-Control-Allow-Origin'] = origin

    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
    response.headers['Access-Control-Allow-Credentials'] = 'true'  # Enable if you're using credentials (cookies, HTTP authentication)

    return response

@app.route('/')
def index():
    return 'HELLO THERE '

'''
@app.route('/auth', methods=['POST'])
def auth():
    data = request.get_json()
    email = data.get('email')
    # func to query password for email 
    token = jwt.encode({"email": email}, "secret", algorithm="HS256" )
    if data.get('password') == 'password':
        res = make_response('authenticated')
    else :
        res = make_response('not_authenticated')
        res.headers['Authorization'] = 'Bearer ' + token
    return res 
'''


@app.route('/auth/create', methods=['POST'])
def createUser():
    try : 
        newuser = extract_user_json(request)
        with Session(engine) as session:
            session.add(newuser)
            session.commit()
            return newuser.to_dict()
    except Exception as e: 
        print(e)

@app.route('/auth/log', methods=['POST'])
def authlog():
    return "hello"
    

def extract_user_json(request):
    data = request.get_json()
    newuser = model.User(
       email=data.get('email'), 
       password=data.get('password'))
    return newuser