from flask import Flask, jsonify, request #importing flask

#creating flask object
app= Flask(__name__) 

tasks = [ #json format
    {
        #object 1
        'id':1,
        'Name':u'Sameer',
        'Contact':u'981727838',
        'done':False
    },
    {
        #object 2
        'id':2,
        'Name':u'Max',
        'Contact': u'7847384859',
        'done':False
    }
]

@app.route("/add-data", methods=["POST"]) #setting route,app data is url here...instead send post request
def add_task():
    if not request.json:
        return jsonify({ #if not data found then give 404 error xD
            "status":"error",
            "message":"PLease prove the data"
        },400)

#adding the tasks to task
    contact = {
        'id': tasks[-1]['id'] +1, #+1 is for second id
        'Name': request.json['Name'],
        'Contact':request.json.get('Contact',""),
        'done':False
    }
    tasks.append(contact)#adding task to tasks
    return jsonify({
        "status":"success", #if task added then success
        "message":"Contact added Successfully"
    })

# @app.route("/greet") #route is decorator, /greet is url
# def hello_world():
#     return "Hello World!" #just printing hello world

#running the application
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks #the tasks above will return as json format with key data
    })

#running web application
if(__name__ == "__main__"):
    app.run(debug=True)

#to activate venv: .\venv\Scripts\activate