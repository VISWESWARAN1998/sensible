# SWAMI KARUPPASWAMI THUNNAI


def camel_to_snake(camel):
    snake = ""
    for i in camel:
        if i.isupper():
            snake += "_"
            snake += i.lower()
        else:
            snake += i
    return snake