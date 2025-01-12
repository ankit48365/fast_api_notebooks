# Model Configuration
# The Config attribute of the BaseModel helps in controlling the behavior of the model. It is in fact an object of the BaseConfig class. This configuration feature can be used in many ways. For example, the max_anystr_length decides what should be the maximum length for the model’s string properties. You can also specify if you want the strings to always appear in upper- or lowercase. Set anystr_upper and/or anystr_lower to True if you want.

# One of the cool Config settings is to include a schema_extra property (Listing 3-10). Its value is a dict object giving a valid example of the model object. This acts as additional information in the documentation of the JSON Schema of the model.

# The Product model with schema_extra defined in its Config is rewritten in Listing 3-10.

# Listing 3-10:
# from pydantic import BaseModel

# class Product(BaseModel):
#     prodId:int
#     prodName:str
#     price:float
#     stock:int

#     class Config:
#         schema_extra = {
#             "example": {
#                 "prodId": 1,
#                 "prodName": "Ceiling Fan",
#                 "price": 2000,
#                 "stock": 50
#             }
#         }

# When the Swagger interface generates the Product schema, this example data appears in it, as in Figure 3-4.

# Figure 3-4: Example schema
# Larger View

# orm_mode
# The Config class inside the Pydantic model has an important property called orm_mode. If it is set to True, the Pydantic model can be created from any ORM model instance.

# The term ORM stands for object-relational mapper. It is used for the programming technique of mapping a table structure in a SQL database with a class declared in an object-oriented language such as Python. SQLAlchemy is one of the most popular ORM libraries for Python. Its main advantage is that we can programmatically interact with the database and not by executing raw SQL queries.

# If we set the orm_mode property to True, the model can be constructed from the instance of an ORM class such as the one inherited from SQLAlchemy’s declarative_base class.

# In our Product model, let us include the orm_mode configuration property (Listing 3-11).

# Listing 3-11:
# from pydantic import BaseModel
# class Product(BaseModel):
#     prodId:int
#     prodName:str
#     price:float
#     stock:int
#     class Config:
#         orm_mode=True

# Next, we shall declare a SQLAlchemy model (Listing 3-12) to match with the Pydantic model structure.

# Listing 3-12:
# from sqlalchemy import Column, Integer, Float, String
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class ProductORM(Base):
#     __tablename__ = 'products'
#     prodId = Column(Integer, primary_key=True, nullable=False)
#     prodName = Column(String(63), unique=True)
#     price = Column(Float)
#     stock = Column(Integer)

# The from_orm() method of Pydantic’s BaseModel allows a model instance to be constructed from the ORM model object. Listing 3-13 shows the usage of this method.

# Listing 3-13:
# prod_alchemy = ProductORM(
#     prodId=1,
#     prodName='Ceiling Fan',
#     price=2000,
#     stock=50
# )

# product = Product.from_orm(prod_alchemy)

# Here, the prod_alchemy is initialized, and the same is used as an argument to the from_orm() method to obtain product as the object of the Pydantic model.

# Conversely, the instance of the Product BaseModel can be parsed into an instance of the ProductORM model. We have a dict() method with the BaseModel that returns its dictionary representation. This dictionary is unpacked into an ORM object as in Listing 3-14.

# Listing 3-14:
# product=Product(prodId=2, prodName='LED Bulb', price=250, stock=50)
# prod_alchemy=ProductORM(**product.dict())

# We shall come back to this interfacing between the Pydantic and SQLAlchemy models later in this book when we discuss how to use a SQL database with the REST API.