import appdaemon.plugins.hass.hassapi as hass
import sys
import os

sys.path.append(os.path.dirname(__file__))
from commands import handle_command

class JarvisBrain(hass.Hass):
    def initialize(self):
        self.listen_event(self.process_voice, "jarvis_voice_input")
        self.log("Jarvis Bridge is active.")

    def process_voice(self, event_name, data, kwargs):
        user_text = data.get("text", "")
      
        response = handle_command(user_text)
        self.call_service("tts/speak", 
            media_player_entity_id="media_player.your_speaker",
            message=response
        )
