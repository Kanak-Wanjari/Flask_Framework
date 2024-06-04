from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Kanak"
    return render_template('index.html', Name = name)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return 'This is the contact page'

if __name__ == '__main__':
    app.run(debug=True)