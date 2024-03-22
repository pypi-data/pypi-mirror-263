PunkEditor
==========

Framework for flexible and powerful curses-based applications.

Installation
------------

For command line version only: `pipx install punkeditor`

To use the code library: `pip3 install punkeditor` (or add to your `requirements.txt` etc).

Use
---

We only have a prototype at the moment. It's a variation on the curses TextBox class. If you seek word wrapping, or even character mapping, or copy/paste, or basically anything, look elsewhere.

The command is:

```
punke
```

Optionally, provide `--width` and `--height` options for an edit box smaller than the full terminal window.

The editor will open with an empty buffer. Try keys:

| Key | Action |
| --- | --- |
| \<arrows\> | move |
| ctrl-a | left end of line |
| ctrl-e | right end of line |
| ctrl-d | delete character |
| ctrl-k | delete remainder of line |
| \<backspace\> | backspace |

 Hit **Tab** to quit. The command will dump the contents of the buffer to the output after quitting.

We're still missing the concept of a newline character. The editor ignores the **Return** key, and only inserts a space between output

Logo by [Freepik](https://www.flaticon.com/free-icons/girl)
