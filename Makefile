build-dev:
	docker build -f dev.Dockerfile -t shoplo/chatbot .

stop:
	docker stop shoplo_chatbot || true
	docker rm shoplo_chatbot || true
	
rm: stop
	docker rm shoplo_chatbot

run: stop
	docker run -d -p 5005:5005 --name=shoplo_chatbot -v `pwd`:/chatbot shoplo/chatbot

bash:
	docker exec -ti shoplo_chatbot bash

logs:
	docker logs -f shoplo_chatbot

learn:
	docker exec -ti shoplo_chatbot python bot.py train-nlu
	docker exec -ti shoplo_chatbot python bot.py train-dialogue
	docker exec shoplo_chatbot /usr/bin/supervisorctl restart all