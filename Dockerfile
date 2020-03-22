FROM python:3.7
MAINTAINER helios<i@shangyes.net>
ENV TimeZone=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TimeZone /etc/localtime && echo $TimeZone > /etc/timezone
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
EXPOSE 8316
RUN chmod +x ./run.sh
CMD ["/bin/bash", "./run.sh"]