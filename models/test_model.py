from db import db

# create models for db tables here

class TestModel(db.Model):
    __tablename__ = 'test_table_name'
    id = db.Column('id', db.String, primary_key=True)