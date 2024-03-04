from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, ForeignKey
from datetime import datetime
import pytz

class Users(db.Model, UserMixin):  # base table
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(24), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(24))
    date_created = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.timezone("America/New_York")).replace(microsecond=0))
    last_login_time = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.timezone("America/New_York")).replace(microsecond=0))
    




