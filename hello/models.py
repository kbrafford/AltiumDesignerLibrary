from sqlalchemy import *
from hello import db
HIDDEN_FIELDS = ('uuid', 'id')
# Models are auto-generated, because our database schema is really stupid-simple
meta = db.Model.metadata
meta.reflect(db.engine)

class Resistor(db.Model):
    __table__ = meta.tables['resistor']
    properties = meta.tables['resistor'].c.keys()

class Capacitor(db.Model):
    __table__ = meta.tables['capacitor']
    properties = meta.tables['capacitor'].c.keys()

class Inductor(db.Model):
    __table__ = meta.tables['inductor']
    properties = meta.tables['inductor'].c.keys()

class Diode(db.Model):
    __table__ = meta.tables['diode']
    properties = meta.tables['diode'].c.keys()

components = {'resistor':Resistor, 'capacitor':Capacitor, 'inductor':Inductor, 'diode':Diode}
