from flask import Flask, render_template

app = Flask(__name__)

users = ['mike', 'mishel', 'adel', 'keks', 'kamila']


@app.route('/')
def index():
    return render_template('index.html')


# BEGIN (write your solution here)
@app.route('/users/')
def get_users():
    return render_template(
        'users/index.html',
        users=users)


@app.route('/users/<int:id>')
def get_user_data(id):
    user = next(filter(lambda x: x['id'] == id, users), None)
    if user is not None:
        return render_template(
            'users/show.html',
            user=user)
    return not_found()


@app.errorhandler(404)
def not_found():
    return 'Page not found', 404

# END
