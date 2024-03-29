from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings

from policy import OrderPolicy
from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.events import SlotSet
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.memoization import MemoizationPolicy

logger = logging.getLogger(__name__)


class OrderAPI(object):
    def search(self, info):
        return "Order status is new"


class ActionSearchOrder(Action):
    def name(self):
        return 'action_search_order'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("looking for order status")
        order_api = OrderAPI()
        orderStatus = order_api.search(tracker.get_slot("orderid"))
        SlotSet("order_status", orderStatus)
        return []

class ActionSuggest(Action):
    def name(self):
        return 'action_suggest'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("here's what I found:")
        dispatcher.utter_message(tracker.get_slot("order_status"))
        dispatcher.utter_message("is it ok for you? "
                                 "hint: I'm not going to "
                                 "find anything else :)")
        return []

def train_dialogue(domain_file="order_domain.yml",
                   model_path="models/dialogue",
                   training_data_file="data/babi_stories.md"):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(), OrderPolicy()])

    agent.train(
            training_data_file,
            max_history=3,
            epochs=400,
            batch_size=100,
            validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def train_nlu():
    from rasa_nlu.converters import load_data
    from rasa_nlu.config import RasaNLUConfig
    from rasa_nlu.model import Trainer

    training_data = load_data('data/franken_data.json')
    trainer = Trainer(RasaNLUConfig("nlu_model_config.json"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/', fixed_model_name="current")

    return model_directory


def run(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu/default/current")
    agent = Agent.load("models/dialogue", interpreter=interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")

    parser = argparse.ArgumentParser(
            description='starts the bot')

    parser.add_argument(
            'task',
            choices=["train-nlu", "train-dialogue", "run"],
            help="what the bot should do - e.g. run or train?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-nlu":
        train_nlu()
    elif task == "train-dialogue":
        train_dialogue()
    elif task == "run":
        run()
    else:
        warnings.warn("Need to pass either 'train-nlu', 'train-dialogue' or "
                      "'run' to use the script.")
        exit(1)