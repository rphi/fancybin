FROM python:3.7
EXPOSE 8000

VOLUME ["/srv/static"]

RUN apt-get update \
    && apt-get install -y npm python-psycopg2 \
    && apt-get clean

RUN npm install -g yarn

WORKDIR /srv/fancybin
ADD requirements.txt /srv/fancybin
RUN pip install -r requirements.txt

ADD package.json /srv/fancybin
ADD yarn.lock /srv/fancybin
RUN yarn install
ADD yarn-build-prod.sh /srv/fancybin
ADD static/src /srv/fancybin/static/src
RUN yarn build-prod

ADD . /srv/fancybin
ENTRYPOINT ["bash", "/srv/fancybin/start.sh"]
