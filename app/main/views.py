# from flask import render_template,request,redirect,url_for
from . import main
# from ..request import get_movies,get_movie,search_movie
# from .forms import ReviewForm
# from ..models import Review
from flask_login import login_required, current_user
from flask import render_template,request,redirect,url_for,abort
from ..models import Pitch, User, Comment
from .forms import PitchForm,UpdateProfile
# from .. import db
from .. import db,photos



@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    message = 'Hello World'
    return render_template('index.html',message = message)
# @main.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''

#     # Getting popular movie
#     popular_movies = get_movies('popular')
#     upcoming_movie = get_movies('upcoming')
#     now_showing_movie = get_movies('now_playing')

#     title = 'Home - Welcome to The best Movie Review Website Online'

#     search_movie = request.args.get('movie_query')

#     if search_movie:
#         return redirect(url_for('search',movie_name=search_movie))
#     else:
#         return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )
# @main.route('/movies/<int:id>')
# def movies(movie_id):

#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#     return render_template('movie.html',id = movie_id)

# @main.route('/movie/<int:id>')
# def movie(id):

#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#     movie = get_movie(id)
#     title = f'{movie.title}'
#     pitches = Pitch.get_pitches(movie.id)

#     return render_template('movie.html',title = title,movie = movie,pitches = pitches)

# @main.route('/search/<movie_name>')
# def search(movie_name):
#     '''
#     View function to display the search results
#     '''
#     movie_name_list = movie_name.split(" ")
#     movie_name_format = "+".join(movie_name_list)
#     searched_movies = search_movie(movie_name_format)
#     title = f'search results for {movie_name}'
#     return render_template('search.html',movies = searched_movies)

    
@main.route('/new', methods=['GET', 'POST'])
@login_required

def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():

        pitch = form.pitch.data
        title = form.title.data
        category = form.category.data
    
        new_pitch = Pitch(pitch=pitch, title=title, category=category, user_id=current_user.id)

        db.session.add(new_pitch)
        db.session.commit()

    return render_template('new_pitch.html', pitch_form=form)




@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)



@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))