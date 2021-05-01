from light_text_prepro.lprepro import LPrePro

obj = LPrePro()


def test_unique_function_name():
    mock_dict = read_regex_file()
    assert len(mock_dict) == len(set(mock_dict))


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


def test_chain():
    result = obj.set_text("hey @user this is my 192.122.1.2")\
        .ip_address(replace_with='[ip]')\
        .user_tag(replace_with='[user]')\
        .get_text()
    assert result == "hey [user] this is my [ip]"


def read_regex_file():
    raw_keys = []
    f = open("./light_text_prepro/rules/regex.yml", "r")
    while(True):
        line = f.readline()
        if not line:
            break
        raw_keys.append(line.split(':')[0].strip())
    f.close
    return raw_keys
