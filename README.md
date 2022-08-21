# Parsing WB (Fullstats test)

### Функционал:

- Парсинг WB по артикулу товара
- Парсинг происходит раз в сутки с помощью Celery
- Реализованы фильтры и порядок отображения
- Фильтр по временному диапазону
- Упаковано в Docker compose



## Настройка

Склонируйте проект

```bash
git clone https://github.com/Ramil2003/Fullstats_test
```

Создайте виртуальное окружение:
```bash
python3 -m venv venv
```

Активируйте виртуальное окружение:
```bash
source venv/Scripts/activate
```

Установите зависимости

```bash
pip install -r requirements.txt
```

Запустите Docker

```bash
docker-compose up --build
```