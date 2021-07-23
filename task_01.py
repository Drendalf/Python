import re


def email_parse(email_address):
    try:
        c = {}
        pattern = re.compile(r"[@]")
        text = re.split(pattern, email_address)
        c["username"] = text[0]
        c["domain"] = text[1]
        return c
    except (IndexError,) as e:
        c = "адрес не правильный"
        return c


print(email_parse("email@address"))
print(email_parse("emailaddress"))
