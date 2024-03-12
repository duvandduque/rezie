FROM python:3.11.8-slim

# Copy local code to the container image.
ENV APP_HOME /app
ENV PORT 8080
WORKDIR $APP_HOME
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./
RUN export DOCKER_CLIENT_TIMEOUT=1800
RUN export COMPOSE_HTTP_TIMEOUT=1800
# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
EXPOSE 8080
CMD exec gunicorn --preload --worker-class uvicorn.workers.UvicornWorker --bind :$PORT --workers 1 --threads 8 --timeout 310 main:app
#