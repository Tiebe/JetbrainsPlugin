from data.plugins.me_tiebe_streamdeck_plugin_jetbrains.actions.DefaultAction.DefaultAction import DefaultAction

import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

class CustomAction(DefaultAction):
    def __init__(self, *args, **kwargs):
        super().__init__(None, *args, **kwargs)
        self.action_id_input = None

    def on_ready(self):
        self.jetbrains_action_id = self.get_settings().get("action_id", "")
        

    def get_config_rows(self) -> "list[Adw.PreferencesRow]":
        super_rows = super().get_config_rows()

        self.action_id_input = Adw.EntryRow(title="Action ID")

        settings = self.get_settings()
        self.action_id_input.set_text(settings.get("action_id", ""))

        self.action_id_input.connect("changed", self.on_value_changed)

        super_rows.append(self.action_id_input)
        return super_rows

    def on_value_changed(self, config):
        settings = self.get_settings()
        settings["action_id"] = config.get_text()

        self.jetbrains_action_id = config.get_text()

        self.set_settings(settings)