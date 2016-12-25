**SHABBATTABLE**
*Frijay - Friday Dinners*

### Instructions for First Time Usage ###

1. Create your own virtualenv (Python 3.5.2) and install required dependancies:
```
#!bash

pip install -r requirements.txt
```
2. Initialize the database by running the supplied shell script:

```
#!bash

sh reset_db.sh
```
3. At this point, dummy data has been inserted into the database, along with your administrative user account. 

* Username: frijay 

* Password(default): frijay_pass

4. Now, launch server:
```
#!bash

python manage.py runserver
```

### Additional Information ###
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