from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.after_request
def add_header(response):
    response.cache_control.public = True
    response.cache_control.max_age = 300
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
