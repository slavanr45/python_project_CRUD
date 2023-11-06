# Homework project:
## making webserver with CRUD operations


short command to start webserver with database in JSON file:   
**make start_json**

full command to start webserver with database in JSON file:    
**poetry run gunicorn -w 5 -b 0.0.0.0:8000 webserver:app_json_file_DB run**

short command to start webserver with in 'session' object:   
**make start**

full command to start webserver with database in 'session' object:   
**poetry run gunicorn -w 5 -b 0.0.0.0:8000 webserver:app run**