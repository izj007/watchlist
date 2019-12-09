from flask import Flask,url_for,render_template

app = Flask(__name__)

name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html',name=name,movies=movies)

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
