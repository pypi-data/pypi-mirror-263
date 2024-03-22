from wizlib.app import WizApp

from punkeditor.command import PunkEditorCommand


class PunkEditorApp(WizApp):

    base_command = PunkEditorCommand
    name = 'punke'
