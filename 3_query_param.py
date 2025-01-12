# uvicorn 3_query_param:app --host 127.0.0.1 --port 7000 --reload
# swagger - http://127.0.0.1:7000/docs

# from fastapi import FastAPI
# app = FastAPI()

# @app.get("/employee/{name}")
# async def get_employee(name:str, age:int):  # can use {age:int=20} for a query parameter with default value or {age:Optional[int]=None} for marking it optional, so when not requested it will return null {import this - From typing import Optional}
#     return {"name":name, "age":age}


# The decorator parses the value after /employee into a path parameter called name. 
# However, its mapped function declares one more parameter – age. How does the router receive a value for this parameter?

# In the list of parameters, while name is a path parameter as before, age is identified as a query parameter 
# (note that both parameters are marked as required). Click the Execute button. Figure 2-14 shows the autogenerated request URL.

# on swagger --> try it out --> try name and age -->  execute --> o/p response--> http://127.0.0.1:7000/employee/ank?age=20 

# The URL http://localhost:8000/employee/Rahul?age=20 shows the query string appended after a ? symbol in front of the path parameter. 
# If there are more than one query parameter, the parameter=value pairs are concatenated by the & symbol.

# to understand the order of fixed / path / query parameters, comment out above and run below part 

from typing import Optional
from fastapi import FastAPI
app = FastAPI()

@app.get("/employee/{name}/branch/{branch_id}")
async def get_employee(name:str, brname:str, branch_id:int,
                       age:Optional[int]=None):
    employee={'name':name, 'Branch':brname,
              'Branch ID':branch_id, 'age':age}
    return employee

# above code on swagger reponsewill give url like below
# reponse:
# http://127.0.0.1:7000/employee/Ankit/branch/12?brname=wed&age=12      {here employee and branch are fixed part,   ankit and 12 are path paramemters    ?branme=wed&adge=12 are query parameters}