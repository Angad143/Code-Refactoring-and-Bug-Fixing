from flask import Flask, render_template, request
app = Flask(__name__)
notes = []
@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note:  # Check if note is not empty
            notes.append(note)
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
