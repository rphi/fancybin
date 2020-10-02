FROM python:3.8-buster
EXPOSE 8000

VOLUME ["/srv/static"]

RUN apt-get update \
    && apt-get install -y python-psycopg2 \
    && apt-get clean

WORKDIR /srv/fancybin
ADD requirements.txt /srv/fancybin
RUN pip install -r requirements.txt

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y yarn npm

ADD package.json /srv/fancybin
ADD yarn.lock /srv/fancybin
RUN yarn install
ADD yarn-build-prod.sh /srv/fancybin
ADD static/src /srv/fancybin/static/src
RUN yarn build-prod

ADD . /srv/fancybin
ENTRYPOINT ["bash", "/srv/fancybin/start.sh"]
