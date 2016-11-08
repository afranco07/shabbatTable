To run the server on local instance, run 
```
#!bash

python manage.py runserver
```


In addition, server can be launched via gunicorn using the command 
```
#!bash

gunicorn shabbattable.wsgi
```
To use gunicorn, do 
```
#!bash

pip install gunicorn
```


The admin panel can be reached at 127.0.0.1:8000/admin/

Website is deployed at [heroku](http://shabbattable.herokuapp.com/frijay/)