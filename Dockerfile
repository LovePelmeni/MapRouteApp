ARG arch=amd64
# / * There is some issues with SCRAM Authentication on Postgresql on M1 Chip.
FROM --platform=linux/${arch} python:3.8.13-buster
MAINTAINER Klimushin Kirill, Email: kirklimushin@gmail.com

RUN echo "Building Project Docker Application Image...  It will Take some time."
CMD mkdir /project/dir/
WORKDIR /project/dir/

ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
COPY . .

RUN pip install -r requirements.txt
RUN pip install psycopg2-binary --no-input --no-cache-dir
RUN pip install gunicorn
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["sh", "./entrypoint.sh"]



