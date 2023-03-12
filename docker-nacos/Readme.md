# Docker Nacos

## Run

### Macbook M1
```bash
# Option 1) use M1 docker image
# https://hub.docker.com/r/zhusaidong/nacos-server-m1
# chttps://github.com/alibaba/nacos/issues/6340
docker pull zhusaidong/nacos-server-m1:2.0.3
docker run --name nacos-standalone -e MODE=standalone -e JVM_XMS=512m -e JVM_XMX=512m -e JVM_XMN=256m -p 8848:8848 -d zhusaidong/nacos-server-m1:2.0.3
```
## Ref
- https://blog.csdn.net/qq_41824075/article/details/121442865
- https://hub.docker.com/layers/zhusaidong/nacos-server-m1/2.0.3/images/sha256-ec4094306d61e286b201b282be11fcf1e300e29ca4878c6060c29bf4dfd84033
