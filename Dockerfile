#Version: 1.0
FROM python:3.7-stretch

SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && \
apt-get autoclean

WORKDIR /var/www/

ADD https://api.github.com/repos/smagiera/agenthelper/git/refs/heads/docker version.json
RUN git clone -b docker --single-branch https://github.com/smagiera/agenthelper.git

WORKDIR /var/www/agenthelper

RUN pip install -r requirements.txt

COPY startup.sh startup.sh

EXPOSE 80

#ENTRYPOINT ["python", "manage.py"]

#CMD ["runserver", "0.0.0.0:8000"]

CMD ./startup.sh

