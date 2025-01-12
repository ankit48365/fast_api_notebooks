# POST Method
# A web browser software can send the request only through the GET method. 
# We know that a GET request is used to retrieve one or more resources on the HTTP server. 
# The path and/or query parameters in the request URL serve as a filter to fetch the data of specific resources.
# Using the GET method for client-server interaction over HTTP has certain drawbacks. First of all, it is not very secure as the URL along with the parameter data is revealed 
# in the address bar of the browser. Secondly, there is a limit to how much data can be sent to the server along with the GET request 
# (and the limit is not very big either – in the range of a few kilobytes only!). Moreover, the data to be sent must be representable in ASCII characters only. 
# That means any binary data such as an image can’t be a part of the GET request.
# To send a request for creating a new resource on the server, the HTTP protocol requires that the POST method should be used. 
# The data that is required for a new resource is packed in the body of the POST request. This serves two purposes. 
# The body part is not displayed in the browser’s address bar; hence, it is a more secure method. 
# Secondly, there is no size limit, and raw binary data can also be a part of the HTTP request body.
# As a web browser cannot be used to raise a POST request directly, we have to find other means. 
# We can use an HTTP client such as the Curl command-line tool to send a POST request. 
# 
# A typical example of Curl’s POST command is shown in Listing 3-1.
# Listing 3-1:
# curl -i -H "Content-Type: application/json" -X POST -d "{\"prodId\":\"1\",\"prodName\":\"Ceiling Fan\", \"price\":\"2000\", \"stock\":\"50\" }"  http://localhost:8000/product

# Note that we need to set the POST method explicitly with the -X option (remember that the default HTTP method is GET). The -d option is followed by the parameters and their values in JSON format. 
# This data populates the body of the HTTP request.
# We can also use certain web-based tools such as the Postman app or Swagger UI for this purpose or make an HTML form to send the request submitting the data with the POST method.
# We have now become fairly conversant with the Swagger UI. We shall continue to use it in this chapter to understand how the data in the HTTP body is processed by FastAPI. 
# In a subsequent chapter, we shall deal with the HTML form data.

# Body Parameters
# In a FastAPI app, POST requests are handled by the @app.post() decorator. As explained earlier, the path operation decorator needs a mandatory path string argument. 
# (If the URL has any path parameters, their placeholder identifiers may appear in the path string as we learned in the previous chapter.)

# The ASGI server passes the request’s context data to the coroutine function (we call it an operation function) defined just below the @app.post() decorator. 
# It contains the request object and the body data.

# The value of each parameter of the body data is passed to the corresponding Body parameter declared in the operation function’s definition. 
# A Body parameter is an object of the Body class in FastAPI (similar to Path and Query classes).

# To process the POST request raised by the Curl command mentioned earlier, let us define the addnew() operation function under the POST decorator (Listing 3-2).

# Listing 3-2:
from fastapi import FastAPI, Body, Request
app = FastAPI()

@app.post("/product")
async def addnew(request: Request, prodId:int = Body(), prodName:str = Body(), price:float=Body(), stock:int = Body()):
    product={'Product ID':prodId, 'product name':prodName,
             'Price':price, 'Stock':stock}
    return product

# The addnew() function is defined with the Body parameters – prodId, prodName, price, and stock. They are in fact the objects of the Body class. 
# All the arguments to the Body class constructor are optional.

# Run the preceding FastAPI code and launch the Uvicorn server on the localhost. 
# uvicorn 5_post:app --reload


# Then open a command terminal and issue the POST Curl command mentioned earlier. As shown in Listing 3-3, the terminal returns a JSON response of the addnew() function along with the HTTP headers.
#  worked on bash terminal and failed on powersehll terminal
# curl -i -H "Content-Type: application/json" -X POST -d "{\"prodId\":\"1\",\"prodName\":\"Ceiling Fan\", \"price\":\"2000\", \"stock\":\"50\" }"  http://localhost:8000/product

# Listing 3-3:
# HTTP/1.1 200 OK
# date: Fri, 26 Aug 2022 17:38:00 GMT
# server: uvicorn
# content-length: 71
# content-type: application/json

# {"Product ID":1,"product name":"Ceiling Fan","Price":2000.0,"Stock":50}

# The Swagger UI is more convenient to use rather than the Curl tool, especially while testing the response of the routes of a FastAPI app (Figure 3-1). So, while the server is running, visit the http://localhost:8000/docs link with a web browser.
# http://127.0.0.1:8000/docs

# The Swagger UI page opens up. Click on the POST button to expand the /product route. Click on the Try it out button.
# In the Request body section, enter the JSON data as shown in Figure 3-2. Click on the Execute button.