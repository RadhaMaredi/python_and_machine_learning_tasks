from flask import Flask, jsonify

app = Flask(__name__)

student_details = [{"student_name": "Ram",
            'rollno': "1",
            'class': "10th",
            "marks" : "500"},

           {"student_name": "Raju",
            'rollno': "2",
            'class': "10th",
            "marsk" : "630"},

           {"student_name": "Raghu",
            'rollno': "3",
            'class': "10th",
            "marks" : "570"},

           {"student_name": "Rakesh",
            'rollno': "4",
            'class': "10th",
            "marks" : "460"}
           ]

@app.route('/')
def index():
    return "<h1>Welcome SCC. batch 2012</h1>"

@app.route("/student_details", methods = ['GET'])
def get():
    return jsonify({'student_details': student_details})

@app.route("/student_details/<int:marks>", methods=['GET'])
def get_id(marks):
    return jsonify({'student_details': student_details[marks]})

@app.route("/student_details", methods = ['POST'])
def create():
    detail = {'name': "Rama",
              'rollno': "6",
              'class': "10th",
              'marks': "670"}
    student_details.append(detail)
    return jsonify({'Created': detail})

@app.route("/student_details/<int:rollno>", methods=['PUT'])
def student_detail_update(rollno):
    student_details[rollno]['student_name'] = "RADHA"
    return jsonify({'student_details': student_details[rollno]})

@app.route("/student_details/<int:rollno>", methods=['DELETE'])
def delete(rollno):
    student_details.remove(student_details[rollno])
    return jsonify({'result': True})


app.run(debug=True)