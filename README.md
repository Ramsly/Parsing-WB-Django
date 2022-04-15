# Parsing WB (Fullstats test)



## Настройка

Склонируйте проект

```bash
git clone https://github.com/Ramil2003/Fullstats_test
```

Создайте виртуальное окружение:
```bash
py -m venv venv
```

Активируйте виртуальное окружение:
```bash
venv/Scripts/activate
```

Установите зависимости

```bash
pip install -r requirements.txt
```

Создайте БД Postgres

```bash
create database fullstats with template=template0 encoding=6;
```
```bash
create user fullstats_admin with password 'qwerty12345';
```
```bash
grant all privileges on database 'fullstats' to fullstats_admin;
```

Запустите Docker

```bash
docker-compose build
```
```bash
docker-compose up
```

Сделайте миграции

```bash
docker-compose exec web python manage.py makemigrations
```
```bash
docker-compose exec web python manage.py migrate
```