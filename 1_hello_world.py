# FastAPI was developed by Sebastian Ramirez in December 2018. FastAPI 0.79.0 is the currently available version (released in July 2022). In spite of being very young, it has very quickly climbed up on the popularity charts and is one of the most loved web frameworks.
# So, let’s go ahead and install FastAPI (preferably in a virtual environment). It’s easy. Just use the PIP utility to get it from the PyPI repository. Ensure that you are using Python’s 3.6 version or later:

# pip3 install fastapi

# Since FastAPI is built on top of two important libraries, Starlette and Pydantic, they are also installed, along with some others.
# You also need to install the Uvicorn package to serve the FastAPI app:

# pip3 install uvicorn[standard]

# The “standard” option installs the Cython-based dependencies, uvloop, httptools, and websockets. If you don’t intend to use WebSockets, this option may be omitted. Certain additional supporting libraries are also installed.

#########################################################


# anyio is an asynchronous networking and concurrency library that implements a structured concurrency on top of asyncio.

# click stands for Command Line Interface Creation Kit. This package is required if you intend to use typer for building a CLI instead of a web API.

# colorama is a cross-platform library to render colored text in the Python terminal.

# The h11 package is used internally by the Uvicorn server to implement the HTTP/1.1 protocol.

# The typing-extensions module acts as a backport for Python 3.6–based applications. It may not be used if you are using newer versions of Python (version 3.7+).

# The watchfiles package is a simple, modern, and high-performance file watching and code reload in Python. To autoreload the application code when it is already running on the server, the watchfiles package is needed.

# The sniffio package detects which async library is being used by your code.

# Using python-dotenv is a convenient way to load the environment variables from a .env file.

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/") # called decorator
async def index(): # decorator mapped function
    return {"message": "Hello World !!!!"}

if __name__ == "__learn_fast_api_11__":
    # we are going to use the Uvicorn server to run a FastAPI application. It is an ASGI implementation for Python. 
    # You can start the Uvicorn server either by using the command-line interface of the Uvicorn library or programmatically by calling its run() function.
    uvicorn.run("1_hello_world:app", host="127.0.0.1", port=7000, reload=True)
    # if not from code and line above  then run from command line as below
    #  uvicorn learn_fast_api_11:app --host 127.0.0.1 --port 7000 --reload


# FastAPI, as per the OpenAPI standards, these methods are called operations. So, 
# the GET operation retrieves a resource, 
# the POST operation creates a new resource, and 
# the PUT and DELETE operations modify and delete a resource, respectively.
# They are @app.get(), @app.post(), @app.put(), and @app.delete().

# The FastAPI class defines path operation methods corresponding to HTTP operations mentioned earlier. 

# These methods need a mandatory path parameter – as in @app.get("/"). The @ symbol is prefixed to indicate that they are decorators.
