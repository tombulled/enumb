# enumb
Beautifully streamlined Python Enums

## About
Are you fed up of writing `enum.auto()`... me too!

## Installation
This library uses [Poetry](https://github.com/python-poetry/poetry) and can easily be installed using *pip*
```console
$ pip install git+https://github.com/tombulled/enumb
```

## Usage
```python
>>> class Protocol(enumb.AutoName):
        UDP: str
        TCP: str
>>>
>>> Protocol.UDP
<Protocol.UDP: 'UDP'>
>>>
>>> class Header(enumb.AutoNameSlugTitle):
        REFERER:         str
        USER_AGENT:      str
        ACCEPT_LANGUAGE: str
>>>
>>> Header.ACCEPT_LANGUAGE
<Header.ACCEPT_LANGUAGE: 'Accept-Language'>
>>>
>>> class Band(enumb.AutoNameTitle):
        NIRVANA:      str
        FOO_FIGHTERS: str
>>>
>>> Band.FOO_FIGHTERS
<Band.FOO_FIGHTERS: 'Foo Fighters'>
>>>
>>> class Product(enumb.AutoNameSlugLower):
        CHROME:      str
        GOOGLE_PLAY: str
        GMAIL:       str

>>> Product.GOOGLE_PLAY
<Product.GOOGLE_PLAY: 'google-play'>
>>>
>>> >>> class Parameter(enumb.AutoNameSnakeLower):
...     USERNAME: str
...     PASSWORD: str
...     USE_SSL:  str
...
>>> Parameter.USE_SSL
<Parameter.USE_SSL: 'use_ssl'>
>>>
>>> # etc.
```


## Credits
Here's a list of the awesome libraries used to make `enumb`
| Library | Repository |
| ------- | ---------- |
| [addict](https://pypi.org/project/addict/) | [mewwts/addict](https://github.com/mewwts/addict) |
| [humps](https://pypi.org/project/pyhumps/) | [nficano/humps](https://github.com/nficano/humps) |
| [slugify](https://pypi.org/project/python-slugify/) | [un33k/python-slugify](https://github.com/un33k/python-slugify) |
