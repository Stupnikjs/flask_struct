import model
from sqlalchemy.orm import Session 
from flask import request
from server import app
from server import engine



@app.route('/')
def index():
    return 'HELLO THERE '

@app.route('/get/all') 
def fetchallrempla():
    with Session(engine) as session:
        result = session.query(model.Rempla).all()
        response = []
        for res in result: 
            response.append(res.to_dict())
        return response

@app.route('/add/one', methods=['POST']) 
def add_rempla_():
    try:
    # Assuming the request data is JSON
        newrempla = extractJson(request)
        with Session(engine) as session:
            session.add(newrempla)
            session.commit()
            return "done"
    except : 
        return "error"
    

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
        retrocession=data.get('retrocession'), 
        location=data.get('location'), 
        minutes_from_home=data.get('minutes_from_home'))
    return newrempla

