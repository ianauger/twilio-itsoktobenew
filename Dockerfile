FROM python:3.6.5
LABEL maintainer="ianauger@gmail.com"

WORKDIR /usr/src/app
COPY requirements.txt app.py texts.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./app.py" ]
