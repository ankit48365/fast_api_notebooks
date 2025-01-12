# Interactive API Docs
# One of the standout features of FastAPI is its ability to automatically generate interactive API documentation. The Swagger UI tool integrates seamlessly with FastAPI. It provides a user-friendly web interface to visualize the documentation and exploration of the endpoints.
# FastAPI’s design follows the OpenAPI Specification (OAS) for API creation and declaration of path operations, parameters, etc. It also autogenerates the documentation of data models with JSON Schema. JSON Schema defines a JSON-based media type called “application/schema+json”. It is a format for describing the structure of JSON data. It specifies what a JSON document should be like, how to extract information from it, and how to interact with it.
# Swagger is a suite of API development utilities, of which the Swagger UI is a part. It is a REST API development tool with a web interface. The Swagger specification is now a part of the Linux Foundation and has been renamed as OpenAPI. There are a number of such OpenAPI-compliant utilities. By default, FastAPI includes support for Swagger UI and Redoc (Figure 2-2).

# Swagger UI
# Swagger UI’s web interface is built with the help of HTML, JavaScript, and CSS assets to autogenerate an interactive documentation based on the API code. Here, we shall be using it along with the REST API written with FastAPI.
# To understand how Swagger UI documentation works, let us first add one more path operation in our Hello World example. Update the hello_world.py to the code shown in Listing 2-6.

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World with Swagger UI !!!!"}

@app.get("/{name}/{id}") #  two identifiers enclosed under curly brackets -> These are called path parameters. They are passed on to the operation function below it.

async def user(name:str, id:int):
    return {"name":name, "id":id} 

# to run from CLI : 
# uvicorn 2_hello_world_swagger:app --host 127.0.0.1 --port 7000 --reload

#  The Swagger and Redoc tools actually translate the JSON representation of the API code. They use certain JavaScript and CSS code for an elegant representation of the raw JSON format in which the API schema is present. 
#  This representation is done in the “application/schema+json” media type.

# load for swagger- http://127.0.0.1:7000/docs    
# load for redoc- http://localhost:7000/redoc 

#   If you want to find out how the raw OpenAPI schema appears, use the below URL in your browser. It displays the JSON data in raw form.
# for actual json - http://localhost:7000/openapi.json

# There are many API generation tools available, similar to Swagger and Redoc. You can easily configure FastAPI to use any of these tools. 
# However, this is a slightly advanced maneuver and is beyond the scope of this book.