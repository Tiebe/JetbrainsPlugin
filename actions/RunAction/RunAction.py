import os

from data.plugins.me_tiebe_streamdeck_plugin_jetbrains.actions.DefaultAction.DefaultAction import DefaultAction

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

class RunAction(DefaultAction):
    def __init__(self, *args, **kwargs):
        super().__init__("Run", *args, **kwargs)
        self.run_config_entry = None

    def on_ready(self) -> None:
        icon_path = os.path.join(self.plugin_base.PATH, "assets", "run.svg")
        self.set_media(media_path=icon_path, size=0.5)
        self.run_config = self.get_settings().get("run_config", "")

    def get_config_rows(self) -> "list[Adw.PreferencesRow]":
        super_rows = super().get_config_rows()

        self.run_config_entry = Adw.EntryRow(title="Run config name")

        settings = self.get_settings()
        self.run_config_entry.set_text(settings.get("run_config", ""))

        self.run_config_entry.connect("changed", self.on_value_changed)

        super_rows.append(self.run_config_entry)
        return super_rows

    def on_value_changed(self, config):
        settings = self.get_settings()
        settings["run_config"] = config.get_text()
        self.set_settings(settings)