# Metro API v2

Metro API v2 is an API for Metro's GTFS-RT data.

## Versioning

Metro API v2 uses a modified version of [Semantic Versioning](https://semver.org/), with major (`X`), minor(`x`), and hotfix(`*`) releases for the numbers respectively: `X.x.*`.

More versioning information can be found in [versioning.md](versioning.md)

## Getting started

### Prerequistes

- Docker installed

### Local Deployment

Install the repository locally. The application can be run directly or through a Docker container.

``` shell
# clone the repository
git clone https://github.com/LACMTA/metro_api_v2.git

# change to the directory
cd metro-api-v2
```

#### Environment Variables

Create a `.env` file with the required variables.

#### Running in Docker

Build the docker container and then run it.

``` shell
# creates image in current folder with tag nginx
docker build . -t metro-api-v2:metro-api-v2

# runs metro-api-v2 image
docker run --rm -it  -p 80:80/tcp metro-api-v2:metro-api-v2
```

???

``` shell
docker-compose stop -t 1
```

#### Running Locally

``` shell
# change to the API application directory
cd fastapi

# install the required libraries
pip3 install -r requirements.txt

# run uvicorn to serve the API
uvicorn app.main:app --reload --port 1212
```

Use this command to run uvicorn from Windows.

``` shell
python -m uvicorn app.main:app --reload 

# or

python3 -m uvicorn app.main:app --reload
```

### Run Data Service

``` shell
# change to the API application directory
cd data-loading-service
```


``` shell
# install the required libraries
pip3 install -r requirements.txt
```

Run the application

``` shell
# install the required libraries
python app

```
python main.py
```

### Misc Commands

``` shell
docker build -t metro-api-v2:metro-api-v2 .
docker compose up

docker tag metro-api-v2:metro-api-v2 albertkun/

metro-api-v2

docker push albertkun/metro-api-v2
```

### Debugging in VS Code

Go to `Run -> Open Configurations` and add this to the `launch.json` file:

``` js
{
    "name": "Python: Module",
    "type": "python",
    "request": "launch",
    "module": "uvicorn",
    "args": ["app.main:app", "--reload"],
    "justMyCode": true
}
```

This will tell the debugger to launch uvicorn as a python module, which is the equivalent of running `python -m uvicorn` in the terminal.  The `justMyCode` setting tells the debugger to only debug your code and not the included libraries.

To use this configuration, press `F1` or `ctrl-shift-P` and choose `Debug: Select and Start Debugging`.  From the list, select the `Python: Module` configuration.

## General Endpoint Naming Conventions

- All GTFS endpoints require an `agency_id`.
- If no specific value for a parameter is specified at the end, the endpoint will return all values for that parameter.

## Documentation

Visit [https://api.metro.net/docs/](https://api.metro.net/docs/)

### Editing the documentation

Install the packages

```bash
cd documentation
yarn install
```

Start the `dev` server.
```bash
yarn start 
```

The `cd` command changes the directory you're working with. In order to work with your newly created Docusaurus site, you'll need to navigate the terminal there.

The `yarn start` command builds your website locally and serves it through a development server, ready for you to view at http://localhost:3000/.

Open `docs/intro.md` (this page) and edit some lines: the site **reloads automatically** and displays your changes.

### Changes to the API Schema

When there are changes to the OpenAPI Schema in the API you will need to regenerate the documentation based on the json file by running the command:

```bash
cd documentation
yarn docusaurus clean-api-docs all
```