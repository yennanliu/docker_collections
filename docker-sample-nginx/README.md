# docker-sample-nginx
a sample nginx container to display container name

## cmd

```bash

# build
docker build -t my-nginx-image .

# run
# export 80 port to 8080
docker run -d -p 8080:80 --name my-nginx-container my-nginx-image


# restart
docker restart my-nginx-container
```