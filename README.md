# chatbot
Bot for shoplo chat

## Instalacja ( w niektórych wypadkach jest wymagana wersja pythona 3 )
* pip install rasa_core
* pip install rasa_nlu

w katalogu projektu uruchamiamy trenowanie:
* python bot.py train-nlu
* python bot.py train-dialogue

następnie odpalamy serwer:
```
python -m rasa_core.server -d models/dialogue -u models/nlu/default/current -o out.log | php
```

## Przykładowa konwersacja:
klient:
```
curl -XPOST localhost:5005/conversations/default/parse -d '{"query":"hey"}' | php

```
bot:
```
{"next_action": "utter_ask_howcanhelp", "tracker": {"sender_id": "default", "slots": {"order_status": null, "orderid": null, "userid": null}, "latest_message": {"intent": {"name": "greet", "confidence": 0.4908578205111868}, "entities": [], "intent_ranking": [{"name": "greet", "confidence": 0.4908578205111868}, {"name": "ask_status", "confidence": 0.21045089063419703}, {"name": "inform", "confidence": 0.17818117210904127}, {"name": "goodbye", "confidence": 0.12051011674557507}], "text": "hey"}, "latest_event_time": 1523015649.0471349, "paused": false, "events": null}} | php
```
klient:
```
curl -XPOST localhost:5005/conversations/default/continue -d '{"executed_action":"utter_ask_howcanhelp"}' | php
```
bot:
```
{"next_action": "action_listen", "tracker": {"sender_id": "default", "slots": {"order_status": null, "orderid": null, "userid": null}, "latest_message": {"intent": {"name": "greet", "confidence": 0.4908578205111868}, "entities": [], "intent_ranking": [{"name": "greet", "confidence": 0.4908578205111868}, {"name": "ask_status", "confidence": 0.21045089063419703}, {"name": "inform", "confidence": 0.17818117210904127}, {"name": "goodbye", "confidence": 0.12051011674557507}], "text": "hey"}, "latest_event_time": 1523015664.252301, "paused": false, "events": null}} | php
```
klient:
```
curl -XPOST localhost:5005/conversations/default/parse -d '{"query":"what is my order status"}' | php
```
bot:
```
{"next_action": "utter_ask_orderid", "tracker": {"sender_id": "default", "slots": {"order_status": null, "orderid": null, "userid": null}, "latest_message": {"intent": {"name": "ask_status", "confidence": 0.5080308894715004}, "entities": [], "intent_ranking": [{"name": "ask_status", "confidence": 0.5080308894715004}, {"name": "inform", "confidence": 0.27404960373137766}, {"name": "greet", "confidence": 0.11312741234977927}, {"name": "goodbye", "confidence": 0.10479209444734257}], "text": "what is my order status"}, "latest_event_time": 1523015709.127669, "paused": false, "events": null}} | php
curl -XPOST localhost:5005/conversations/default/continue -d '{"executed_action":"utter_ask_orderid"}' | php
{"next_action": "action_listen", "tracker": {"sender_id": "default", "slots": {"order_status": null, "orderid": null, "userid": null}, "latest_message": {"intent": {"name": "ask_status", "confidence": 0.5080308894715004}, "entities": [], "intent_ranking": [{"name": "ask_status", "confidence": 0.5080308894715004}, {"name": "inform", "confidence": 0.27404960373137766}, {"name": "greet", "confidence": 0.11312741234977927}, {"name": "goodbye", "confidence": 0.10479209444734257}], "text": "what is my order status"}, "latest_event_time": 1523015746.9243479, "paused": false, "events": null}} | php
```
klient:
```
curl -XPOST localhost:5005/conversations/default/parse -d '{"query":"my order number is 1001"}' | php
```
bot:
```
{"next_action": "utter_ack_dosearch", "tracker": {"sender_id": "default", "slots": {"order_status": null, "orderid": "1001", "userid": null}, "latest_message": {"intent": {"name": "inform", "confidence": 0.5780707119858551}, "entities": [{"start": 19, "end": 23, "value": "1001", "entity": "orderid", "extractor": "ner_crf"}], "intent_ranking": [{"name": "inform", "confidence": 0.5780707119858551}, {"name": "ask_status", "confidence": 0.22832907026652513}, {"name": "goodbye", "confidence": 0.11493486554941026}, {"name": "greet", "confidence": 0.07866535219820914}], "text": "my order number is 1001"}, "latest_event_time": 1523015770.321353, "paused": false, "events": null}} | php
curl -XPOST localhost:5005/conversations/default/continue -d '{"executed_action":"utter_ack_dosearch"}' | php
{"next_action": "action_search_order", "tracker": {"sender_id": "default", "slots": {"order_status": null, "orderid": "1001", "userid": null}, "latest_message": {"intent": {"name": "inform", "confidence": 0.5780707119858551}, "entities": [{"start": 19, "end": 23, "value": "1001", "entity": "orderid", "extractor": "ner_crf"}], "intent_ranking": [{"name": "inform", "confidence": 0.5780707119858551}, {"name": "ask_status", "confidence": 0.22832907026652513}, {"name": "goodbye", "confidence": 0.11493486554941026}, {"name": "greet", "confidence": 0.07866535219820914}], "text": "my order number is 1001"}, "latest_event_time": 1523015792.744116, "paused": false, "events": null}} | php
curl -XPOST localhost:5005/conversations/default/continue -d '{"executed_action":"action_search_order"}' | php
{"next_action": "action_suggest", "tracker": {"sender_id": "default", "slots": {"order_status": null, "orderid": "1001", "userid": null}, "latest_message": {"intent": {"name": "inform", "confidence": 0.5780707119858551}, "entities": [{"start": 19, "end": 23, "value": "1001", "entity": "orderid", "extractor": "ner_crf"}], "intent_ranking": [{"name": "inform", "confidence": 0.5780707119858551}, {"name": "ask_status", "confidence": 0.22832907026652513}, {"name": "goodbye", "confidence": 0.11493486554941026}, {"name": "greet", "confidence": 0.07866535219820914}], "text": "my order number is 1001"}, "latest_event_time": 1523015851.840822, "paused": false, "events": null}} | php
curl -XPOST localhost:5005/conversations/default/continue -d '{"executed_action":"action_suggest"}' | php
{"next_action": "action_listen", "tracker": {"sender_id": "default", "slots": {"order_status": null, "orderid": "1001", "userid": null}, "latest_message": {"intent": {"name": "inform", "confidence": 0.5780707119858551}, "entities": [{"start": 19, "end": 23, "value": "1001", "entity": "orderid", "extractor": "ner_crf"}], "intent_ranking": [{"name": "inform", "confidence": 0.5780707119858551}, {"name": "ask_status", "confidence": 0.22832907026652513}, {"name": "goodbye", "confidence": 0.11493486554941026}, {"name": "greet", "confidence": 0.07866535219820914}], "text": "my order number is 1001"}, "latest_event_time": 1523015869.9020958, "paused": false, "events": null}} | php
```
klient:
```
curl -XPOST localhost:5005/conversations/default/parse -d '{"query":"bye"}' | php
```
bot:
```
{"next_action": "utter_goodbye", "tracker": {"sender_id": "default", "slots": {"order_status": null, "orderid": "1001", "userid": null}, "latest_message": {"intent": {"name": "greet", "confidence": 0.5101045419610185}, "entities": [], "intent_ranking": [{"name": "greet", "confidence": 0.5101045419610185}, {"name": "ask_status", "confidence": 0.23772006185302055}, {"name": "inform", "confidence": 0.2376078927254182}, {"name": "goodbye", "confidence": 0.014567503460542593}], "text": "bye"}, "latest_event_time": 1523015909.7921789, "paused": false, "events": null}} | php
curl -XPOST localhost:5005/conversations/default/continue -d '{"executed_action":"utter_goodbye"}' | php
```
