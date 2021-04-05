FROM python:3

WORKDIR /docker_web_app

ADD . /docker_web_app

RUN pip install -r requirement.txt

EXPOSE 5000

CMD ["python","app.py"]
