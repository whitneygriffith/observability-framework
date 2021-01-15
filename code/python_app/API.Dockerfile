# set base image (host OS)
FROM python:3.9

# set the working directory in the container
WORKDIR /code

# copy the api app to the working directory
COPY api.py  .

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "./api.py" ]

# command to run on container start
CMD ["opentelemetry-instrument", "--exporter", "none", "--service-name", "jokes-api", "--ids-generator", "random", "gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "--threads", "2", "--worker-tmp-dir", "/dev/shm", "api:app"]
