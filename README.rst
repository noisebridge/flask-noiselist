Introduction
------------

This is the second installment of our tour of web frameworks. This will 
be a simple TODO list.


Up and Running
--------------
Just like in the last class, you want to run bootstrap and buildout. Unlike the last
class, the cloned noiselist is the full solution so you can view the commit log to see 
how the app was built step by step. To get the first step::

 > git clone git://github.com/eleddy/flask-noiselist.git
 > cd flask-noiselist
 > git checkout -b ba4ebf111f
 > cd flask-noiselist
 > python bootstrap.py
 > ./bin/buildout

To get the server running in foreground mode, do::

 > bin/flask-ctl debug fg

Your app will be running at http://127.0.0.1:5000 with a simple hello world 
placeholder.

Take a minute to notice the differences between this app and web2py. There is 
no admin console and no formatting by default. Flask is really a micro framwork. 

Notice as well that starting we are in foreground mode, and that you don't 
have to kill a process or terminal to restart. Simply Ctl-C to restart. This 
also means that any pdbing will take you directly to this console.

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
 
 <!DOCTYPE html>
  <html>
    <head>
      <title>TODO at Noisebridge</title>
    </head>
    <body>
      <h1>My Personal TODO List</h1>
      <ul>
        <li>Finish evaluating pull requests</li>
        <li>Finish writing up class work</li>
        <li>Swim and enjoy the sun</li>
      <ul>
      <form action="" method="POST" id="add_to_todo_list">
        <input type="text" name="todo_item"/>
        <input type="submit" name="add_todo_submit" value="Add to List!"/>
      </form>
    </body>
  </html>

And then in __init__.py, we will connect the index page with that tempalte by
adding a decorator::

  from flask import render_template

  ...
  
  @app.route('/')
  def index():
    return render_template('hello.html')

Reload the page to see the changes.

Styling
-------
Because there are no styles by default, I will show you where and how we can add javascript, 
css, and othe image files.

Let's start by hooking up some styles. Since it's all the craze with kids these days, we will 
use twitters Bootstrap library.

First let's add the default styles to the top of hello.html. The firs link is hostted by twitter 
and the second link will be hosted by us::

  <head>
    <title>TODO at Noisebridge</title>
    <link rel="stylesheet" href="http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css"/>
    <link rel="stylesheet" href="/static/css/noiselist.css"/>
  </head>

Note that in this case, flask will be serving the css for us. In most cases of production 
deployment you will want to have your webserver do this. We will talk more about this in 
later classes.

Let's add a some directories for service static content (*must* be called static)::

  > mkdir static
  > mkdir static/css
  > mkdir static/javascript
  > mkdir static/images
  > touch static/css/noiselist.css 

Now let's add some styles to static/css/noiselist.css::

  footer{
    background-image: url(https://www.noisebridge.net/NB-logo-red-black-med.png);
    background-position: bottom right;
    background-repeat: no-repeat;
    min-height: 130px;
  }

  div.content{
    margin-top: 70px;
  }
  

This is just a basic logo that let's us know that we are serving up the correct content.

Let's update our front page to use bootstraps styles. For brevity I will just point to 
the raw source since its a lot. Update hello.html with the code at::

  https://raw.github.com/eleddy/flask-noiselist/d1137326c11cb908ddc6d59598913e439d5b1f83/src/noiselist/templates/hello.html

Reload and party.

Hooking up to Data
------------------
Flask passes arguments to the templating language just like web2 py does. To quickly 
pass in a list of items to display on the front page, update __init__.py to say::

  def index():
    todo_list = ["Watch TV",
             "Contemplate Work",
             "Go to Bed",
            ]
    return render_template('hello.html', todos=todo_list)

Then in hello.html we update the list to pull from the todos passed in::

    <h2>Current TODOs</h2>
    <ul>
      {% for todo in todos %}
         <li>{{ todo }}</li>
      {% endfor %}
    <ul>

Note the difference in syntax here with web2py. To end a loop we use "endfor" instead
of "pass". The = is not required to display a variable either.


The Database
------------


More Info
---------
 * Flask Documentation: http://flask.pocoo.org/docs/
 * About Jinja2: http://jinja.pocoo.org/docs/
 * Bootstrap: http://twitter.github.com/bootstrap/
 * For more info on this buildout itself, please see http://flask.pocoo.org/snippets/27/
