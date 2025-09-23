# 🏋️‍♂️ Фитнес-клуб DVFitness - Документация проекта (Django + Nuxt 3)

> **🚧 Сайт в разработке**  
> Я активно работаю над проектом. Окончательная версия будет доступна в ближайшее время.

![Фитнес клуб DVFitness](/frontend/public/gym_screen.png)

## 🚀 О проекте

Современный сайт премиального фитнес-клуба с:

- ✅ **Полноценный Backend на Django** (CRM, расписание, бронирование)
- ✅ **Интерактивный Frontend на Nuxt 3** (SSR, PWA, анимации)
- ✅ **Система бронирования** онлайн-записи на тренировки
- ✅ **Персональные кабинеты** для клиентов и тренеров
- ✅ **Полная SEO-оптимизация** (мета-теги, микроразметка, sitemap)

---

## 💪 Технологический стек

### Backend (Django Powerhouse)

- **Python 3.10** + Django
- **Django REST Framework** - мощное API
- **PostgreSQL** - надежное хранение данных
- **Celery + Redis** - напоминания о тренировках, отчеты
- **Stripe** - онлайн-платежи за абонементы
- **Docker** - контейнеризация
- **Recaptcha** - защита от спама

---

### Frontend (Nuxt 3)

- **Vue 3** + Composition API
- **Pinia** - состояние приложения (расписание, профили)
- **SASS** - современный дизайн
- **NuxtImg** - ленивая загрузка изображений
- **NuxtIcon** - иконки
- **Swiper** - слайдеры
- **Yandex Maps API** - интерактивная карта
- **V-Calendar** - система бронирования
- **Recaptcha** - защита от спама
- **Nuxt-AOS** - анимация при скролле

---

---

## 🛠️ Установка и запуск

### 1. Backend (Django)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```

---

### 2. Frontend (Nuxt)

```bash
cd frontend
npm install
npm run dev
```


# django.contrib.gis    - почитать


# 🚀 Чек-лист улучшений для проекта «Фитнес-клуб» (Django REST + Nuxt3 SSR)

## 🧑‍💻 Пользовательские фичи
- [ ] **Регистрация и авторизация**
  - JWT (refresh/access токены) через `djangorestframework-simplejwt`
  - OAuth вход (Google, VK, Yandex, Apple ID)
  - SSR-авторизация в Nuxt (куки + Pinia store)

- [ ] **Личный кабинет клиента**
  - История покупок абонементов
  - Прогресс: вес, замеры тела, посещённые тренировки
  - Возможность заморозки абонемента

- [ ] **Календарь тренировок**
  - Просмотр расписания
  - Запись на занятия
  - Drag&Drop (перенос тренировок)
  - Интеграция с Google Calendar/iCal

- [ ] **Оплата**
  - Подключить Stripe или YooKassa
  - Покупка и продление абонементов онлайн

- [ ] **Геймификация**
  - Бейджи за активность
  - Рейтинг участников (лидерборд)

- [ ] **Чат и онлайн-коммуникации**
  - Чат с тренером через WebSocket (Django Channels)
  - Push-уведомления (PWA) о новых занятиях или акциях

---

## ⚙️ Бэкенд (Django + DRF)
- [ ] **Асинхронные задачи (Celery + Redis)**
  - Email/SMS напоминания о тренировках
  - Рассылка акций
  - Автоматическая проверка статуса оплаты

- [ ] **Фильтрация и поиск**
  - DjangoFilter для списка тренеров/услуг
  - ElasticSearch/Meilisearch для умного поиска

- [ ] **Геолокация**
  - Поиск ближайшего клуба (GeoDjango + PostGIS)

- [ ] **Документация API**
  - drf-spectacular → Swagger/Redoc UI

- [ ] **GraphQL (опционально)**
  - Поднять GraphQL API (Graphene или Strawberry)
  - Использовать для гибких запросов в Nuxt (Apollo Client)

---

## 🎨 Фронт (Nuxt 3 SSR)
- [ ] **UI/UX**
  - Tailwind + shadcn/ui для современных компонентов
  - Framer Motion / Motion Vue для анимаций
  - Nuxt Image для оптимизации картинок

- [ ] **PWA**
  - Офлайн-режим
  - Установка на рабочий стол
  - Push-уведомления о тренировках/скидках

- [ ] **SSR + SEO**
  - Мета-теги (`useHead`)
  - Sitemap/robots.txt
  - Lazy-loading компонентов

---

## 🛠 DevOps / Инфраструктура
- [ ] **Docker**
  - Сборка фронта и бэка в контейнеры
  - `docker-compose` для разработки и деплоя

- [ ] **CI/CD**
  - GitHub Actions для автотестов и деплоя
  - Автоматический деплой на сервер (VPS/Render/Heroku)

- [ ] **Мониторинг**
  - Sentry для ошибок
  - Prometheus + Grafana для метрик

- [ ] **Тестирование**
  - Pytest + coverage для Django
  - Vitest для Nuxt
