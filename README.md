# Light Text Pre-processing

`Light Text Pre-processing` is an easy-to-use python module that permits to apply a chain of built-in regex rules to a input string. Regex rules are stored in a separate YML file and compiled at run-time. The compiling mechanism and how to add a custom regex are described below.

<br/>

<p align="center">
  
  <a target="_blank" rel="noopener noreferrer" href="https://github.com/Arfius/light-text-prepro/actions/workflows/light-text-prepro.yml/badge.svg">
    <img src="https://github.com/Arfius/light-text-prepro/actions/workflows/light-text-prepro.yml/badge.svg" alt="ci/cd" style="max-width: 100%;"/>
  </a>

<a href="https://pypi.org/project/light-text-prepro" target="_blank">
    <img src="https://img.shields.io/pypi/v/light-text-prepro" alt="Package version">
</a>

<a href="https://pypi.org/project/light-text-prepro" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/light-text-prepro.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>
<p align="center">
  <a target="_blank"  href="https://twitter.com/alfarruggia">
    <img src="https://img.shields.io/twitter/follow/alfarruggia"/>
  </a>
</p>

## How it works

Package reads a list of regex from `light_text_prepro/rules/regex.yml`.  Each row in `regex.yml` identifies a regex rule such as `user_tag: '"@[0-9a-z](\.?[0-9a-z])*"'`. In this row, `user_tag` is the `key` of the regex, whereas the `'"@[0-9a-z](\.?[0-9a-z])*"'`is its `value`.

At run-time, the package reads the `regex.yml` and compiles a method for each regex, the method is named as the the `key` of the row. For example, at the end of the process, you will be able to call the `user_tag()`method, that permit to match the user tagged. Each method has the optional parameter `replace_with` that allow you to replace the string matched by regex rule with an arbitrary text.

## Package installation

### List of Regex 
```yaml
user_tag: '"(?<![\w@])@([\w@]+(?:[.!][\w@]+)*)"'
email: '"([^@|\s]+@[^@]+\.[^@|\s]+)"'
url: '"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"'
punctuation: '"[-!`?,.\":;]"'
parentheses: '"[\[\]{}()]"'
special_chars: '"[$%^&*_+|~=<>:;\\]"'
ip_address: '"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"'
html_tag: '"^<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)$"'
tab_new_line: '"(\n|\t|\r)"'
multiple_space: '"[ ]+"'
emoji: '"[^\u1F600-\u1F6FF\s]"'
```

If you are happy wiht the list above, you can install the package via pip.

```
pip install light-text-prepro
```

## How to use

```python
from light_text_prepro.lprepro import LPrePro
...
obj = LPrePro()
...
result = obj.set_text('Hey @username, this is my email my@email.com') \
		 .user_tag(replace_with='[user]') \
		 .email(replace_with='[email]') \
    	.get_text()
# result -> Hey [user], this is my email [email]
```


Otherwise, if you want to contribute to enrich the package adding your regex rule, please follow section below.

## How to add a regex rules

### Setup project

````
$> git clone https://github.com/Arfius/light-text-prepro.git
$> cd light-text-prepro
$> pip install poetry flake8
$> poetry install
````

### Add  new regex

1. Open `light_text_prepro/rules/regex.yml` and add a new row. Make sure to use a unique key for the rule. If  you get issue adding the regex rule, use any online regex validation tool and export the regex rule for python. (i.e. https://regex101.com/ => FLAVOR python => Copy to clipboard )
2. Add a `unit tests` under the  `tests` folder and make all test passed.  Use`$> poetry run pytest` to run unit tests.
3. Update the  section `List of Regex` at the end of this file.
4. Create a Pull Request


