FROM python:3.6.1

RUN python -m pip install pymongo==3.4.0

RUN python -m pip install geopy==1.11.0