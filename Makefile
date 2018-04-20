build-dev:
	docker build -f dev.Dockerfile -t shoplo/chatbot .

stop:
	docker stop shoplo_bot || true
	docker rm shoplo_bot || true

run: stop
	docker run -d -p 5005:5005 --name=shoplo_bot -v `pwd`:/chatbot shoplo/chatbot

bash:
	docker exec -ti shoplo_bot bash

logs:
	docker logs -f shoplo_bot

learn:
	docker exec -ti shoplo_bot "supervisorctl -c /etc/supervisor/supervisord.conf restart all"
	docker exec -ti shoplo_bot "cd /chatbot && /usr/bin/python bot.py train-nlu"
	docker exec -ti shoplo_bot "cd /chatbot && /usr/bin/python bot.py train-dialogue"