# Python: Getting Started

A barebones Django app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Prepare the app
`$ git clone https://github.com/heroku/python-getting-started.git` <directory to save to, if not specified it goes to where ever you are cd>
`$ cd python-getting-started`

## Deploy the app
`$ heroku create`
`$ git push heroku master`

## Check app instance
`$ heroku ps:scale web=1`

## Open app
`$ heroku open`

## View logs
`heroku logs --tail`
- Control + C to stop viewing logs

## Define a Procfile
Example file looks like:

`web: gunicorn gettingstarted.wsgi --log-file -`

This declares a single process type, web, and the command needed to run it. The name web is important here. It declares that this process type will be attached to the HTTP routing stack of Heroku, and receive web traffic when deployed.

Procfiles can contain additional process types. For example, you might declare one for a background worker process that processes items off of a queue.

Microsoft Windows version file: Procfile.windows

Has content:

`web: python manage.py runserver 0.0.0.0:5000`

## Scale the app
Check the number of dynos running using:

`$ heroku ps`

Scale down:

`$ heroku ps:scale web=0`

Scale up from 0:

`$ heroku ps:scale web=1`

## Declare app dependencies
This requires Postgres installed to properly work.

`$ pip install -r requirements.txt`

Check pip's feature list:

`$ pip list`

## Run the app locally
The app is almost ready to start locally. Django uses local assets, so first, you’ll need to run collectstatic:

`$ python manage.py collectstatic`

Respond with “yes”.

Now start your application locally using `heroku local`, which was installed as part of the Heroku CLI.

If you’re on Microsoft Windows system, run this:

`heroku local web -f Procfile.windows`

If you’re on a Unix system, just use the default Procfile by running:

`heroku local web`

Your local web server will then start up:

[OKAY] Loaded ENV .env File as KEY=VALUE Format
2:28:11 PM web.1 |  [2018-10-12 14:28:11 -0500] [18712] [INFO] Starting gunicorn 19.9.0
2:28:11 PM web.1 |  [2018-10-12 14:28:11 -0500] [18712] [INFO] Listening at: http://0.0.0.0:5000 (18712)
2:28:11 PM web.1 |  [2018-10-12 14:28:11 -0500] [18712] [INFO] Using worker: sync
2:28:11 PM web.1 |  [2018-10-12 14:28:11 -0500] [18715] [INFO] Booting worker with pid: 18715

Just like Heroku, `heroku local` examines the `Procfile` to determine what to run.

Open `http://localhost:5000` with your web browser. You should see your app running locally.

To stop the app from running locally, go back to your terminal window and press Ctrl+C to exit.

## Push local changes

`$ pip install requests`

And then add it to your `requirements.txt` file:

`django` <br>
`gunicorn` <br>
`django-heroku` <br>
`requests` <br>

Modify hello/views.py so that it imports the requests module at the start:

`import requests`

Now modify the `index` method to make use of the module. Try replacing the current `index` method with the following code:

`def index(request):` <br>
    `r = requests.get('http://httpbin.org/status/418')` <br>
    `print(r.text)` <br>
    `return HttpResponse('<pre>' + r.text + '</pre>')` <br>
    
Now test locally:

`heroku local`

Visit your application at http://localhost:5000. You should now see the output of fetching http://httpbin.org/status/418, which is a lovely teapot:

    -=[ teapot ]=-

       _...._
     .'  _ _ `.
    | ."` ^ `". _,
    \_;`"---"`|//
      |       ;/
      \_     _/
        `"""`
Now deploy. Almost every deploy to Heroku follows this same pattern. First, add the modified files to the local git repository:

`git add .`

Now commit the changes to the repository:

`git commit -m "Demo"`

Now deploy, just as you did previously:

`git push heroku master`

Finally, check that everything is working:

`heroku open`

## Provision add-ons
Add-ons are third-party cloud services that provide out-of-the-box additional services for your application, from persistence through logging to monitoring and more.

By default, Heroku stores 1500 lines of logs from your application. However, it makes the full log stream available as a service - and several add-on providers have written logging services that provide things such as log persistence, search, and email and SMS alerts.

In this step you will provision one of these logging add-ons, Papertrail.

Provision the papertrail logging add-on:

`$ heroku addons:create papertrail`

To help with abuse prevention, provisioning an add-on requires account verification. If your account has not been verified, you will be directed to visit the verification site.

The add-on is now deployed and configured for your application. You can list add-ons for your app like so:

`$ heroku addons`

To see this particular add-on in action, visit your application’s Heroku URL a few times. Each visit will generate more log messages, which should now get routed to the papertrail add-on. Visit the papertrail console to see the log messages:

`$ heroku addons:open papertrail`

## Start a console

`$ heroku run python manage.py shell`

or run bash

`$ heroku run bash`

## Define config vars

Edit `hello/views.py`. At the beginning, add a line to import the `os` module:

`$ import os`

Now modify the `index` method so that it repeats an action depending on the value of the `TIMES` environment variable:

`def index(request):`<br>
    `times = int(os.environ.get('TIMES',3))`<br>
    `return HttpResponse('Hello! ' * times)`<br>

`heroku local` will automatically set up the environment based on the contents of the `.env` file in your local directory. In the top-level directory of your project there is already a `.env` file that has the following contents:

If you run the app with `heroku local`, you’ll see two “Hello!”’s.

To set the config var on Heroku, execute the following:

`$ heroku config:set TIMES=2`

View the config vars that are set using heroku config:

`$ heroku config`

Deploy your changed application to Heroku to see this in action.

## Provision a database

The add-on marketplace has a large number of data stores, from Redis and MongoDB providers, to Postgres and MySQL. In this step you will learn about the free Heroku Postgres add-on that was automatically provisioned when your app was deployed.

A database is an add-on, and so you can find out a little more about the database provisioned for your app using the `addons` command in the CLI:

`$ heroku addons`

Listing the config vars for your app will display the URL that your app is using to connect to the database, DATABASE_URL:

`$ heroku config`

Heroku also provides a pg command that shows a lot more details:

`$ heroku pg`

This indicates I have a hobby database (free), running Postgres 10.5, with no data.

The example app you deployed already has database functionality, which you should be able to reach by visiting your app’s URL and appending `/db`. For example, if your app was deployed to `https://wonderful-app-287.herokuapp.com/` then visit `https://wonderful-app-287.herokuapp.com/db`.

Accessing it will yield an error though, because while the database is configured, the tables have not been created. Run the standard Django `manage.py migrate` to create the tables.

`$ heroku run python manage.py migrate`

If you see a message that says, “You just installed Django’s auth system, which means you don’t have any superusers defined. Would you like to create one now?”, type `no`.

Now access the `/db` route again and you’ll see a simple page update every time you access it:

`Page View Report` <br>
`April 19, 2017, 8:50 a.m.` <br>
`April 19, 2017, 8:52 a.m.` <br>

The code to access the database is straightforward, and makes use of a simple Django model called `Greetings` that you can find in `hello/models.py`.

Whenever you visit the `/db` route of your app, the following method in the hello/views.py file is invoked which creates a new Greeting and then renders all the existing Greetings:

    def db(request):
    
        greeting = Greeting()
        greeting.save()
    
        greetings = Greeting.objects.all()
    
        return render(request, 'db.html', {'greetings': greetings})

Assuming that you have Postgres installed locally, use the `heroku pg:psql` command to connect to the remote database and see all the rows:

`$ heroku pg:psql`

## Running Locally V2

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/heroku/python-getting-started.git
$ cd python-getting-started

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
