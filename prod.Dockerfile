FROM rasa/rasa_nlu

RUN apt-get update
RUN apt-get -y install build-essential

WORKDIR /chatbot
#COPY ./requirements.txt ./
#RUN pip install -r requirements.txt
RUN pip install rasa_core
#RUN pip install rasa_nlu


COPY ./ ./

RUN python bot.py train-nlu
RUN python bot.py train-dialogue

ENTRYPOINT []
CMD python -m rasa_core.server -d models/dialogue -u models/nlu/default/current