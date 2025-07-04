from data.plugins.me_tiebe_streamdeck_plugin_jetbrains.connection import jetbrains_request
from src.backend.DeckManagement.InputIdentifier import Input
from src.backend.PluginManager.ActionBase import ActionBase
from src.backend.PluginManager.EventAssigner import EventAssigner

import urllib.parse

class DefaultAction(ActionBase):
    def __init__(self, jetbrains_action_id, *args, **kwargs):
        self.jetbrains_action_id = jetbrains_action_id
        self.run_config = None

        super().__init__(*args, **kwargs)

    def on_key_up(self) -> None:
        host = "127.0.0.1"
        password = None
        port = None

        endpoint = f"/api/action/{self.jetbrains_action_id}"
        if self.run_config is not None and self.run_config != "":
            endpoint += "?name=" + urllib.parse.quote(self.run_config.get_text())

        jetbrains_request(
            endpoint,
            "GET",
            host, password, port
        )
