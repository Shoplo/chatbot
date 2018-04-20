FROM rasa/rasa_nlu

RUN apt-get update
RUN apt-get -y install build-essential
RUN pip install rasa_core

RUN mkdir -p /chatbot
WORKDIR /chatbot

COPY . .

RUN python bot.py train-nlu
RUN python bot.py train-dialogue

ENTRYPOINT []
CMD python -m rasa_core.server -d models/dialogue -u models/nlu/default/current
