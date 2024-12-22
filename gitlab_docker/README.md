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