import re
import sublime
import sublime_plugin

# Recursively substitute the input pattern
def rsub(name, input_, arg):
    if isinstance(arg, list):
        for i, a in enumerate(arg):
            arg[i] = rsub(name, input_, a)
        return arg
    else:
        return re.sub("%{}%".format(name), input_, arg)

def sub_kwargs(kwargs, name, value):
    if "cmd" in kwargs:
        kwargs.update({"cmd": rsub(name, value, kwargs["cmd"])})
    if "shell_cmd" in kwargs:
        kwargs.update({"shell_cmd": rsub(name, value, kwargs["shell_cmd"])})

class BuildSystemInputCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        window = sublime.active_window()
        inputs = kwargs.pop("input", None)
        storage = {"name": [], "value": []}
        if inputs:
            names = iter(sorted(inputs))
            # A little bit hacky, but I do not see another way to do this...
            def do_next(input_):
                if input_ is not None:
                    storage["value"].append(input_)
                try:
                    name = names.__next__()
                    storage["name"].append(name)
                    window.show_input_panel(
                        "{}:".format(name), inputs[name], do_next, None, None
                    )
                except StopIteration:
                    for name, value in zip(storage["name"], storage["value"]):
                        sub_kwargs(kwargs, name, value)
                    window.run_command("exec", kwargs)

            do_next(None)
