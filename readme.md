To run the server on local instance, run 
```
#!bash

python manage.py runserver
```

On production, this website should be launched using gunicorn.
```
#!bash

gunicorn shabbattable.wsgi
```
Be sure to use virtualenv when working with libraries from this project. Sync your pip with

```
#!bash

pip install -r requirements.txt
```

In addition, developer documentation can be found on the wiki.


The admin panel can be reached at 127.0.0.1:8000/admin/

Website is deployed at [heroku](https://shabbattable.herokuapp.com/)