import azure.functions as func
import logging

# Create a Function App with HTTP trigger authentication
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# Define an HTTP trigger route for "func_testtinggithubactions"
@app.route(route="func_testtinggithubactions")
def func_testtinggithubactions(req: func.HttpRequest) -> func.HttpResponse:
    # Log that the function processed a request
    logging.info('Python HTTP trigger function processed a request.')

    # Get the name from the query string or request body
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    # Generate a fun response with ASCII art
    if name:
        response_message = (
            f"Hello, {name}! 🚀\n"
            "This Serverless function is blasting off to new heights!"
            " 🌌🚀"
        )
        return func.HttpResponse(response_message, status_code=200)
    else:
        # Provide a custom message when the name is not provided
        return func.HttpResponse(
            "Hooray ..Serverless is super duper awesome!! 🎉 "
            "Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )


