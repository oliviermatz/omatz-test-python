import azure.functions as func
import logging

app = func.FunctionApp()

@app.function_name(name="HttpTrigger")
@app.route(route="hello")
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("HttpExample function processed a request!")
