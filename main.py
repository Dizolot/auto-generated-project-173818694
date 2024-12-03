ранслирует текст с английского языка на русский с помощью библиотеки googletrans.

```python
from googletrans import Translator

def translate_text(text):
    translator = Translator()
    translated_text = translator.translate(text, dest='ru')
    return translated_text.text

text_to_translate = input("Введите текст для перевода: ")
translated_text = translate_text(text_to_translate)

print("Переведенный текст:")
print(translated_text)
```

Пример использования программы:
```
Введите текст для перевода: Hello, how are you?
Переведенный текст:
Привет, как ты?
```