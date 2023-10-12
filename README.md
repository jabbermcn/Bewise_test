FastAPI приложение с использованием Docker
Этот репозиторий содержит пример FastAPI-приложения, которое вы можете легко создать и запустить в Docker контейнерах. Ваше приложение будет включать в себя FastAPI API и базу данных PostgreSQL.

Шаги для запуска
1. Установите Docker
Убедитесь, что у вас установлен Docker. Если Docker не установлен, вы можете скачать его с официального сайта Docker.

2. Клонируйте репозиторий
Вы можете склонировать этот репозиторий на свой компьютер с помощью следующей команды:

git clone https://github.com/jabbermcn/Bewise_test.git

3. Настройте переменные окружения
Откройте файл docker-compose.yml в репозитории и убедитесь, что переменные окружения для PostgreSQL настроены правильно:

  environment:
    POSTGRES_USER: postgres
    POSTGRES_PASSWORD: postgres
    POSTGRES_DB: postgres
    
4. Соберите и запустите Docker контейнеры
Запустите следующую команду в корневом каталоге репозитория, чтобы собрать и запустить Docker контейнеры:

docker-compose up --build

Это создаст и запустит два контейнера: FastAPI-приложение и PostgreSQL. FastAPI-приложение будет доступно по адресу http://localhost:8000.

5. Используйте FastAPI-приложение
Теперь вы можете использовать ваше FastAPI-приложение для получения случайных вопросов. Вы можете отправлять POST-запросы на /get_questions/ с данными в формате {"questions_num": N}, где N - количество случайных вопросов, которые вы хотите получить.

6. Остановка Docker контейнеров
Чтобы остановить Docker контейнеры, выполните следующую команду в корневом каталоге репозитория:

docker-compose down

Это завершит все контейнеры, остановит их выполнение и освободит ресурсы.
