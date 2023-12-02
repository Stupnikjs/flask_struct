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



@app.route('/api/all/') 
def fetchallrempla():
    with Session(engine) as session:
        result = session.query(model.Rempla).all()
        response = []
        for res in result: 
            response.append(res.to_dict())
        return response

@app.route('/api/new', methods=['POST']) 
def add_rempla_():
    try:
    # Assuming the request data is JSON
        newrempla = extract_rempla_json(request)
        with Session(engine) as session:
            session.add(newrempla)
            session.commit()
            return "done"
    except Exception as e:
        # Print the exception details
        return f"SQLAlchemyError: {e}"
        
    

@app.route('/api/del/<id>')
def deleteOne(id):
    with Session(engine) as session:
        item = session.query(model.Rempla).get(id)
        session.delete(item)
        session.commit()
        return "done"

@app.route('/get/one/<int:id>')
def getOne(id):
    print(id)
    with Session(engine) as session:
        item = session.query(model.Rempla).get(id)
        return item.to_dict()






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
    

def extract_rempla_json(request):
    data = request.get_json()
    newrempla = model.Rempla(
        debut=data.get('debut'), 
        fin=data.get('fin'), 
        location=data.get('location'),
        retrocession=data.get('retrocession'), 
        logiciel=data.get('logiciel'),
        minutes_from_home=data.get('minutes_from_home'))
    return newrempla

def extract_user_json(request):
    data = request.get_json()
    newuser = model.User(
       email=data.get('email'), 
       password=data.get('password'))
    return newuser