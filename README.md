# BuildSystemInput

Extend default Sublime Text 3 build systems with input arguments.

Choose the `"build_system_input"` target in any build system to prompt for inputs, which are substituted for any occurence of the corresponding variable in `"cmd"` or `"shell_cmd"`. The input variables and their default values are provided in the new `"input"` dictionary. For example,
```json
        "input": {
            "input1": "a",
            "input2": "b"
        }
```
will first prompt for `%input1%` with default value `"a"` and then for `%input2%` with default value `"b"`. Two simple use cases of this concept are shown below for a single input variable. However, you can use as many input variables as you like.

Pass arguments to a Python script:
```json
    {
        "target": "build_system_input",
        "selector" : "source.python",
        "shell_cmd": "xterm -e 'python $file_name %args%; echo && echo Press ENTER to continue && read line && exit'",
        "windows": {
            "shell_cmd": "start cmd /k \"python $file_name %args% & pause && exit\""
        },
        "shell": true,
        "file_regex": "^\\s*File \"(...*?)\", line ([0-9]*)",
        "working_dir": "$file_path",
        "input": {
            "args": "some arguments"
        }
    }
```

Pass compiler flags to clang:
```json
    {
        "target": "build_system_input",
        "selector" : "source.c, source.cpp, source.c++",
        "cmd": ["clang++", "-std=c++11", "-Wno-c++98-compat-pedantic", "%flags%", "-Wall", "-o", "$file_base_name", "$file_name"],
        "windows": {
            "cmd": ["clang-cl", "-std=c++11", "-Wno-c++98-compat-pedantic", "%flags", "/Wall", "/o", "$file_base_name", "$file_name"]
        },
        "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
        "working_dir": "$file_path",
        "variants": [
            {
                "name": "Run Terminal",
                "shell_cmd": "clang++ -std=c++11 -Wno-c++98-compat-pedantic %flags% -Wall \"$file\" -o \"$file_path/$file_base_name\" && xterm -e '$file_path/$file_base_name; echo && echo Press ENTER to continue && read line && exit'",
                "windows": {
                    "shell_cmd": "clang-cl -std=c++11 -Wno-c++98-compat-pedantic %flags% /Wall \"$file\" /o \"$file_path/$file_base_name\" && start cmd /k \"$file_base_name & pause && exit\""
                },
                "shell": true
            }
        ],
        "input": {
            "flags": "-Wno-newline-eof"
        }
    }
```

**NOTE**: In contrast to the UNIX-style Sublime Text 3 build system variables, i. e. `$var`, this package uses DOS-style variables, i. e. `%var%`. This is, because Sublime Text will try to substitute environment variables in `"cmd"` and `"shell_cmd"`, which results in the erasion of all unknown variables.

## Installation
Clone this repository to your Sublime Text 3 **Packages** folder. You can find it by using the menu: Preferences > Browse Packages...

No configuration is necessary apart from using the `"build_system_input"` as target for your custom build system.
