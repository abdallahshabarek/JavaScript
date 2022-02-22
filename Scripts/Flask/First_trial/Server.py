
import flask
from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
from UI import render_ui, render_original, render_ui_3d



app = Flask(__name__)
api = Api(app)

# @app.route('/', methods=['POST'])
# def addRegion():
#     ...
#     return (flask.request.form['projectFilePath'])

@app.route("/", methods = ['GET','POST'])
def render():
    if flask.request.method == 'POST':
        if flask.request.form['action'] == 'Submit':
            print("NEW >>>")
            request = flask.request.form
            print (request)
            hexid = request['gridid']
            # print(flask.request.form.get['gridid'])
            # return (flask.request.form['template.html'])
            return render_ui(hexid = request['gridid'], analysis_type=request['analysis_type'], year=request['year'], month=request['month'], resolution=request['resolution'], region =request['region'])#render_template("template.html")
        if flask.request.form['action'] == 'Vizualize':
            print("NEW >>>")
            request = flask.request.form
            print (request)
            hexid = request['gridid']
            # print(flask.request.form.get['gridid'])
            # return (flask.request.form['template.html'])
            # hexid = 10, analysis_type= "destination", year = "2019", month = "1", resolution = "6", region = "16"
            return render_ui_3d(hexid = request['gridid'], analysis_type=request['analysis_type'], year=request['year'], month=request['month'], resolution=request['resolution'], region =request['region'])#render_template("template.html")
    return render_original()

if __name__ == "__main__":
    app.run(host ="localhost",debug = True)


