# Weather-app-django

Its a simple Web-App that shows weather info of the cities. Users have options to add/delete their interested cities by providing the City names.

Instructions to run the App:
--
1) Download all files to local directory. 
2) Get the App-key from Openweathermap website (Need to register in website and get the key).
3) Replace the key in https://github.com/aravindprasad90/weather-webapp-django/blob/master/weather_proj/weather/views.py file, line number - 10.


Steps for creating Virtualenv:
----
1) pip install virtualenv
2) pip install virtualenvwrapper 
3) In Bash file ==> "export WORKON_HOME=~/.virtualenvs; source /usr/local/bin/virtualenvwrapper.sh"
4) Create a directory for project and goto directory. 
5) Create the virtual env ==> "mkvirtualenv -a $(pwd) name-of-env"
(This will help to map the virtual enviromnment to the path location)
6) To start wroking on virtual env ==> workon name-of-env
7) For deleting the virtualenv, "rmvirtualenv name-of-env"
8) For viewing the list of packages in virtual env, "pip list"


