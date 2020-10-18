# Unbias.ly
Website code for a news aggregator and ranker based on language used.

## API
Written with Python as a Flask build.

Before beginning, initialize the venv by calling `python -m venv venv`. If the venv folder exists in the cloned repo, remove it first and reinstall.

Next, activate the venv. If you are on Windows, use `venv\Scripts\activate` from inside the `/api` directory. This starts the venv.

Then install the following: `pip install Flask cassandra-driver six python-dotenv`. Flask is the backend this uses. The next two are for using the DataStax Astra database. The last is for the use of `.env` file which allows for storing information in the full environment for use.

Included in the backend is a flask app file, `api.py` and an Astra schema `schema.cql` file.

### ranker
Algorithm and related processes stored here. If you are not using Astra at the moment, import your functions to `api.py` and create the route there. Otherwise, create a datastore object blueprint and use that.

## UI
Written in JS/TS with React.

This contains the `package.json` which means both of the following commands must be run from inside the `/ui` directory. When in development mode, open two terminals from the same location and call the following in each.

### `yarn start` or `npm start`
Runs the app in development mode at `localhost:3000`. Keep in mind that this project lacks a `yarn.lock` and `package-lock.json` so before anything can be called, please use `yarn install` or `npm install`.

### `yarn serve` or `npm serve`
Runs the api server (Flask) on at `localhost:5000`. However, there is no need for CORS as the ui has a proxy connection to the api.

## ENVs
There is a `.env` required for both the front-end and back-end. This contains environment variables you will need for this occur. In the front-end, add `API_PORT=localhost:5000/` (this is development, this app was never formally deployed). In the backend, the `.env`, add your username and password as `ASTRA_USER` and `ASTRA_PASS`. To use the bundle zip, add your bundle to `/api`. For security reasons, those files and the security bundle for this project have been removed from this repository.


##Update: HackGT MLH Challenge Winner
