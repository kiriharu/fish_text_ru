<h1 align="center">Fish-text.ru python wrapper</h1>

Эта небольшая обёртка позволяет использовать API с сайта Fish-text.ru для генерации так называемого "текста-рыбы" или "рыботекста"

## Примеры использования
* В вашем проекте необходимо заполнить базу данных каким-то текстовым контентом
* Собственно, наверное, это все ¯\_(ツ)_/¯

## Установка
Установить стабильную версию с PyPi:
```
pip install fish_text_ru
```
Установить с GitHub:
```
pip install https://github.com/kiriharu/fish_text_ru/archive/master.zip
```

## Использование
### Json Wrapper (рекомендуется)

```python
# импортируем FishTextJson и TextType, нужный нам.
# В методе .get() вернется по итогу объект JsonAPIResponse
from fishtext import FishTextJson
from fishtext.types import TextType, JsonAPIResponse

# делаем объект
api = FishTextJson(text_type=TextType.Title)
# используем!
titles = api.get(1)

# Используем JsonAPIResponse
print(titles.status)
print(titles.errorCode)
print(titles.text)
```

### Html wrapper
```python

from fishtext import FishTextHtml
from fishtext.types import TextType

# делаем объект
api = FishTextHtml(text_type=TextType.Title)
# используем!
title = api.get(1)

print(title) # <p> какой-то там title </p>

```