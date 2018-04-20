FROM rasa/rasa_nlu

RUN apt-get update
RUN apt-get -y install build-essential
RUN apt-get -y install supervisor
RUN pip install rasa_core

COPY docker/supervisord.conf /etc/supervisor/supervisord.conf

RUN mkdir -p /chatbot
WORKDIR /chatbot

ENTRYPOINT []
#CMD python -m rasa_core.server -d models/dialogue -u models/nlu/default/current

CMD supervisord -n -c /etc/supervisor/supervisord.conf