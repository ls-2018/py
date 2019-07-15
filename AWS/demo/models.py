# encoding=utf-8
"""
@Time: 2019/7/10 11:04 
@Author: liushuo
@File: models.py 
@Desc: 
@Software: PyCharm
"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import
Base = declarative_base()
engine = create_engine(
    "mysql+mysqlconnector://root:1234@127.0.0.1:3306/l2cloud?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)
SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()

class Billing(Base):
    __tablename__ = 'billings'
    id = Column(Integer, primary_key=True)
    InvoiceID = Column(String(256), index=True, nullable=True)
    PayerAccountId = Column(String(256), nullable=True)
    LinkedAccountId = Column(String(256), nullable=True)
    ProductCode = Column(String(256), nullable=True)
    AvailabilityZone = Column(String(256), nullable=True)

    UsageStartDate = Column(String(256), nullable=True)
    UsageEndDate = Column(String(256), nullable=True)

    UsageQuantity = Column(String(256), nullable=True)
    CostBeforeTax = Column(String(256), nullable=True)
    Credits = Column(String(256), nullable=True)
    TaxAmount = Column(String(256), nullable=True)
    TotalCost = Column(String(256), nullable=True)
    Tag_Name = Column(String(256), nullable=True)
    Tag_Value = Column(String(256), nullable=True)


def create_table():
    Base.metadata.create_all(engine)


def drop_table():
    Base.metadata.drop_all(engine)

def save_data(kwarg):
    kwarg = json.loads(json.dumps(kwarg))

    obj = Billing(**kwarg)
    session.add(obj)
    # session.add_all([obj, ])
    session.commit()
    # 将连接交还给连接池
    # session.remove()
if __name__ == '__main__':
    create_table()
