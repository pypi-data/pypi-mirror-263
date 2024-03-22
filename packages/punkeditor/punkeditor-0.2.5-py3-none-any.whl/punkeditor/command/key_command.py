from dataclasses import dataclass
import curses

from punkeditor.command import PunkEditorCommand


class KeyCommand(PunkEditorCommand):

    name = 'key'

    def loop(self, window: curses.window):
        window.clear()
        chrs = hexs = ''
        while True:
            ch = window.getch()
            if chr(ch) == ' ':
                break
            chrs += chr(ch)
            hexs += hex(ch) + ' '
            window.clear()
            window.addstr(chrs + '\n\n' + hexs + '\n\n')
            window.refresh()

    @PunkEditorCommand.wrap
    def execute(self):
        curses.wrapper(self.loop)
