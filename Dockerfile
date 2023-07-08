FROM python:3.10-alpine as python-base

# https://python-poetry.org/docs#ci-recommendations
ENV POETRY_VERSION=1.4.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
# Keep Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turn off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# where to place poetry cache and virtual environment
ENV POETRY_CACHE_DIR=/opt/.cache

# stage for Poetry installation
FROM python-base as poetry-base

# Creating a virtual environment just for poetry and install it with pip
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# stage from the base python image
FROM python-base as bot-app

# Copy Poetry to bot-app image
COPY --from=poetry-base ${POETRY_VENV} ${POETRY_VENV}

# Add Poetry to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

# Copy Dependencies
COPY poetry.lock pyproject.toml ./ptb_mongo_docker_preset/

#set working directory
WORKDIR /ptb_mongo_docker_preset

# [OPTIONAL] Validate the project is properly configured
RUN poetry check

# Install Dependencies with --no-root
RUN poetry install --no-root --no-interaction --no-cache --without dev

# Copy Application
COPY . .

#run the application
WORKDIR /ptb_mongo_docker_preset/ptb_mongo_docker_preset
CMD ["ls", "-a"]
CMD [ "poetry", "run", "python", "__main__.py"]