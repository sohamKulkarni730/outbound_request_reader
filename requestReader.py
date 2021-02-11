from flask import Flask, request
import datetime
import json

app = Flask(__name__)


# default route to test via browser GET
@app.route("/")
def welcome():
    return """\
                <!-- #######  THIS IS A COMMENT - Visible only in the source editor #########-->
                <pre style="padding-left: 30px;"> 
                     <br />       This application is acting like psudo API .Receive request and sends success responce with body whenever necessary.
                     <br />       Few URL routes are configured and <span style="color: #ff0000;"><em><strong>will only work for pre-configured route + HTTP method combination</strong></em></span>
                     <br />       
                     <br />
                     <br />       Routes configured are:
                     <br />
                     <br />         /instructor
                     <br />         /session
                     <br />         /session/&lt;SessionId&gt;
                     <br />         /session/&lt;SessionId&gt;/user/&lt;base64EncodedEmail&gt;/url
                     <br />         /session/&lt;SessionId&gt;/attendees
                     <br /><br /><br /><br />
                     <br />&nabla; <strong>Soham .S. Kulkarni</strong> </pre>
                  """

@app.route("/read_request")
def request_reader():
    print(request.headers)

# Testing data - not business logic - should be removed later
    if (len(request.data) != 0):
        data = json.loads(request.data)
        print(data)

    # returning a success responce - Creating Dictionary -> Converting to JSON string -> Sending as responce
    dict = {}
    dict["status"] = "success"
    dict["correlationId"] = "correlationId"
    dict["timestamp"] = datetime.datetime.now()

    return "responce"


# add and update instructor routine -- POST and PUT methods are supported
@app.route("/instructor", methods=['POST', 'PUT'])
def instructor():
    print(request.headers)

# Testing data - not business logic - should be removed later
    if (len(request.data) != 0):
        data = json.loads(request.data)
        print(data)

    # returning a success responce - Creating Dictionary -> Converting to JSON string -> Sending as responce
    dict = {}
    dict["status"] = "success"
    dict["correlationId"] = request.headers.get("correlationId")
    dict["timestamp"] = f"{datetime.datetime.now()}"
    reponse = json.dumps(dict)

    return reponse


# Session create routine - POST method supported
@app.route("/session", methods=['POST'])
def session():
    print(request.headers)

# Testing data - not business logic - should be removed later
    if len(request.data) != 0:
        data = json.loads(request.data)
        print(data)

    # returning a success responce - Creating Dictionary -> Converting to JSON string -> Sending as responce
    dict = {}
    dict["status"] = "success"
    dict["correlationId"] = request.headers.get("correlationId")
    dict["timestamp"] = f"{datetime.datetime.now()}"
    reponse = json.dumps(dict)

    return reponse


## Update session routine  - PUT method supported
@app.route("/session/<SessionId>", methods=['PUT'])
def session_update(SessionId):
    print(request.headers)

# Testing data - not business logic - should be removed later
    if (len(request.data) != 0):
        data = json.loads(request.data)
        print(data)

    # returning a success responce - Creating Dictionary -> Converting to JSON string -> Sending as responce
    dict = {}
    dict["status"] = "success"
    dict["correlationId"] = request.headers.get("correlationId")
    dict["timestamp"] = f"{datetime.datetime.now()}"
    reponse = json.dumps(dict)

    return reponse


## Fetch URL routine -- GET method supported
@app.route("/session/<SessionId>/user/<base64EncodedEmail>/url", methods=['GET'])
def fetch_url(SessionId, base64EncodedEmail):
    print(request.headers)

# Testing data - not business logic - should be removed later
    if (len(request.data) != 0):
        data = json.loads(request.data)
        print(data)

    # returning a success responce - Creating Dictionary -> Converting to JSON string -> Sending as responce
    dict = {}
    dict["status"] = "success"
    dict["correlationId"] = request.headers.get("correlationId")
    dict["timestamp"] = f"{datetime.datetime.now()}"
    url_dict = {}
    url_dict["joinUrl"] = "https://www.google.com"
    dict["data"] = url_dict

    reponse = json.dumps(dict)

    return reponse


# Get attendees routine - GET MEthod supported
@app.route("/session/<SessionId>/attendees", methods=['GET'])
def get_attendees(SessionId):
    print(request.headers)

# Testing data - not business logic - should be removed later
    if (len(request.data) != 0):
        data = json.loads(request.data)
        print(data)

    #returning a success responce - Creating Dictionary -> Converting to JSON string -> Sending as responce
    dict = {}
    dict["status"] = "success"
    dict["correlationId"] = request.headers.get("correlationId")
    dict["timestamp"] = f"{datetime.datetime.now()}"

    attendee_data = {}
    attendee_data["attendees"] = []

    attendee = {}
    attendee["email"] = "123test@tcs.com"
    attendee_data["attendees"].append(attendee)

    dict["data"] = attendee_data
    reponse = json.dumps(dict)

    return reponse


# application start
if __name__ == '__main__':
    app.run(debug=False)
