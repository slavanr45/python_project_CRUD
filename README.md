# CRUD project:
This is a small project, showing how to work with all the standard CRUD functions
(Create, Read, Update, Delete) using Flask. Consists of 7 main routes:

1. **Show users list:** @app.route('/users')              
2. **User information:** @app.route('/users/int:id')
3. **New user form:** @app.route('/users/new')
4. **Make new user:** @app.route('/users', methods=['post'])
5. **Edit user form:** @app.route('/users/int:id/edit')
6. **Update user information:** @app.route('/users/int:id/edit', methods=['POST'])
7. **Delete user:** @app.route('/users/int:id/delete', methods=['POST'])

## Usage
1. You can start webserver with database in JSON file:
- **make start_json** or
- **poetry run gunicorn -w 5 -b 0.0.0.0:8000 webserver:app_json_file_DB run**
2. Or can start webserver with in 'session' object:
- **make start** or
- **poetry run gunicorn -w 5 -b 0.0.0.0:8000 webserver:app run**
3. Enter a password '123' in input field and click "Login" button for autorization
4. Now you can use simple user registration system: show, add, edit, delete users
5. On each page you can logout from testing system by "Logout" button

## Technologies Used
- Python
- Flask + jinja
- HTML/CSS
