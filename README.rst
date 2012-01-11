Introduction
------------

This is the second installment of our tour of web frameworks. This will 
be a simple TODO list.

Just like in the last class, you want to run bootstrap and buildout::
 > git clone <location to repo here>
 > cd flask-noiselist
 > python bootstrap.py
 > ./bin/buildout

To get the server running in foreground mode, do::
 > bin/flask-ctl debug fg

Your app will be running at http://127.0.0.1:5000 with a simple hello world 
placeholder.

Take a minute to notice the differences between this app and web2py. There is 
no admin console and no formatting by default. Flask is really a micro framwork. 
Notice as well that starting we are in foreground more, and that you don't 
have to kill a process or terminal to restart. Simply Ctl-C.







More Info
---------
For more info on this buildout itself, please see http://flask.pocoo.org/snippets/27/
