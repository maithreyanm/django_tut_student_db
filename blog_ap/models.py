from django.db import models
from blog_ap.sql import session
# Create your models here.
from django.utils import timezone
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Person():
    __tablename__ = 'Person'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    phone = Column(Integer)

    def save(self):
        try:
            session.add(self)
            session.commit()
            return self
        except Exception as e:
            session.rollback()
            raise e



class Email():
    __tablename__ = 'email'

    id = Column(Integer, primary_key=True)
    email_1 = Column(String)
    email_2 = Column(String)

    def save(self):
        try:
            session.add(self)
            session.commit()
            return self
        except Exception as e:
            session.rollback()
            raise e