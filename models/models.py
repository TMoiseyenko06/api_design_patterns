from flask_sqlalchemy import SQLAlchemy
from database import db, Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Date, Integer
import datetime

class Employee(Base):
    __tablename__ = 'employees'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255),nullable=False)
    position: Mapped[str] = mapped_column(db.String(255),nullable=False)

class Product(Base):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255),nullable=False)
    price: Mapped[float] = mapped_column(db.Float)

class Customer(Base):
    __tablename__ = 'customers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255),nullable=False)
    email: Mapped[str] = mapped_column(db.String(255))
    phone: Mapped[str] = mapped_column(db.String(255))

class Order(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id'),nullable=False)
    product_id: Mapped[int] = mapped_column(db.ForeignKey('products.id'),nullable=False)
    quantity: Mapped[int] = mapped_column(db.Integer,nullable=False)
    total_price: Mapped[float] = mapped_column(db.Float,nullable=False)

class Production(Base):
    __tablename__ = 'production'
    id: Mapped[int] = mapped_column(primary_key=True)
    employee_id: Mapped[int] = mapped_column(db.ForeignKey('employees.id'))
    product_id: Mapped[int] = mapped_column(db.ForeignKey('products.id'))
    quantity_produced: Mapped[int] = mapped_column(db.Integer,nullable=False)
    date_produced: Mapped[datetime.date] = mapped_column(Date,default=datetime.date.today())