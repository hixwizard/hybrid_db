### hybrid_db 0.1.0
#### Описание:
Микросервис для работы с книгами с использованием:
- PostgreSQL — основное хранилище
- Elasticsearch — полнотекстовый поиск  
**Текущий статус**: реализована работа с PostgreSQL
---
#### Проверка работы API:
```bash
curl -X GET "http://localhost:8000/health" -H "accept: application/json"
```
#### Создание книги:
```bash
curl -X POST "http://localhost:8000/books/" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d '{"title":"Clean Code","author":"Robert Martin","description":"Best practices"}'
```
#### Получение книги по id:
```bash
curl -X GET "http://localhost:8000/books/1" -H "accept: application/json"
```
#### Получение всех книг:
```bash
curl -X GET "http://localhost:8000/books/" -H "accept: application/json"
```
#### Структура:
```
hybrid_db/
├── app/
│   ├── api/                  # FastAPI роутеры
│   │   ├── v1/               # Версия API
│   │   │   ├── endpoints/    # Разделы API
│   ├── core/                 # Конфиги, утилиты
│   ├── db/                   # Работа с базами данных
│   │   ├── elasticsearch/    # ES-клиент и индексы
│   │   ├── postgres/         # SQLAlchemy модели и сессии
│   │   └── redis/            # (опционально)
│   ├── models/               # Pydantic схемы
│   ├── services/             # Бизнес-логика
│   └── main.py               # FastAPI app
├── docker-compose.yaml       # Конфигурация PostgreSQL + Elasticsearch + app
└── Dockerfile
```

#### Запуск:
```bash
docker-compose up -d
```
#### Автор: [Баринов Станислав](https://github.com/hixwizard)
*2025*