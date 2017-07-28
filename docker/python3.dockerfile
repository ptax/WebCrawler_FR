FROM python:3.6.1

RUN apt-get update -y

RUN python -m pip install pymongo==3.4.0

RUN python -m pip install geopy==1.11.0

RUN pip3 install beautifulsoup4

RUN pip install pyyaml

RUN apt-get install -y python-matplotlib

WORKDIR /app

CMD ["sleep", "50d"]