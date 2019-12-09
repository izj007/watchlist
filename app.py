from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
def hello_world():
    return 'Hello World!1111<h1>this is a title!</h1>'

@app.route('/user/<username>')
def user_page(username):
    return 'User is %s' % username
@app.route('/test')
def url_test_for():
    print(url_for('hello_world'))
    print(url_for('user_page',username='mike'))
    print(url_for('user_page',username='Lili'))
    print(url_for('url_test_for'))
    print(url_for('url_test_for',num=2))
    return 'End'

if __name__ == '__main__':
    app.run()
