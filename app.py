from flask import Flask, jsonify, render_template, jsonify, request

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,100'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        # 'salary': 'Rs. 12,00,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'San Francisco, USA',
        'salary': '$120,000'
    }
]


@app.route("/")
def hello():
    return render_template('home.html', jobs=JOBS, company_name='Chethan')


# Adding API route
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
