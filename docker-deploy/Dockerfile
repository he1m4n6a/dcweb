FROM vulhub/python:2.7

MAINTAINER he1m4n6a <he1m4n6a@163.com>

ADD requirements.txt /tmp/requirements.txt

ADD docker-entrypoint.sh /docker-entrypoint.sh

ADD sources.list /etc/apt/sources.list

ADD dcweb.zip /tmp/dcweb.zip

ADD https://bintray.com/jeremy-long/owasp/download_file?file_path=dependency-check-3.2.1-release.zip /tmp/dependency-check.zip

RUN	apt-get update \
	&& apt-get -y install unzip  \
	&& apt-get -y install default-jre \
	&& apt-get -y install default-jdk  \
	&& pip install -U -r /tmp/requirements.txt \
	&& chmod +x /docker-entrypoint.sh \
	&& cd /tmp \ 
	&& unzip dcweb.zip \
	&& mv dcweb / \
	&& unzip dependency-check.zip \
	&& mv dependency-check /dcweb

EXPOSE 8888

WORKDIR /dcweb

CMD ["/docker-entrypoint.sh"]
