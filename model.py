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

    def to_dict(self):
        return {
            'id': self.id,
            'debut': self.debut,
            'fin': self.fin,
            'logiciel': self.logiciel,
            'retrocession': self.retrocession,
            'location': self.location,
            'minutes_from_home': self.minutes_from_home
        }

    def __str__(self):
        return self.to_dict()