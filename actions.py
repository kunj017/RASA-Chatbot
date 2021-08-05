# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import urllib.request
import re
import webbrowser

from typing import Dict, Text, Any, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class ActionSong(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "form_song"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["song"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"song": [self.from_text()]}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(text="form is done")
        # dispatcher.utter_template('utter_submit', tracker)
        return []


def findYT(search):
    res = search
    # parse the query string
    query_string = urllib.parse.urlencode({"search_query": res})
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query_string)

    # using regular expression, get all the links
    search_results = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    # extract the first search result
    link = "http://www.youtube.com/watch?v=" + search_results[0]
    # printing the link captured in the action server terminal
    print("http://www.youtube.com/watch?v=" + search_results[0])

    # opening in the browser
    webbrowser.open(link, new=2)


# Custom action for Youtube Search functionality
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_YTSearch"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # extract the entities from the message
        # entities = tracker.latest_message['entities']
        # print(entities)
        query = ""
        query = tracker.get_slot("song")

        # if it contains a song name, extract it and save in query string
        # for e in entities:
        #     if e['entity'] == 'song':
        #         query = e['value']

        # if found call findYT method
        if len(query) == 0:
            dispatcher.utter_message(text="None found!")
            return []
        else:
            dispatcher.utter_message(text="Opening it in your default browser")
            findYT(query)

        dispatcher.utter_message(text="How do you feel now?!")

        return []
