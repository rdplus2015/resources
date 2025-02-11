# Docker

### Installation (Docker engine or Docker Desktop) 

- [Installation](https://docs.docker.com/engine/install/ubuntu/)
- [Documentation](https://docs.docker.com/)
```sh
docker --version  # Check Docker Version
sudo systemctl start docker  # Start Docker Service
sudo systemctl enable docker  # Enable Docker Service
```

## Working with Docker Images

```sh
# List Available Images
docker images  

# Pull an Image
docker pull ubuntu:latest

# Push an image 
docker push username/monimage:1.0 

#  Build an Image from Dockerfile
docker build -t myimage:1.0 . 

# Example with a build argument
docker build --build-arg NODE_ENV=production -t myimage:latest .

# Tag an Image
docker tag myimage:1.0 myrepo/myimage:latest

# Remove an Image 
docker rmi myimage  
```
## Dockerfile 

```bash
## 1. Define the base image
FROM python:3.8-slim 

## 2. Set the working directory inside the container
WORKDIR /app

## 3. Install dependencies during the image build
COPY requirements.txt .
RUN pip install -r requirements.txt

## 4. Copy the project files into the working directory
COPY flask-demo/ .  

## 5. Inform that the application will use port 5000 inside the container
EXPOSE 5000 

## 6. Define the command to run when the container starts
CMD [ "python", "app.py" ]
```

## Working with Containers


```sh
docker ps  ## List Running Containers
docker ps -a  ## List All Containers (Including Stopped Ones)
```

```sh
# Run a container 
docker run my-python-app :latest 

# The -v flag in the docker run command is used to mount a volume (which can be a file or directory) from your local machine (host) into the container.

# any changes made to the files in /home/user/python-app on your host machine will automatically be reflected inside the container in the /app directory (and vice versa). 
docker run -v /home/user/python-app:/app my-python-app:latest 

#interactively run a container with a terminal session
docker run -it --name mycontainer ubuntu:latest /bin/bash

# Run a Container in detached Mode instead of attaching to the terminal.
docker run -d --name mycontainer ubuntu:latest

# View Logs of a Container 
docker logs mycontainer

# Execute a Command 
docker exec -it mycontainer /bin/bash ls -l /app in a Running Container

# Restart a Container
docker restart mycontainer

# Stop a Running Container
docker stop mycontainer

# Remove a Container 
docker rm mycontainer 
```

## Networking in Docker

```sh
# List Networks
docker network ls

# Create a Network
docker network create mynetwork

# Create a network with a specific driver
# bridge: This is the default network mode, which isolates the container.
# Host: The container shares the network stack with the host system.
# None: No networking. You manage the networking manually.
docker network create --driver bridge my-network 

# Connect a Container to a Network
docker network connect mynetwork mycontainer

# Disconnect a Container from a Network
docker network disconnect mynetwork mycontainer

# commande example 
docker run --network my-network \
-p 4000:4000 \
--name ecommerce-ui \
-e REACT_APP_PROFILE_API_HOST=http://profile-management \
-e REACT_APP_SHIPPING_API_HOST=http://shipping-and-handling \
ecommerce-ui

```

## Working with Volumes

```sh
# List Volumes
docker volume ls

# Create a Volume
docker volume create myvolume

# Use a Volume in a Container
docker run -d -v myvolume:/data --name mycontainer ubuntu:latest

# Remove a Volume
docker volume rm myvolume
```

## Docker Compose

### Example `docker-compose.yml`

```yaml
version: '3.8'

services:
  ecommerce-ui:
    image: ecommerce-ui:1.0.0
    container_name: ecommerce-ui
    ports:
      - "4000:4000"
    environment:
      - REACT_APP_PROFILE_API_HOST=http://profile-management
      - REACT_APP_SHIPPING_API_HOST=http://shipping-and-handling
    depends_on:
      - profile-management
      - shipping-and-handling

  shipping-and-handling:
    image: shipping-and-handling:1.0.0
    container_name: shipping-and-handling
    ports:
      - "8080:8080"
    depends_on:
      - mongodb-shipping
    environment:
      - MONGO_URI=mongodb://mongodb-shipping:27017

  mongodb-shipping:
    image: mongo
    container_name: mongodb-shipping
    ports:
      - "27020:27017"
    volumes:
      - mongodb_shipping_data:/data/db

  profile-management:
    image: profile-management:1.0.0
    container_name: profile-management
    depends_on:
      - mysql-profile-management
    ports:
      - "3003:3003"
    environment:
      - MYSQL_HOST=mysql-profile-management
      - MYSQL_PORT=3306
      - MYSQL_DATABASE=profile_management
      - MYSQL_USER=profile_user
      - MYSQL_PASSWORD=profile_password

  mysql-profile-management:
    image: mysql:8.0
    container_name: mysql-profile-management
    environment:
      - MYSQL_DATABASE=profile_management
      - MYSQL_USER=profile_user
      - MYSQL_PASSWORD=profile_password
      - MYSQL_ROOT_PASSWORD=root_password
    volumes:
      - mysql_profile_management_data:/var/lib/mysql

volumes:
  mongodb_shipping_data:
  mysql_profile_management_data:
```

```sh
docker-compose up -d # Run a Compose Stack
docker-compose down # Stop Compose Stack
```
```sh
# used to clean up unused Docker resources, including containers, images, networks, and volumes.
docker system prune -a 

# View general Docker system information
docker info

# View detailed information about a specific container
docker inspect <container_name_or_id>

```

## 7. Docker Best Practices

- Use `.dockerignore` to exclude unnecessary files.
- Minimize image size by using Alpine-based images.
- Use multi-stage builds to keep images clean.
- Keep containers stateless and use volumes for data persistence.
- Use labels for metadata and better organization.
