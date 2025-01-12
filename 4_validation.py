# numeric constraints, the maximum and minimum length of string parameters, and the metadata of path parameters to specify the title, description, alias, etc.
# for ex: For the path or query parameters of string type, you can apply min_length and/or max_length constraints to ensure that their character length is in the desired range.

from fastapi import FastAPI, Path, Query
from typing import Optional
app = FastAPI()

@app.get("/employee/{name}/branch/{branch_id}")
async def get_employee(branch_id:int,
                       name:str=Path(title='Name of Employee',
                                     description='Length minimum 10 chars',
                                     alias='EmpName', # title, description, and alias are metadata parameters that can be used to provide additional information about the path parameter.
                                     min_length=10), # example with regEx --> name:str=Path(regex="^[J]|[h]$")): -->  constrain the value of name to either begin with J or end with h (as in John, Javed, or Prakash)
                       brname:str=Query(None, 
                                        title='Branch Name',
                                        description='Length between 5 and 10 chars',
                                        min_length=5, 
                                        max_length=10), 
                       age:Optional[int]=None):
    employee={'name':name, 'Branch':brname, 'Branch ID':branch_id, 'age':age}
    return employee

# The order of the parameters has been changed because the Python function requires the nondefault arguments to be declared before those with default value. 
# The validation checks applied mean that the name (path parameter) should not be smaller than ten characters, and the length of brname (query parameter) # should be between five and ten characters. 
# The branch_id (path parameter) is an integer, and the age (query parameter) is optional.
# If the constraints are not met, FastAPI will return an error message to the client.

# To run the application, execute the following command in the terminal:
# uvicorn 4_validation:app --reload
# http://127.0.0.1:8000/docs

# when pisted this --> http://127.0.0.1:8000/employee/fgtyhju/branch/12?brname=werd   got below error -->

# {
#     "detail": [
#         {
#             "type": "string_too_short",
#             "loc": [
#                 "path",
#                 "name"
#             ],
#             "msg": "String should have at least 10 characters",
#             "input": "fgtyhju",
#             "ctx": {
#                 "min_length": 10
#             }
#         },
#         {
#             "type": "string_too_short",
#             "loc": [
#                 "query",
#                 "brname"
#             ],
#             "msg": "String should have at least 5 characters",
#             "input": "werd",
#             "ctx": {
#                 "min_length": 5
#             }
#         }
#     ]
# }

#  example below shows validation with numeric constraints using gt and le as in greater than and less than or equal to, respectively.

# from fastapi import FastAPI, Path, Query
# app = FastAPI()
# @app.get("/employee/{name}/branch/{branch_id}")
# async def get_employee(name:str, brname:str,
#                        branch_id:int=Path(1, gt=0, le=100),
#                        age:int=Query(None, ge=20, lt=61)):
#     employee={'name':name, 'Branch':brname, 'Branch ID':branch_id, 'age':age}
#     return employee