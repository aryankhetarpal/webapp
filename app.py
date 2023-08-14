from flask import Flask, render_template, jsonify, request, redirect, url_for
from database import add_to_db

app = Flask(__name__)

@app.route('/')
def webapp():
    return render_template('home.html')

@app.route('/input', methods=['POST'])
def enter_shift():
    data = request.form
    print("Data before passing to add_to_db:", data)  # Print the data dictionary
    add_to_db(data)
    return redirect(url_for('webapp'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
