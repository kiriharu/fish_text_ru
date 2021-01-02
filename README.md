<h1 align="center">Fish-text.ru python wrapper</h1>

Эта небольшая обёртка позволяет использовать API с сайта Fish-text.ru для генерации так называемого "текста-рыбы" или "рыботекста"

Тестировано на Python 3.8, 3.9.1

## Примеры использования
* В вашем проекте необходимо заполнить базу данных каким-то текстовым контентом
* Собственно, наверное, это все ¯\\\_(ツ)\_/¯

## Установка
Установить стабильную версию с PyPi:
```
python -m pip install fish_text_ru 
```
Установить с GitHub:
```
python -m pip install git+https://github.com/kiriharu/fish_text_ru
```

## Использование
### Json Wrapper (рекомендуется)

```python
# Импортируем FishTextJson и TextType, нужный нам.
# В методе .get() вернется по итогу объект JsonAPIResponse
from fishtext import FishTextJson
from fishtext.types import TextType, JsonAPIResponse

# Делаем объект
api = FishTextJson(text_type=TextType.Title)
# Используем!
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

# Делаем объект
api = FishTextHtml(text_type=TextType.Title)
# Используем!
title = api.get(1)

print(title) # <p> какой-то там title </p>

```
