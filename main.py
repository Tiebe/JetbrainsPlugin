# Import StreamController modules
import os

from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.PluginManager.ActionHolder import ActionHolder
from .actions.CustomAction.CustomAction import CustomAction
from .actions.RunAction.RunAction import RunAction
from .actions.DebugAction.DebugAction import DebugAction

class PluginTemplate(PluginBase):
    def __init__(self):
        super().__init__()

        self.run_action_holder = ActionHolder(
            plugin_base = self,
            action_base = RunAction,
            action_id = "me_tiebe_streamdeck_plugin_jetbrains::RunAction", # Change this to your own plugin id
            action_name = "Run Action",
        )

        self.add_action_holder(self.run_action_holder)

        self.debug_action_holder = ActionHolder(
            plugin_base = self,
            action_base = DebugAction,
            action_id = "me_tiebe_streamdeck_plugin_jetbrains::DebugAction", # Change this to your own plugin id
            action_name = "Debug Action",
        )

        self.add_action_holder(self.debug_action_holder)

        self.custom_action_holder = ActionHolder(
            plugin_base = self,
            action_base = CustomAction,
            action_id = "me_tiebe_streamdeck_plugin_jetbrains::CustomAction", # Change this to your own plugin id
            action_name = "Custom Action",
        )

        self.add_action_holder(self.custom_action_holder)

        # Register plugin
        self.register(
            plugin_name = "Jetbrains IDE",
            github_repo = "https://github.com/Tiebe/JetbrainsPlugin",
            plugin_version = "1.0.0",
            app_version = "1.5.0"
        )