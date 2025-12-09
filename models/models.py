from sqlalchemy import Column, Integer, String, DateTime, Date, Time, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database.db import Base

class User(Base):
    __tablename__ = "user"

    id_user = Column(Integer, primary_key=True)
    name = Column(String(length=50), nullable=False)
    email = Column(String(length=100), unique=True, nullable=False)
    password = Column(String(length=255), nullable=False)
    height = Column(Integer)
    weight = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    training = relationship("Training", back_populates="user")
    weeklyGoal = relationship("WeeklyGoal", back_populates="user")

class WeeklyGoal(Base):
    __tablename__ = "weeklyGoal"

    id_goal = Column(Integer, primary_key=True)
    time_goal = Column(Integer, nullable=False)
    qtd_weekly_goal = Column(Integer, nullable=False)
    period_of_day = Column(String(length=15), default="afternoon")
    fk_user = Column(Integer, ForeignKey("user.id_user"), primary_key=True)

    user = relationship("User", back_populates="weeklyGoal")

class Training(Base):
    __tablename__ = "training"

    id_training = Column(Integer, primary_key=True)
    starting_time = Column(Time, nullable=False)
    ending_time = Column(Time, nullable=False)
    training_date = Column(Date, nullable=False)
    fk_user = Column(Integer, ForeignKey("user.id_user"), nullable=False)
    
    user = relationship("User", back_populates="training")
