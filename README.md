# BuildSystemInput

Extend default Sublime Text 3 build systems with input arguments.

Choose the `"build_system_input"` target in any build system to prompt for an input, which is substituted for any occurence of `%input%` in `"cmd"` or `"shell_cmd"`. A default text can be provided using the new `"input"` key. Two simple use cases of this concept are shown below.

Pass arguments to a Python script:
```json
    {
        "target": "build_system_input",
        "selector" : "source.python",
        "linux": {
            "shell_cmd": "xterm -e 'python $file_name %input% && echo && echo Press ENTER to continue && read line && exit'"
        },
        "windows": {
            "shell_cmd": "start cmd /k \"python $file_name %input% && pause && exit\""
        },
        "osx": {
            "shell_cmd": "xterm -e 'python $file_name %input% && echo && echo Press ENTER to continue && read line && exit'"
        },
        "shell": true,
        "file_regex": "^\\s*File \"(...*?)\", line ([0-9]*)",
        "working_dir": "$file_path",
        "input": "default arguments"
    }
```

Pass compiler flags to clang:
```json
    {
        "target": "build_system_input",
        "selector" : "source.c, source.cpp, source.c++",
        "cmd": ["clang++", "-std=c++11", "-Wno-c++98-compat-pedantic -Wno-newline-eof", "%input%", "-Wall", "-o", "$file_base_name", "$file_name"],
        "windows": {
            "cmd": ["clang-cl", "-std=c++11", "-Wno-c++98-compat-pedantic -Wno-newline-eof", "%input", "/Wall", "/o", "$file_base_name", "$file_name"]
        },
        "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
        "working_dir": "$file_path",
        "variants": [
            {
                "name": "Run Terminal",
                "linux": {
                    "shell_cmd": "clang++ -std=c++11 -Wno-c++98-compat-pedantic -Wno-newline-eof %input% -Wall \"$file\" -o \"$file_path/$file_base_name\" && xterm -e '$file_path/$file_base_name && echo && echo Press ENTER to continue && read line && exit'"
                },
                "windows": {
                    "shell_cmd": "clang-cl -std=c++11 -Wno-c++98-compat-pedantic -Wno-newline-eof %input% /Wall \"$file\" /o \"$file_path/$file_base_name\" && start cmd /k \"$file_base_name && pause && exit\""
                },
                "osx": {
                    "shell_cmd": "clang++ -std=c++11 -Wno-c++98-compat-pedantic -Wno-newline-eof %input% -Wall \"$file\" -o \"$file_path/$file_base_name\" && xterm -e '$file_path/$file_base_name && echo && echo Press ENTER to continue && read line && exit'"
                },
                "shell": true
            }
        ],
        "input": "default compiler flags"
    }
```

**NOTE**: In contrast to the UNIX-style Sublime Text 3 build system variables, i. e. `$VAR`, this package uses DOS-style variables, i. e. `%VAR%`. This is, because Sublime Text will try to substitute environment variables in `"cmd"` and `"shell_cmd"`, which results in the erasion of all unknown variables.

## Installation
Clone this repository to your Sublime Text 3 **Packages** folder. You can find it by using the menu: Preferences > Browse Packages...

No configuration is necessary apart from using the `"build_system_input"` as target for your custom build system.