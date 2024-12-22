# GitLab Docker


## Run

```bash

#-------------------------------
# V1
#-------------------------------

# build
docker build -t custom-gitlab .

# run
docker run -d --name gitlab -p 80:80 -p 443:443 -p 22:22 custom-gitlab


#-------------------------------
# V2
#-------------------------------

# run with persistent data
docker run -d --name gitlab \
  -p 80:80 -p 443:443 -p 22:22 \
  -v gitlab_config:/etc/gitlab \
  -v gitlab_logs:/var/log/gitlab \
  -v gitlab_data:/var/opt/gitlab \
  custom-gitlab
```

## Ref
- https://vocus.cc/article/64673005fd89780001dedf45
- https://hackmd.io/@davidho9713/DevOps/https%3A%2F%2Fhackmd.io%2F%40davidho9713%2Fself_host_gitlab_setup