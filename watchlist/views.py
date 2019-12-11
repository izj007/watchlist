from flask import request,url_for,render_template,redirect,flash
from flask_login import login_required,current_user,logout_user,login_user

from watchlist import app,db
from watchlist.models import User,Movie,Message

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            flash('Invalid input.')
            return redirect(url_for('login'))
        user=User.query.first()
        if username==user.username and user.validate_password(password):
            login_user(user)
            flash('Login Success.')
            return redirect(url_for('index'))
        flash('Correct username or password.')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('GoogBye.')
    return redirect(url_for('index'))

@app.route('/',methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
    if request.method=='POST':
        if not current_user.is_authenticated:
            return redirect(url_for('index'))
        title=request.form.get('title')
        year = request.form.get('year')
        if not title or not year or len(year)>4 or len(title)>60:
            flash('Invalid input.')
            return redirect(url_for('index'))
        movie=Movie(title=title,year=year)
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('index'))
    movies=Movie.query.all()
    return render_template('index.html',movies=movies)


@app.route('/settings',methods=['GET','POST'])
def settings():
    if request.method=='POST':
        name=request.form['name']
        if not name or len(name)>20:
            flash('Correct Name.')
            return  redirect(url_for('index'))
        current_user.name=name
        db.session.commit()
        flash('Settings Succsess.')
        return redirect(url_for('index'))
    return render_template('setting.html')



@app.route('/movie/edit/<int:movie_id>',methods=['GET','POST'])
@login_required
def edit(movie_id):
    movie=Movie.query.get_or_404(movie_id)
    if request.method=='POST':
        title=request.form['title']
        year=request.form['year']
        if not title or not year or len(year)>4 or len(title)>60:
            return redirect(url_for('edit',movie_id=movie_id))
        movie.title=title
        movie.year=year
        db.session.commit()
        flash('Item Updated.')
        return redirect(url_for('index'))
    return render_template('edit.html',movie=movie)

@app.route('/movie/delete/<int:movie_id>',methods=['POST'])
@login_required
def delete(movie_id):
    movie=Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('Delete Completed.')
    return redirect(url_for('index'))

@app.route('/message',methods=['GET','POST'])
def message():
    if request.method=='POST':
        name = request.form['name']
        message = request.form['message']
        if not name or not message:
            return redirect(url_for('message'))
        messages=Message(name=name,message=message)
        db.session.add(messages)
        db.session.commit()
        flash('Message Add Success.')
        return redirect(url_for('message'))
    messages = Message.query.order_by(Message.id.desc()).all()
    return render_template('message.html',messages=messages)
