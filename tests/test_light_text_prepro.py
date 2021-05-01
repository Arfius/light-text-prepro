from light_text_prepro import __version__
from light_text_prepro.lprepro import LPrePro

obj = LPrePro()


def test_version():
    assert __version__ == '0.1.0'


def test_unique_function_name():
    mock_dict = {'fn1': 'rg1', 'fn1': 'rg2', 'fn1': 'rg3'}
    obj._check_unique_function_name(mock_dict)


def test_user_tag():
    result = obj.set_text('@username').user_tag(replace_with='[user]').get_text()
    assert result == "[user]"


def test_email():
    result = obj.set_text('my@email.com').email().get_text()
    assert result == ""


def test_special_chars():
    result = obj.set_text("-!$%^&*()_+|~=`{}\[\]:").special_chars().get_text()
    assert result == ""


def test_ip_address():
    result = obj.set_text("192.122.1.2").ip_address().get_text()
    assert result == ""


def test_html_tag():
    result = obj.set_text("<div>ciao</div>").html_tag().get_text()
    assert result == ""


def test_tab_new_line():
    result = obj.set_text("hello\tword\n").tab_new_line().get_text()
    assert result == "helloword"


def test_multiple_space():
    result = obj.set_text("hello    word").multiple_space().get_text()
    assert result == "helloword"
