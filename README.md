
# Photon Heroku Turnbased Webhooks Sample

## Summary

This is the **Photon Turnbased Webhooks** sample using [Heroku](https://www.heroku.com/) and [Heroku Postgres addon](https://addons.heroku.com/heroku-postgresql).

## Requirements
- Potentially any OS supported by Heroku (successfully tested on Ubuntu 13.10, may be problematic on Windows)
- [Photon Developer account](https://dev-cloud.exitgames.com/)
- [Heroku account and Heroku Toolbelt installed](https://devcenter.heroku.com/articles/quickstart)

## Requirements for local development
- Local [PostgreSQL](http://www.postgresql.org/) server installed and running.
- [ngrok](https://ngrok.com/) to forward requests to your PC

## Setup and Run
- Refer to [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) and [Heroku Postgres article](https://devcenter.heroku.com/articles/heroku-postgresql) for detailed Heroku/Python/Flask/PostgreSQL application setup instructions.
### Essential steps are:
- $ `heroku login`
- $ `mkdir photon-turnbased`
- $ `cd photon-turnbased`
- $ `virtualenv venv`
- $ `source venv/bin/activate`
- $ `pip install Flask gunicorn psycopg2`
- copy this repository content to 'photon-turnbased' folder

### Running application locally
- $ `./ngrok 5000` (default Flask port is 5000)
- go to the [Photon Dashboard](https://dev-cloud.exitgames.com/en/Turnbased/Dashboard), create an application and set in the Webhooks tab the BaseUrl value to url from ngrok.
- $ `export DATABASE_URL=[local PostgreSQL database url]`
- $ `python db_init.py` (script destroys current database if it exists and creates new one)
- $ `foreman start`
- start client with appId set to your Photon application and check console for server logs

### Deploying to Heroku Cloud and run
- $ `git init`
- $ `git add .`
- $ `git commit -m "init"`
- $ `heroku create [new Heroku application name]`
- $ `git push heroku master`
- go to the [Photon Dashboard](https://dev-cloud.exitgames.com/en/Turnbased/Dashboard), create an application or choose already existing and set in the Webhooks tab the BaseUrl value to url of your Heroku web application (http://[Heroku application name].herokuapp.com).
- $ `heroku addons:add heroku-postgresql:dev`
- $ `heroku pg:promote HEROKU_POSTGRESQL_COLOR_URL` (replace with your database color url)
- $ `heroku run python db_init.py` (script destroys current database if it exists and creates new one)
- $ `heroku ps:scale web=1`
- $ `heroku logs --tail`
- start client with appId set to your Photon application and check console for server logs