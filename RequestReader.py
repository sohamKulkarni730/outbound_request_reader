from flask import Flask, request
import datetime
import json

app = Flask(__name__)


@app.route("/")
def welcome():
    return "go to /read_request"



@app.route("/read_request")
def request_reader():
    print(request.headers)

    if (len(request.data) != 0):
        data = json.loads(request.data)
        print(data)

    dict = {}
    dict["status"] = "success"
    dict["correlationId"] = "correlationId"
    dict["timestamp"] = datetime.datetime.now()

    return "responce"

@app.route("/instructor" ,methods = ['POST', 'PUT'])
def instructor():
    print(request.headers)

    if (len(request.data) != 0):
        data = json.loads(request.data)
        print(data)


    dict = {}
    dict["status"] = "success"
    dict["correlationId"] = request.headers.get("correlationId")
    dict["timestamp"] = f"{datetime.datetime.now()}"
    reponse = json.dumps(dict)


    return reponse


@app.route("/session"  ,methods = ['POST'])
def session():
    print(request.headers)

    if (len(request.data) != 0):
        data = json.loads(request.data)
        print(data)

    dict = {}
    dict["status"] = "success"
    dict["correlationId"] = request.headers.get("correlationId")
    dict["timestamp"] = f"{datetime.datetime.now()}"
    reponse = json.dumps(dict)

    return reponse

@app.route("/session/<SessionId>" , methods = ['PUT'] )
def session_update(SessionId):
    print(request.headers)

    if (len(request.data) != 0):
        data = json.loads(request.data)
        print(data)

    dict = {}
    dict["status"] = "success"
    dict["correlationId"] = request.headers.get("correlationId")
    dict["timestamp"] = f"{datetime.datetime.now()}"
    reponse = json.dumps(dict)

    return reponse


@app.route("/session/<SessionId>/user/<base64EncodedEmail>/url" , methods = ['GET'] )
def fetch_url(SessionId,base64EncodedEmail):
    print(request.headers)

    if (len(request.data) != 0):
        data = json.loads(request.data)
        print(data)

    dict = {}
    dict["status"] = "success"
    dict["correlationId"] = request.headers.get("correlationId")
    dict["timestamp"] = f"{datetime.datetime.now()}"
    url_dict ={}
    url_dict["joinUrl"] = "https://www.google.com"
    dict["data"] = url_dict

    reponse = json.dumps(dict)

    return reponse


@app.route("/session/<SessionId>/attendees", methods=['GET'])
def get_attendees(SessionId):
    print(request.headers)

    if (len(request.data) != 0):
        data = json.loads(request.data)
        print(data)

    dict = {}
    dict["status"] = "success"
    dict["correlationId"] = request.headers.get("correlationId")
    dict["timestamp"] = f"{datetime.datetime.now()}"


    attendee_data = {}
    attendee_data["attendees"] =[]

    attendee = {}
    attendee["email"] = "123test@tcs.com"
    attendee_data["attendees"].append(attendee)

    dict["data"]= attendee_data
    reponse = json.dumps(dict)

    return reponse


# application start
if __name__ == '__main__':
    app.run(debug=False)

