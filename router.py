import model
from sqlalchemy.orm import Session
from flask import request, make_response
from server import app
from server import engine
import jwt 


@app.route('/')
def index():
    return 'HELLO THERE '

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
        newrempla = extractJson(request)
        with Session(engine) as session:
            session.add(newrempla)
            session.commit()
            return "done"
    except Exception as e:
        # Print the exception details
        return f"SQLAlchemyError: {e}"
        
    

@app.route('/del/one/<int:id>')
def deleteOne(id):
    print(id)
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



def extractJson(request):
    data = request.get_json()
    newrempla = model.Rempla(
        debut=data.get('debut'), 
        fin=data.get('fin'), 
        location=data.get('location'),
        retrocession=data.get('retrocession'), 
        logiciel=data.get('logiciel'),
        minutes_from_home=data.get('minutes_from_home'))
    return newrempla

