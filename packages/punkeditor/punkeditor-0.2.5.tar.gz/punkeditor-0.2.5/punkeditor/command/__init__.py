from wizlib.command import WizCommand
from wizlib.input_handler import InputHandler
from wizlib.config_handler import ConfigHandler
from wizlib.ui_handler import UIHandler


class PunkEditorCommand(WizCommand):

    default = 'edit'
    handlers = [InputHandler, ConfigHandler, UIHandler]
