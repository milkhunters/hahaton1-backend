# hahaton1-backend

![TeamCity build status](https://teamcity.milkhunters.ru/app/rest/builds/buildType:id:HahaTonBackend_ProdBuild/statusIcon.svg)

REST API backend приложение для кейса

[Frontend часть](https://github.com/milkhunters/hahaton-frontend)

Язык: Python

Фреймфорк: FastAPI


В качестве базы данных используется Postgrsql, но за счёт использования ORM её легко поменять

Теоритически backend приложение выполняет все нефункциональные требования

## Как запустить

Для запуска требуется `docker`, `consul`, `redis` и `postgresql`

Перед запуском необходимо собрать образ с помощью `docker build`

Команда для запуска:
```sh
docker run -d --restart=always -u 0 --name haha-ton-prod -e MODE=prod -e DEBUG=0 -p 8080:80 haha-ton-image:latest
```

### Список всех ключей конфигурации в `consul`

```
haha-ton/base/contact/email
haha-ton/base/contact/name
haha-ton/base/contact/url
haha-ton/base/description
haha-ton/base/email/host
haha-ton/base/email/isSSL
haha-ton/base/email/isTLS
haha-ton/base/email/password
haha-ton/base/email/port
haha-ton/base/email/user
haha-ton/base/name
haha-ton/prod/database/postgresql/host
haha-ton/prod/database/postgresql/name
haha-ton/prod/database/postgresql/password
haha-ton/prod/database/postgresql/port
haha-ton/prod/database/postgresql/username
haha-ton/prod/database/redis/host
haha-ton/prod/database/redis/password
haha-ton/prod/database/redis/port
haha-ton/prod/is_secure_cookie
haha-ton/prod/jwt/JWT_ACCESS_SECRET_KEY
haha-ton/prod/jwt/JWT_REFRESH_SECRET_KEY
```

Несмотря на то, что функции отправки email сообщений не реализованы, указание как миниму значения `null` в эти ключи **обязательно**.
