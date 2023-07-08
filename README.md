### This is preset to skip all the boring parts of creating a telegram bot.

To get started, simply fork the repository 

But, you will have to change the naming manually. 

### Initial setup
To do so, rename 2 directories called "ptb_mongo_docker_preset" to the name of your repo.

__*Important — they have to be named the same*__

Then change ["name", "packages include", "addopts", "mypy_path"] in pyproject.toml to the name of your repo.

And then change `ptb_mongo_docker_preset` in "commands" lines in tox.ini to the name of your repo.

### Poetry setup

Run `pip install poetry`

Run `poetry install`

Select poetry venv in your IDE

### .env setup
Create a file with the name .env in the project home directory, and add it there:

```
TG_BOT_TOKEN=your_tg_bot_token
MONGO_URI=your_mongo_db_uri
```
 
MONGO_URI is `mongodb://localhost:27017/` if you want to run locally

### Startup

To start the script, run `poetry run python ptb_mongo_docker_preset` inside of the project home directory.

### Commits

Before committing your code, run `pip install -r requirements_dev` inside of your venv. 

Run `tox` in your home project folder to run all tests before commit, or run them separately with:

`mypy your_repo_name` <br>
`pytest` <br>
`flake8`

### Server run

To run on the ubuntu server, install docker and nano. 

`nano restart.sh`
```
docker pull $DOCKER_IMAGE
docker stop tgbot
docker rm tgbot
docker run -d --restart on-failure --Log—opt mode=non-blocking --log-opt max-buffer-sizeIUm --log-opt max-file=5 --name tgbot --env-file .env $DOCKER_IMAGE
```
Exit

`nano .env` your env 

#### To update or initially run
`export DOCKER_IMAGE=` link to ghcr.io repo that GitHub will give you

`/bin/bash ./restart.sh`