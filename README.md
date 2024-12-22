# Docker Playground
> personal docker backup

## Useful cmd

- https://github.com/yennanliu/utility_shell/blob/master/docker/docker_commands.sh#L4

```bash
# 9) REMOVE --------------------------
# Remove all containers
docker rm -f $(docker ps -aq)
# Remove all images
docker rmi -f $(docker images -q)
# remove all containers in docker
docker rm -f $(docker ps -a -q)
# remove all images in docker
docker rmi -f $(docker images -q -a)
# clean docker cache : https://stackoverflow.com/questions/65405562/is-there-a-way-to-clean-docker-build-cache
docker builder prune
```
