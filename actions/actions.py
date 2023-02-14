import pprint
from actions import custom_reply, weatherapis
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset, FollowupAction
import random


class ActionGivingReport(Action):

    def name(self) -> Text:
        return "action_giving_report"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        print("==============================================================")
        pprint.pprint(tracker.latest_message)
        pprint.pprint(tracker.get_intent_of_latest_message())
        print("==============================================================")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        pprint.pprint(tracker.current_slot_values())
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        return []


class ActionDebugging(Action):

    def name(self) -> Text:
        return "action_debugging"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        print("IN\nDEBUGGING\nACTION\n______\n________\n______")
        pprint.pprint(tracker.__dict__)
        print("==============================================================")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        pprint.pprint(tracker.current_slot_values())
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("IN\nDEBUGGING\nACTION\n______\n________\n______")
        return []


class ActionGreetWelcome(Action):
    def name(self) -> Text:
        return "action_greet_welcome"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=random.choice(custom_reply.greet_welcome_message))
        return []


class ActionGetTheLocation(Action):
    def name(self) -> Text:
        return "action_get_the_location"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=random.choice(custom_reply.get_the_location_message))
        return []


class ActionGreetGetTheLocation(Action):
    def name(self) -> Text:
        return "action_greet_get_the_location"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=random.choice(custom_reply.greet_get_the_location_message))
        return []


class ActionExplainToWhy(Action):
    def name(self) -> Text:
        return "action_explain_to_why"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=random.choice(custom_reply.explain_to_why_message))
        return []


class ActionExplainToDeny(Action):
    def name(self) -> Text:
        return "action_explain_to_deny"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=random.choice(custom_reply.explain_to_deny_message))
        return []


class ActionExplainToCurrentLocation(Action):
    def name(self) -> Text:
        return "action_explain_to_current_location"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=random.choice(custom_reply.explain_to_current_location_message))
        return []


class ActionAgainAskForLocation(Action):
    def name(self) -> Text:
        return "action_again_ask_for_location"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=random.choice(custom_reply.again_ask_for_location_message))
        return []


class ActionDidThatHelp(Action):
    def name(self) -> Text:
        return "action_did_that_help"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=random.choice(custom_reply.did_that_help_message))
        return []


class ActionReplyForAvailability(Action):
    def name(self) -> Text:
        return "action_reply_for_availability"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=random.choice(custom_reply.reply_for_availability))
        return []


class ActionHappy(Action):
    def name(self) -> Text:
        return "action_happy"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=random.choice(custom_reply.happy_message))
        return []


class ActionProceedFurther(Action):
    def name(self) -> Text:
        return "action_proceed_further"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=random.choice(custom_reply.proceed_further_message))
        return []


class ActionGoodbye(Action):
    def name(self) -> Text:
        return "action_goodbye"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=random.choice(custom_reply.goodbye_message))
        return []


class ActionIamBot(Action):
    def name(self) -> Text:
        return "action_iamabot"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=random.choice(custom_reply.iamabot_message))
        return []


class ActionSlotsValues(Action):
    def name(self) -> Text:
        return "action_slots_values"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=random.choice(custom_reply.slots_values_message))
        return []


class ActionAboutRasa(Action):
    def name(self) -> Text:
        return "action_about_rasa"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=random.choice(custom_reply.about_rasa_message))
        return []


class ActionSeeYouAgain(Action):

    def name(self) -> Text:
        return "action_see_you_again"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Rasa is amazing to work on!"
                                      "\nSee you again at Weather🌄Bot🤖")

        return []


class ActionHandlingOutOfScopeDefault(Action):

    def name(self) -> Text:
        return "action_handling_out_of_scope_default"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        default_counter = tracker.get_slot('oos_counter_default')
        default_counter += 1
        if default_counter <= 3:
            print(f"In default {default_counter}: ", tracker.get_slot('location_slot'))
            dispatcher.utter_message(text=random.choice(custom_reply.oos_default_reply))
            return [SlotSet(key='oos_counter_default', value=default_counter), SlotSet(key='location_slot', value=None)]
        elif default_counter == 4:
            print("In default 4: ", tracker.get_slot('location_slot'))
            dispatcher.utter_message(text=random.choice(custom_reply.main_last_message))
            dispatcher.utter_message(text=random.choice(custom_reply.fresh_start_reply))
            return [AllSlotsReset()]


class ActionHandlingOutOfScopeRephrase(Action):

    def name(self) -> Text:
        return "action_handling_out_of_scope_rephrase"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        else_counter = tracker.get_slot('oos_counter_else')
        else_counter += 1
        if else_counter <= 3:
            print(f"In rephrase {else_counter}: ", tracker.get_slot('location_slot'))
            dispatcher.utter_message(text=random.choice(custom_reply.oos_rephrase_reply))
            return [SlotSet(key='oos_counter_else', value=else_counter), SlotSet(key='location_slot', value=None)]
        elif else_counter == 4:
            print("In rephrase 4: ", tracker.get_slot('location_slot'))
            dispatcher.utter_message(text=random.choice(custom_reply.main_last_message))
            dispatcher.utter_message(text=random.choice(custom_reply.fresh_start_reply))
            return [AllSlotsReset()]


class ActionHandlingOutOfScopeFood(Action):

    def name(self) -> Text:
        return "action_handling_out_of_scope_food"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        else_counter = tracker.get_slot('oos_counter_else')
        else_counter += 1
        if else_counter <= 3:
            print(f"In food {else_counter}: ", tracker.get_slot('location_slot'))
            dispatcher.utter_message(text=random.choice(custom_reply.oos_food_reply))
            return [SlotSet(key='oos_counter_else', value=else_counter), SlotSet(key='location_slot', value=None)]
        elif else_counter == 4:
            print("In food 4: ", tracker.get_slot('location_slot'))
            dispatcher.utter_message(text=random.choice(custom_reply.main_last_message))
            dispatcher.utter_message(text=random.choice(custom_reply.fresh_start_reply))
            return [AllSlotsReset()]


class ActionHandlingOutOfScopeMath(Action):

    def name(self) -> Text:
        return "action_handling_out_of_scope_math"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        else_counter = tracker.get_slot('oos_counter_else')
        else_counter += 1
        if else_counter <= 3:
            print(f"In math {else_counter}: ", tracker.get_slot('location_slot'))
            dispatcher.utter_message(text=random.choice(custom_reply.oos_math_reply))
            return [SlotSet(key='oos_counter_else', value=else_counter), SlotSet(key='location_slot', value=None)]
        elif else_counter == 4:
            print("In math 4: ", tracker.get_slot('location_slot'))
            dispatcher.utter_message(text=random.choice(custom_reply.main_last_message))
            dispatcher.utter_message(text=random.choice(custom_reply.fresh_start_reply))
            return [AllSlotsReset()]


class ActionHandlingOutOfScopeVehicle(Action):

    def name(self) -> Text:
        return "action_handling_out_of_scope_vehicle"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        else_counter = tracker.get_slot('oos_counter_else')
        else_counter += 1
        if else_counter <= 3:
            print(f"In vehicle {else_counter}: ", tracker.get_slot('location_slot'))
            dispatcher.utter_message(text=random.choice(custom_reply.oos_vehicle_reply))
            return [SlotSet(key='oos_counter_else', value=else_counter), SlotSet(key='location_slot', value=None)]
        elif else_counter == 4:
            print("In vehicle 4: ", tracker.get_slot('location_slot'))
            dispatcher.utter_message(text=random.choice(custom_reply.main_last_message))
            dispatcher.utter_message(text=random.choice(custom_reply.fresh_start_reply))
            return [AllSlotsReset()]


class ActionHandlingOutOfScopePersonal(Action):

    def name(self) -> Text:
        return "action_handling_out_of_scope_personal"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        else_counter = tracker.get_slot('oos_counter_else')
        else_counter += 1
        if else_counter <= 3:
            print(f"In personal {else_counter}: ", tracker.get_slot('location_slot'))
            dispatcher.utter_message(text=random.choice(custom_reply.oos_personal_reply))
            return [SlotSet(key='oos_counter_else', value=else_counter), SlotSet(key='location_slot', value=None)]
        elif else_counter == 4:
            print("In personal 4: ", tracker.get_slot('location_slot'))
            dispatcher.utter_message(text=random.choice(custom_reply.main_last_message))
            dispatcher.utter_message(text=random.choice(custom_reply.fresh_start_reply))
            return [AllSlotsReset()]


class ActionHandlingOutOfScopeErrorSentence(Action):

    def name(self) -> Text:
        return "action_handling_out_of_scope_error_sentence"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        fallback_count = tracker.get_slot('fallback_counter')
        fallback_count += 1
        if fallback_count <= 3:
            print(f"In fallback_rephrase {fallback_count}: ", tracker.get_slot('location_slot'))
            dispatcher.utter_message(text=random.choice(custom_reply.oos_fallback_rephrase_reply))
            return [SlotSet(key='fallback_counter', value=fallback_count), SlotSet(key='location_slot', value=None)]
        elif fallback_count == 4:
            print("In fallback_rephrase 4: ", tracker.get_slot('location_slot'))
            dispatcher.utter_message(text=random.choice(custom_reply.main_last_message))
            dispatcher.utter_message(text=random.choice(custom_reply.fresh_start_reply))
            return [AllSlotsReset()]


class ActionHandlingOutOfScopeErrorLocation(Action):

    def name(self) -> Text:
        return "action_handling_out_of_scope_error_location"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        fallback_count = tracker.get_slot('fallback_counter')
        fallback_count += 1
        if fallback_count <= 3:
            print(f"In fallback_rephrase {fallback_count}: ", tracker.get_slot('location_slot'))
            dispatcher.utter_message(text=random.choice(custom_reply.oos_fallback_rephrase_reply))
            return [SlotSet(key='fallback_counter', value=fallback_count), SlotSet(key='location_slot', value=None)]
        elif fallback_count == 4:
            print("In fallback_rephrase 4: ", tracker.get_slot('location_slot'))
            dispatcher.utter_message(text=random.choice(custom_reply.main_last_message))
            dispatcher.utter_message(text=random.choice(custom_reply.fresh_start_reply))
            return [AllSlotsReset()]


class ActionLocationConformation(Action):
    def name(self) -> Text:
        return "action_location_validation_and_conformation"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        resolved_address = weatherapis.finding_location(call_location=tracker.get_slot('location_slot'))
        # resolved_address = 'Porbandar, Gujarat, India'
        if resolved_address is not None:
            buttons = [{'title': f'{random.choice(custom_reply.affirm_buttons)}', 'payload': '/affirm'},
                       {'title': f'{random.choice(custom_reply.deny_buttons)}', 'payload': '/deny'}]
            dispatcher.utter_message(text=f"I am going to do a weather search 🔍 for location: 📍{resolved_address}.\n")
            dispatcher.utter_message(text="Please give the confirmation.",
                                     buttons=buttons)
            return [SlotSet(key='location_slot', value=resolved_address)]
        return [
            SlotSet(key='location_slot', value=resolved_address),
            FollowupAction('action_handling_out_of_scope_error_location')
        ]


class ActionMasterWeatherFetch(Action):
    def name(self) -> Text:
        return "action_master_weather_fetch"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        location = tracker.get_slot('location_slot')
        json_data = weatherapis.finding_weather(call_location=location)
        if json_data['status_code'] >= 400:
            dispatcher.utter_message(text=f"Weather search 🔍 is not going on! Please try again with proper search")
            dispatcher.utter_message(text=f"{json_data['message']}")
        return [
            SlotSet(key='weather_data', value=json_data),
            SlotSet(key='oos_counter_default', value=0),
            SlotSet(key='oos_counter_else', value=0),
            SlotSet(key='fallback_counter', value=0)
        ]


class ActionMasterWeatherPrint(Action):
    def name(self) -> Text:
        return "action_master_weather_print"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        weather_data: dict = tracker.get_slot('weather_data')
        print(tracker.sender_id)
        pprint.pprint(tracker.current_slot_values())
        if weather_data['status_code'] == 200:
            dispatcher.utter_message(
                text=f"Weather Conditions at 📍 {weather_data.get('payload').get('resolvedAddress')}\n"
                     f"Verdict: <em>'{weather_data.get('payload').get('days')[0].get('description')}'</em>\n"
            )
            dispatcher.utter_message(
                text=f"Weather Condition throughout the day {weather_data.get('payload').get('days')[0].get('datetime')}:\n"
                     f"\tTemperature: Avg. {weather_data.get('payload').get('days')[0].get('temp')}°C,\n"
                     f"\tMax: {weather_data.get('payload').get('days')[0].get('tempmax')}°C, Min: {weather_data.get('payload').get('days')[0].get('tempmin')}°C\n"
                     f"\tFeels Like: Avg. {weather_data.get('payload').get('days')[0].get('feelslike')}°C,\n"
                     f"\tMax: {weather_data.get('payload').get('days')[0].get('feelslikemax')}°C, Min: {weather_data.get('payload').get('days')[0].get('feelslikemin')}°C\n"
            )
            dispatcher.utter_message(
                text=f"Latest Weather Condition at {weather_data.get('payload').get('currentConditions').get('datetime')}:\n"
                     f"\tTemperature is {weather_data.get('payload').get('currentConditions').get('temp')}°C\n"
                     f"\tWeather Type is {weather_data.get('payload').get('currentConditions').get('conditions')}\n"
            )
            return []
        elif weather_data['status_code'] == 400:
            return [FollowupAction('action_handling_out_of_scope_error_location')]


class ActionAskForMoreDetail(Action):
    def name(self) -> Text:
        return "action_ask_for_more_details"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        buttons = [{'title': f'Yeah! In a popup view 🖥', 'payload': '/display_all_details'},
                   {'title': f'Yes, give a list to select 📜', 'payload': '/display_list'},
                   {'title': f'No, that\'s fine 🔵', 'payload': '/deny'}]
        dispatcher.utter_message(text="If you want to know more details then select from the following:",
                                 buttons=buttons)
        return []


class ActionDisplayAllDetails(Action):
    def name(self) -> Text:
        return "action_display_all_details"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # more_data = weatherapis.pass_all_details(tracker.get_slot('weather_data'))
        dispatcher.utter_message(json_message=tracker.get_slot('weather_data'))
        return []


class ActionDisplayList(Action):
    def name(self) -> Text:
        return "action_display_list"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        more_data = {
            'text': 'Select from the list:',
            'buttons': 'send',
            'details': weatherapis.show_dict,
        }
        dispatcher.utter_message(json_message=more_data)
        return []
