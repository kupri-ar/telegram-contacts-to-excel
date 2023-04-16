#!/bin/bash

cd app

# Start the Docker Compose project in detached mode
docker-compose up -d --build

# Wait for the container to start
until docker-compose ps -q app | xargs docker inspect -f '{{.State.Running}}' | grep -q true; do
    sleep 1
done

echo Press Enter to continue...

# Attach to the container
docker attach $(docker-compose ps -q app)

# Down the Docker Compose project in detached mode
docker-compose down