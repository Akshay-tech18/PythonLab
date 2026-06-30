# from flask import Flask, request, jsonify

# app = Flask(__name__)
# students = {}


# # GET - Read All Students
# @app.route("/students", methods=["GET"])
# def get_students():
#     return jsonify(students), 200

# # GET - Read Single Student
# @app.route("/students/<roll>", methods=["GET"])
# def get_student(roll):

#     if roll in students:
#         return jsonify(students[roll]), 200

#     return jsonify({"error": "Student not found"}), 404


# # ----------------------------
# # POST - Create Student
# # ----------------------------
# @app.route("/students", methods=["POST"])
# def add_student():

#     data = request.get_json()

#     # Validation
#     if (not data or
#         "roll" not in data or
#         "name" not in data or
#         "course" not in data):

#         return jsonify({"error": "Invalid input"}), 400

#     roll = str(data["roll"])

#     # Check if student already exists
#     if roll in students:
#         return jsonify({"error": "Student already exists"}), 409

#     students[roll] = {
#         "name": data["name"],
#         "course": data["course"]
#     }

#     return jsonify({
#         "message": "Student added successfully"
#     }), 201


# # ----------------------------
# # PUT - Update Student
# # ----------------------------
# @app.route("/students/<roll>", methods=["PUT"])
# def update_student(roll):

#     if roll not in students:
#         return jsonify({"error": "Student not found"}), 404

#     data = request.get_json()

#     if not data:
#         return jsonify({"error": "Invalid input"}), 400

#     students[roll]["name"] = data.get(
#         "name",
#         students[roll]["name"]
#     )

#     students[roll]["course"] = data.get(
#         "course",
#         students[roll]["course"]
#     )

#     return jsonify({
#         "message": "Student updated successfully"
#     }), 200


# # ----------------------------
# # DELETE - Delete Student
# # ----------------------------
# @app.route("/students/<roll>", methods=["DELETE"])
# def delete_student(roll):

#     if roll not in students:
#         return jsonify({"error": "Student not found"}), 404

#     del students[roll]

#     return jsonify({
#         "message": "Student deleted successfully"
#     }), 200


# # ----------------------------
# # Run Flask App
# # ----------------------------
# if __name__ == "__main__":
#     app.run(debug=True, use_reloader=False)

from flask import Flask, request, jsonify

app = Flask(__name__)
students = {}

@app.route("/students", methods=["GET"])
def get_all():
    return jsonify(students)

@app.route("/students/<roll>", methods=["GET"])
def get(roll):
    return jsonify(students.get(roll, "Not Found"))

@app.route("/students", methods=["POST"])
def add():
    d = request.json
    students[str(d["roll"])] = {
        "name": d["name"],
        "course": d["course"]
    }
    return jsonify({"msg": "Added"})

@app.route("/students/<roll>", methods=["PUT"])
def update(roll):
    d = request.json
    if roll in students:
        students[roll].update(d)
        return jsonify({"msg": "Updated"})
    return jsonify({"msg": "Not Found"})

@app.route("/students/<roll>", methods=["DELETE"])
def delete(roll):
    students.pop(roll, None)
    return jsonify({"msg": "Deleted"})

app.run(debug=True)
