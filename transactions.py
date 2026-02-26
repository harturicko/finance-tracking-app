from sqlalchemy import *
from sqlalchemy.orm import * 
from db import db
from datetime import datetime
class Transaction(db.Model):

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    description: Mapped[str] = mapped_column(String(250), nullable = False)
    category: Mapped[str] = mapped_column(String(20), nullable = False)
    amount: Mapped[float] = mapped_column(Float, nullable = False)
    created_on: Mapped[datetime] = mapped_column(DateTime, nullable = False, default=func.now())

