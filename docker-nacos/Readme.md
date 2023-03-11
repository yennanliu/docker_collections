# Docker Nacos

## Run
```bash
# Option 1) use M1 docker image
# https://hub.docker.com/r/zhusaidong/nacos-server-m1
# chttps://github.com/alibaba/nacos/issues/6340
docker pull zhusaidong/nacos-server-m1:2.0.3
docker run --name nacos-standalone -e MODE=standalone -e JVM_XMS=512m -e JVM_XMX=512m -e JVM_XMN=256m -p 8848:8848 -d zhusaidong/nacos-server-m1:2.0.3
```
