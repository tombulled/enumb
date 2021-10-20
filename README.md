# enumb
Concise, Pythonic Enums

## Prelude
This library was created out of the frustration of writing `enum.auto()`.

## Installation
This library uses [Poetry](https://github.com/python-poetry/poetry) and can easily be installed using *pip*
```console
$ pip install git+https://github.com/tombulled/enumb
```

## Examples

### NoValue
```python
>>> class Role(enumb.NoValue):
        ADMIN: str
>>>
>>> Role.ADMIN
<Role.ADMIN>
>>>
```

### Name
```python
>>> class MyEnum(enumb.Name):
        Some__SPECIFIC_namE: str
>>>
>>> MyEnum.Some__SPECIFIC_namE
<MyEnum.Some__SPECIFIC_namE: 'Some__SPECIFIC_namE'>
>>>
```

### Lower
```python
>>> class MyEnum(enumb.Lower):
        FOO_BAR: str
>>>
>>> MyEnum.FOO_BAR
<MyEnum.FOO_BAR: 'foo bar'>
>>>
```

### Train
```python
>>> class Header(enumb.Train):
        USER_AGENT: str
>>>
>>> Header.USER_AGENT
<Header.USER_AGENT: 'User-Agent'>
>>>
```
