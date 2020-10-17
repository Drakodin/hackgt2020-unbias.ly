# hackgt2020-aggr
Website code for a news aggregator and ranker based on language used.

## API
Written with Python as a Flask build.

Before beginning, initialize the venv by calling `python -m venv venv`. If the venv folder exists in the cloned repo, remove it first and reinstall.

Next, activate the venv. If you are on Windows, use `venv\Scripts\activate` from inside the `/api` directory. This starts the venv.

Then install the following: `pip install Flask cassandra-driver six python-dotenv`. Flask is the backend this uses. The next two are for using the DataStax Astra database. The last is for the use of `.env` file which allows for storing information in the full environment for use.

Included in the backend is a flask app file, `api.py` and an Astra schema `schema.cql` file.

## UI
Written in JS/TS with React.

This contains the `package.json` which means both of the following commands must be run from inside the `/ui` directory. When in development mode, open two terminals from the same location and call the following in each.

### `yarn start` or `npm start`
Runs the app in development mode at `localhost:3000`. Keep in mind that this project lacks a `yarn.lock` and `package-lock.json` so before anything can be called, please use `yarn install` or `npm install`.

### `yarn serve` or `npm serve`
Runs the api server (Flask) on at `localhost:5000`. However, there is no need for CORS as the ui has a proxy connection to the api.
