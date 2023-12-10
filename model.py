from sqlalchemy import String,Integer, Column
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

class Base(DeclarativeBase):
    pass


class Rempla(Base):
    __tablename__='remplas'

    id = Column(Integer,primary_key=True)
    debut = Column(String(30))
    fin = Column(String(30))
    logiciel=Column(String(30))
    retrocession = Column(Integer)
    location = Column(String(30))
    minutes_from_home = Column(Integer)
    color=Column(String(30))

    def to_dict(self):
        return {
            'id': self.id,
            'debut': self.debut,
            'fin': self.fin,
            'logiciel': self.logiciel,
            'retrocession': self.retrocession,
            'location': self.location,
            'minutes_from_home': self.minutes_from_home, 
            'color': self.color
        }

    def __str__(self):
        return self.to_dict()
    

class User(Base):
    __tablename__='users'
    id = Column(Integer,primary_key=True)
    email = Column(String(30))
    password = Column(String(30)) 

    def __init__(self, email, password): 
        self.email = email
        self.password = password
    
    def __str__(self):
        return self.to_dict()
    
    
    def to_dict(self):
        return {
            'email':self.email, 
            'password': self.password

        }
