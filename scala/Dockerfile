FROM srdc/java:oraclejdk-8
MAINTAINER SRDC Ltd. <technical@srdc.com.tr>

#Install Scala
ENV SCALA_VERSION 2.11.7

RUN curl -sL http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz | gunzip | tar -x -C /usr/local
RUN cd /usr/local && ln -s ./scala-$SCALA_VERSION scala
ENV SCALA_HOME  /usr/local/scala
ENV PATH ${PATH}:${SCALA_HOME}/bin

#Install SBT
ENV SBT_VERSION 0.13.9

ENV SBT_HOME /usr/local/sbt
ENV PATH ${PATH}:${SBT_HOME}/bin
RUN curl -sL http://dl.bintray.com/sbt/native-packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz | gunzip | tar -x -C /usr/local
RUN cd /usr/local && ln -s ./sbt-$SBT_VERSION sbt
RUN echo "-scala-home /usr/local/scala" ${SBT_HOME}/conf/sbtopts

CMD ["bash"]