
# Photon Heroku Realtime Webhooks Sample

## Summary

This is the **Photon Realtime Webhooks** sample using a Python 3 [Heroku](https://www.heroku.com/) application and [Heroku Postgres addon](https://addons.heroku.com/heroku-postgresql).

## Requirements
- Potentially any OS supported by Heroku (successfully tested on Ubuntu 13.10, may be problematic on Windows)
- [Photon Developer account](https://photonengine.com/)
- [Heroku account and Heroku Toolbelt installed](https://devcenter.heroku.com/articles/quickstart)

## Requirements for local development
- Local [PostgreSQL](http://www.postgresql.org/) server installed and running.
- [ngrok](https://ngrok.com/) to forward requests to your PC

## Setup and Run
- Refer to [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) and [Heroku Postgres article](https://devcenter.heroku.com/articles/heroku-postgresql) for detailed Heroku/Python/Flask/PostgreSQL application setup instructions.
### Essential steps are:
- $ `heroku login`
- $ `cd photon.webhooks.turnbased.heroku`
- $ `pipenv  install Flask gunicorn psycopg2`

### Running application locally
- $ `./ngrok http 5000` (default Flask port is 5000)
- go to the [Photon Dashboard](https://photonengine.com/en-US/Dashboard), create an application and set in the Webhooks tab the BaseUrl value to url from ngrok.
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
- go to the [Photon Dashboard](https://photonengine.com/en-US/Dashboard), create an application or choose already existing and set in the Webhooks tab the BaseUrl value to url of your Heroku web application (http://[Heroku application name].herokuapp.com).
- $ `heroku addons:create heroku-postgresql:hobby-dev`
- $ `heroku run python db_init.py` (script destroys current database if it exists and creates new one)
- $ `heroku ps:scale web=1`
- $ `heroku logs --tail`
- start client with appId set to your Photon application and check console for server logs