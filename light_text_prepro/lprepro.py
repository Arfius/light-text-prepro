import yaml
import re
import os



class LPrePro:
    def __init__(self):
        self.__text = None
        self.template = """LPrePro.{0} = lambda self, replace_with="" : self._t_func(r{1}, replace_with) """
        dictionary = self.__read_yml('regex.yml')
        for key in dictionary.keys():
            f_string = self.template.format(key, dictionary[key])
            exec(f_string)

    def _t_func(self, regex: str, replace_with: str):
        if self.__text is None:
            raise ValueError("Use set_text to initialise text")
        self.__text = re.sub(regex, replace_with, self.__text, flags=re.M | re.I)
        return self

    def __read_yml(self, file_name: str):
        with open(f"{os.path.dirname(os.path.realpath(__file__))}/rules/" + file_name) as file:
            return yaml.load(file, Loader=yaml.FullLoader)

    def set_text(self, text: str):
        self.__text = text
        return self

    def get_text(self) -> str:
        return self.__text
