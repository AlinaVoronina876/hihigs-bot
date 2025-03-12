# hihigs-bot
Ranepa telegram bot for education (computer science)

## Установка

### Запуск проекта из исходника

1. Для запуска проекта стяните его с помощью `git clone`

2. Перейдите в каталог проекта и создайте изолированную среду. Например, `.venv`

```
python3 -m venv .venv
```

3. Запустите среду и установите зависимости
   
```
pip install -r requirements.txt
```

4. Полученный токен в [BotFather](https://t.me/BotFather) вставить в созданный файл `.env`

```
TOKEN=<ВАШ ТОКЕН>
```

5. Для запуска проекта введите в консоли

```
python3 main.py
```
### Запуск docker-контейнера

1. Для запуска проекта в контейнере стяните его с помощью `git clone`. Проект содержит `Dockerfile` и `docker-compose.yml`

2. Перейдите в каталог проекта и запустите команду сборки контейнера `example-tgbot:vX`, где X – текущая версия проекта.

```
docker build -t <ВАШ КОНТЕЙНЕР>:v<ВЕРСИЯ> .
```
3. Для запуска контейнера в фоновом режиме используйте команду

```
docker run -d -e .env <ВАШ КОНТЕЙНЕР>:v<ВЕРСИЯ>
```

Проверить состоятние запущенного контейнера для `docker`

```
docker ps
```

4. Для автоматизированной сборки нескольких контейнеров воспользуйтесь `docker-compose`

```
docker-compose -up --build -d
```

Проверить состоятние запущенного контейнера для `docker-compose`

```
docker-compose ps
```

5. Если вы хотите остановить контейнер `docker`

```
docker stop <ID-контейнера>
```

Для удаления контейнера

```
docker rm <ID-контейнера>
```

Если вы хотите остановить `docker-compose`

```
docker-compose down
```

Перезапустить контейнеры

```
docker-compose restart
```



## Запуск проекта 

1. Для запуска проекта стяните его с помощью `git clone`

2. Полученный токен в {BotFather}(https://t.me/BotFather) вставить в созданный файл `.env`

```
TOKEN=<ВАШ ТОКЕН>
```

3. Для запуска проекта введите в консоли

```
python3 main.py
```