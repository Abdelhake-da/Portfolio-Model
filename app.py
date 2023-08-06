import json
from flask import Flask, render_template, request,redirect, url_for
import os
import uuid

projects = []

app = Flask(__name__)
def replace_double_slash(text):
    text = text.replace('static/','/')
    return text.replace('\\', "/")
def read_file():
    with open("static/data.json") as json_file:
        return json.load(json_file)
def write_file(new_data):
    projects = read_file()
    projects.insert(0,new_data)
    with open("static/data.json", 'w') as json_file:
            json.dump(projects, json_file)
    
def print_list(lis):
    for l in lis:
        print (l)
@app.route("/")
def home():
    return render_template("index.html",projects=read_file())
@app.route("/project/<project_id>")
def project(project_id):
    for pro in read_file():
        if pro["_id"]  == project_id:
            project = pro
    return  render_template("project.html", project=project)
@app.route("/add")
def add_project():
    return render_template("add.html")

@app.route('/upload', methods=['POST'])
def upload_files():
    data = {
        "_id":"",
        "project_name":"",
        "tec":"",
        "path_img":"",
        "images":[],
        "project_disc":"",
    }

    # Generate a UUID (Version 4)
    unique_id = uuid.uuid4()
    # Check if the post request has file(s)
    name = request.form.get("name")
    tec = request.form.get("tec")
    discription = request.form.get("disc")
    if name != "":
        data['_id']=str(unique_id)
        data['project_name']= name
        data["tec"] = tec
        data["project_disc"]= discription
        if 'file' not in request.files:
            return 'No file part'

        # Get the list of files from the 'file' field in the request
        uploaded_files = request.files.getlist('file')

        if len(uploaded_files) == 0:
            return 'No file selected.'

        # Create an 'uploads' folder if it doesn't exist
        if not os.path.exists('static/uploads/'+str(unique_id)):
            os.makedirs('static/uploads/'+str(unique_id))
        f = []
        file_paths = []
        i=True
        for uploaded_file in uploaded_files:
           
            if uploaded_file:
                # Get the file path
                file_path = os.path.join('static/uploads/'+str(unique_id), uploaded_file.filename)
                f.append(replace_double_slash(file_path)) 
                if i:
                    data["path_img"]= replace_double_slash(file_path)
                    i = False
                # Save the file to the 'uploads' folder in your application
                
                uploaded_file.save(file_path)
                file_paths.append(file_path)
        data["images"] = f
        
        write_file(data)
        
    return redirect(url_for("home", projects=read_file()))

if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0")