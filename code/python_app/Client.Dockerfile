# set base image (host OS)
FROM python:3.9

# set the working directory in the container
WORKDIR /code

# copy the client app to the working directory
COPY client.py  .

# copy the client html to the working directory
COPY templates/* ./templates/ 

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "./client.py" ]

# command to run on container start
CMD ["opentelemetry-instrument", "--exporter", "none", "--service-name", "jokes-client", "--ids-generator", "random", "gunicorn", "--bind", "0.0.0.0:5000", "--worker-tmp-dir", "/dev/shm", "client:app"]

