import model
from sqlalchemy.orm import Session
from flask import request, make_response
from server import app
from server import engine




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


@app.route('/api/create', methods=['POST']) 
def add_remplas_():
    try:
    # Assuming the request data is JSON
        newremplas = extract_remplas_json(request)
        with Session(engine) as session:
            for rempla in newremplas:
                session.add(rempla)
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


def extract_rempla_json(request):
    data = request.get_json()
    newrempla = model.Rempla(
        debut=data.get('debut'), 
        fin=data.get('fin'), 
        location=data.get('location'),
        retrocession=data.get('retrocession'), 
        logiciel=data.get('logiciel'),
        minutes_from_home=data.get('minutes_from_home'),
        color=data.get('color'))
    return newrempla

def extract_remplas_json(request):
    data = request.get_json()
    remplas = []
    for rempla in data: 
        newrempla = model.Rempla(
            debut=rempla.get('debut'), 
            fin=rempla.get('fin'), 
            location=rempla.get('location'),
            retrocession=rempla.get('retrocession'), 
            logiciel=rempla.get('logiciel'),
            minutes_from_home=rempla.get('minutes_from_home'),
            color=rempla.get('color'))
        remplas.append(newrempla)
    return remplas
