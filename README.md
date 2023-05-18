# GPT-4-Free навык для Алисы от Яндекса

## Описание

Этот проект является форком проекта [chat_gpt_yandex_alice](https://github.com/peleccom/chat_gpt_yandex_alice) и добавляет навык для умной колонки Алиса, который позволяет использовать модель языка ChatGPT для генерации текста в ответ на пользовательские запросы. Основное отличие этого проекта в том, что вместо официального API OpenAI используется [gpt4free](https://github.com/xtekky/gpt4free), с API от you.com поискового сервиса. Это означает, что для запуска нужен только сервер и платить за API ненужно, так как оно бесплатно.

## Инструкции по установке и использованию

1. Склонируйте репозиторий на свой компьютер:

```bash
git clone https://github.com/cofob/alice_gpt4ree.git
```

2. Запустите проект:

```bash
docker-compose up
```

3. Подключите навык к Алисе.

## Локальное тестирование

1. Установите утилиту alice-nearby.
2. Запустите ее указав webhook на localhost:

```bash
./alice-nearby --webhook=http://localhost:5000/post --port=3456
```

3. Откройте <http://localhost:3456> в браузере.

## Ссылки

- [GPT4Free API](https://github.com/xtekky/gpt4free)
- [Документация по API Алисы](https://yandex.ru/dev/dialogs/alice/doc/)
- [Руководство по разработке навыков для Алисы](https://yandex.ru/dev/dialogs/alice/doc/quickstart-about.html)
