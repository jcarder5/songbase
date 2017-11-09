from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    #return '<h1>hello world!!!!!</h1>'
    return render_template('idex.html')


@app.route('/user/<string:name>/')
def get_user(name):
    #return '<h1>hello %s your age is %d</h1>' % (name, 3)
    return render_template('user.html', user_name = name)


@app.route('/songs')
def list_all_songs():

    songs = [
    'song 1'
    'song 2'
    'song 3'
    ]
    return render_template('songs.html', songs=songs)

if __name__ == '__main__':
    app.run()
