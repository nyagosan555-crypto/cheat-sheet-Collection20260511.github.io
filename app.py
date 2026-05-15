from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "<h1>Hello！</h1>"

@app.route('/')
def public_index():
    return render_template('public/index.html')

@app.route('/info/')
def public_info():
    return render_template('public/info.html')

if __name__ == '__main__':
    app.run(debug=True)