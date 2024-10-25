from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Load the CSV data
def load_attendance_data():
    df = pd.read_csv('/Users/yogesh/projects/CNTv1/attendance.csv')
    return df

@app.route('/')
def index():
    data = load_attendance_data().to_dict(orient='records')
    return render_template('dashboard.html', attendance_data=data)

if __name__ == '__main__':
    app.run(debug=True)
