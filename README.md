# FastAPI Redis app

Тестовое приложение на FastAPI и Redis.
Используется для хранения и получения данных по номеру телефона.

## Запуск

    docker-compose up --build

## Тестирование

    docker-compose up --build tests

## Второе задание
### 1
    WITH trimmed_full_names AS (
      SELECT name, SUBSTRING(name FROM '^[^.]+') AS short_name
      FROM full_names
    )
    UPDATE full_names f
    SET status = s.status
    FROM short_names s, trimmed_full_names t
    WHERE f.name = t.name
      AND t.short_name = s.name
      AND f.status IS NULL;

### 2
    UPDATE full_names f
    SET status = s.status
    FROM short_names s
    WHERE REGEXP_REPLACE(f.name, '\..+$', '') = s.name
    AND f.status IS NULL;

    
