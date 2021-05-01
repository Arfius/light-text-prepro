# Light Text Pre-processing

It is an easy-to-use python module that collects regex rules. The package follows the `build design pattern`. You can import it and build a chain of regex that will be applied in cascade to a input text string.

## How it works

Package reads a list of regex from `light_text_prepro/rules/regex.yml`.  Each row in `regex.yml` file identifies a regex rule, i.e.: `user_tag: '"@[0-9a-z](\.?[0-9a-z])*"'`. In this rule, the `user_tag` is the key of the regex, whereas the `'"@[0-9a-z](\.?[0-9a-z])*"'`is its value .

At run-time, the package reads the `regex.yml` and compiles a method for each regex.  At the end of the process you will be able to call the `user_tag()`method. 

## How to add a regex rules

1. Add a new row into `regex.yml` and make sure to use a unique key for the rule.
2. Add a `unit tests` under the  `tests` folder and make all test passed.  Use`$> python pytest` to run unit tests.
3. Update the below section `List of Regex` in the `Readme.st` file  
4. Create a Pull Request

## Package installation

`$> pip install light_text_prepro ` 

## Usage

```python
from light_text_prepro.lprepro import LPrePro
...
obj = LPrePro()
...
result = obj.set_text('@username') \
		 obj.user_tag(replace_with='[user]').get_text()
# result is [user]
```



### List of Regex 

```yaml
user_tag: '"@[0-9a-z](\.?[0-9a-z])*"'
email: '"^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$"'
url: '"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"'
special_chars: '"[-!$%^&*()_+|~=`{}<>?,.\"\[\]:;/\\]"'
ip_address: '"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"'
html_tag: '"^<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)$"'
tab_new_line: '"(\n|\t|\r)"'
multiple_space: '"[ ]+"'
```

