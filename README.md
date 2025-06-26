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
