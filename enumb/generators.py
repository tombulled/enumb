import typing

import addict

def generate(generator):
    def wrapper(name: str, start: int, count: int, last_values: typing.List[typing.Any]):
        return generator \
        (
            addict.Dict \
            (
                name        = name,
                start       = start,
                count       = count,
                last_values = last_values,
            )
        )

    return wrapper

def generate_name(generator):
    return generate(lambda kwargs: generator(kwargs.name))

def generate_count(generator):
    return generate(lambda kwargs: generator(kwargs.count))
