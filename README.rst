Introduction
------------

This is the second installment of our tour of web frameworks. This will 
be a simple TODO list.

<<<<<<< HEAD

Up and Running
--------------
Just like in the last class, you want to run bootstrap and buildout::

 # TODO: use noisebridge url
 > git clone git://github.com/eleddy/flask-noiselist.git
=======
Just like in the last class, you want to run bootstrap and buildout::
 > git clone <location to repo here>
>>>>>>> 469946adad19506bca2be4345498bafb71111de0
 > cd flask-noiselist
 > python bootstrap.py
 > ./bin/buildout

To get the server running in foreground mode, do::
<<<<<<< HEAD

=======
>>>>>>> 469946adad19506bca2be4345498bafb71111de0
 > bin/flask-ctl debug fg

Your app will be running at http://127.0.0.1:5000 with a simple hello world 
placeholder.

Take a minute to notice the differences between this app and web2py. There is 
no admin console and no formatting by default. Flask is really a micro framwork. 
<<<<<<< HEAD

Notice as well that starting we are in foreground more, and that you don't 
have to kill a process or terminal to restart. Simply Ctl-C to restart.

Modifying These Instructions
----------------------------
Since this is written by a human, please feel free to update the instructions in this
file itself and commit back. If you need permissions, feel free to contact me or just 
fork and I will merge back. If there is interest in class we will discuss how this 
works with github.


Folder Structure
----------------
Unlike web2py, you can not edit the application through the web (TTW). All the files 
you will be editing will be in flask-noiselist/src. Take note that the app itself 
should be in egg format.

script.py has a bunch of stuff you don't need to worry about in the moment. This 
basically just sets up the app for running and testing. You should never have to 
modify this.

The only python file we will be working with is __init__.py. Because the app we are 
doing is small, this will be sufficient for all of our code, although it is not 
really considered to be best practice.

Templating
----------
Note that unlike web2py, you are presented with a completely blank slate. We will be 
touching a few different files in this exercize than the previous one because of this. 
Let's get a few pretty things ironed out first so we know what we want the end result
to look like.

First, notice that we don't have any templates yet. Flask uses Jinja2, a "standalone" 
templating engine. Most modern frameworks should be integrating with 1 or more different 
templating engines. This is beneficial to you because you can learn one framework and
not have to learn a new templating language every time (web2py has its own templating 
language). Jinja2 is very popular and widely used (and more importantly that means it 
is well supported).

First we need to create a directory for holding our templates::

 > mkdir templates

And lets take our Hello page and make it into a template by adding a template::
 
 > touch hello.html

In that file, let's add a few lines to show how our list will look in the end::

 XXX: Link to that changeset

And then in __init__.py, we will connect the index page with that tempalte by
adding a decorator::

  from flask import render_template

  ...
  
  @app.route('/')
  def index():
    return render_template('hello.html')


Deployment
----------
Flask is run under WSGI. We will discuss what that means in other classes, but 
more importantly you just need to know that routing occurs outside of the app itself***
=======
Notice as well that starting we are in foreground more, and that you don't 
have to kill a process or terminal to restart. Simply Ctl-C.



>>>>>>> 469946adad19506bca2be4345498bafb71111de0




More Info
---------
<<<<<<< HEAD
 * Flask Documentation: http://flask.pocoo.org/docs/
 * About Jinja2: http://jinja.pocoo.org/docs/
 * For more info on this buildout itself, please see http://flask.pocoo.org/snippets/27/
=======
For more info on this buildout itself, please see http://flask.pocoo.org/snippets/27/
>>>>>>> 469946adad19506bca2be4345498bafb71111de0
