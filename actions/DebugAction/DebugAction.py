import os

from data.plugins.me_tiebe_streamdeck_plugin_jetbrains.actions.DefaultAction.DefaultAction import DefaultAction

import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

class DebugAction(DefaultAction):
    def __init__(self, *args, **kwargs):
        super().__init__("Debug", *args, **kwargs)

    def on_ready(self) -> None:
        icon_path = os.path.join(self.plugin_base.PATH, "assets", "debug.svg")
        self.set_media(media_path=icon_path, size=0.5)

    def get_config_rows(self) -> "list[Adw.PreferencesRow]":
        super_rows = super().get_config_rows()

        self.run_config = Adw.EntryRow(title="Run config name")

        super_rows.append(self.run_config)
        return super_rows