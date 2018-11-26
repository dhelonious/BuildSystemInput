import re
import sublime
import sublime_plugin

# Recursively substitute the input pattern
def sub(input_, arg):
    if isinstance(arg, list):
        for i, a in enumerate(arg):
            arg[i] = sub(input_, a)
        return arg
    else:
        return re.sub("%{?input}?%", input_, arg)

class BuildSystemInputCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        window = sublime.active_window()
        def on_done(input_):
            if "cmd" in kwargs:
                kwargs.update({"cmd": sub(input_, kwargs["cmd"])})
            if "shell_cmd" in kwargs:
                kwargs.update({"shell_cmd": sub(input_, kwargs["shell_cmd"])})
            window.run_command("exec", kwargs)

        default_input = kwargs.pop("input", "")
        window.show_input_panel("args:", default_input, on_done, None, None)