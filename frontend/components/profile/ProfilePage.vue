<script setup lang="ts">
import { breadcrumbsProfilePage } from '~/assets/data/breadcrumbs.data';
// Состояние активной вкладки
const activeTab = ref("visits");

// Данные пользователя
const user = ref({
  id: 1,
  name: "Иван Петров",
  avatar: "",
  membership: {
    type: "Премиум",
    expires: "2023-12-31",
    status: "active",
    freezeDaysUsed: 7,
  },
});

// Статистика
const stats = ref({
  visits: 24,
  trainings: 8,
  daysLeft: 45,
  freezeDays: 7,
});

// История посещений
const visits = ref([
  {
    id: 1,
    date: "2023-10-15",
    time: "18:00-19:30",
    trainer: "Алексей Смирнов",
    status: "completed",
  },
  {
    id: 2,
    date: "2023-10-12",
    time: "09:00-10:00",
    trainer: null,
    status: "completed",
  },
  {
    id: 3,
    date: "2023-10-10",
    time: "19:00-20:30",
    trainer: "Мария Иванова",
    status: "missed",
  },
]);

// История покупок
const purchases = ref([
  {
    id: 1,
    title: 'Абонемент "Премиум" на 3 месяца',
    date: "2023-09-01",
    price: 15000,
    status: "active",
  },
  {
    id: 2,
    title: "Персональные тренировки (10 занятий)",
    date: "2023-08-15",
    price: 20000,
    status: "active",
  },
  {
    id: 3,
    title: 'Абонемент "Стандарт" на 1 месяц',
    date: "2023-06-01",
    price: 6000,
    status: "expired",
  },
]);

// Персональные тренировки
const trainings = ref([
  {
    id: 1,
    title: "Силовая тренировка",
    date: "2023-10-15",
    trainer: "Алексей Смирнов",
    exercises: [
      { name: "Приседания со штангой", sets: 4, reps: 8, weight: 60 },
      { name: "Жим лежа", sets: 4, reps: 10, weight: 50 },
      { name: "Тяга штанги в наклоне", sets: 3, reps: 10, weight: 40 },
      { name: "Подтягивания", sets: 3, reps: "макс" },
    ],
  },
  {
    id: 2,
    title: "Функциональный тренинг",
    date: "2023-10-08",
    trainer: "Мария Иванова",
    exercises: [
      { name: "Берпи", sets: 4, reps: 15 },
      { name: "Прыжки на тумбу", sets: 3, reps: 10 },
      { name: "Гребля", sets: 3, reps: 20 },
      { name: "Фермерская прогулка", sets: 3, distance: "50м", weight: 24 },
    ],
  },
]);

// Уведомления
const notifications = ref([
  {
    id: 1,
    title: "Завтра тренировка",
    text: "Напоминаем, что завтра в 18:00 у вас запланирована персональная тренировка с Алексеем Смирновым",
    time: "2023-10-14T16:30:00",
    type: "info",
    read: false,
  },
  {
    id: 2,
    title: "Абонемент скоро закончится",
    text: "Ваш абонемент заканчивается через 7 дней. Продлите его, чтобы сохранить скидку",
    time: "2023-10-12T10:15:00",
    type: "warning",
    read: false,
  },
  {
    id: 3,
    title: "Заморозка абонемента подтверждена",
    text: "Ваш абонемент заморожен с 15.10.2023 по 25.10.2023",
    time: "2023-10-10T14:45:00",
    type: "info",
    read: true,
  },
]);

// Данные для заморозки
const freezeData = ref({
  reason: "",
  startDate: "",
  endDate: "",
  customReason: "",
});

// Вычисляемые свойства
const membershipStatus = computed(() => {
  return user.value.membership.status === "active"
    ? `Абонемент "${user.value.membership.type}" (до ${formatDate(
        user.value.membership.expires
      )})`
    : "Абонемент неактивен";
});

const unreadNotifications = computed(() => {
  return notifications.value.some((n) => !n.read);
});

const freezeDaysLeft = computed(() => {
  return 14 - user.value.membership.freezeDaysUsed;
});

// Методы
const formatDate = (dateString) => {
  const options = { day: "numeric", month: "long", year: "numeric" };
  return new Date(dateString).toLocaleDateString("ru-RU", options);
};

const formatTime = (dateTimeString) => {
  const date = new Date(dateTimeString);
  const now = new Date();
  const diffDays = Math.floor((now - date) / (1000 * 60 * 60 * 24));

  if (diffDays === 0) {
    return (
      "Сегодня в " +
      date.toLocaleTimeString("ru-RU", { hour: "2-digit", minute: "2-digit" })
    );
  } else if (diffDays === 1) {
    return (
      "Вчера в " +
      date.toLocaleTimeString("ru-RU", { hour: "2-digit", minute: "2-digit" })
    );
  } else {
    return date.toLocaleDateString("ru-RU", {
      day: "numeric",
      month: "long",
      hour: "2-digit",
      minute: "2-digit",
    });
  }
};

const notificationIcon = (type) => {
  const icons = {
    info: "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z",
    warning: "M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z",
    alert:
      "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z",
  };
  return icons[type] || icons.info;
};

const markAsRead = (id) => {
  const notification = notifications.value.find((n) => n.id === id);
  if (notification) notification.read = true;
};

const markAllAsRead = () => {
  notifications.value.forEach((n) => (n.read = true));
};

const submitFreeze = () => {
  // Здесь будет логика отправки формы
  alert("Запрос на заморозку отправлен");
  freezeData.value = {
    reason: "",
    startDate: "",
    endDate: "",
    customReason: "",
  };
};

const logout = () => {
  // Логика выхода
  alert("Вы вышли из системы");
};

// Загрузка данных при монтировании
onMounted(() => {
  // Здесь может быть запрос к API для получения данных
});
</script>
<template>
  <div class="user-profile">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="breadcrumbsProfilePage" />
      <!-- Шапка профиля -->
      <header class="user-profile__header">
        <h1 class="user-profile__title">Личный кабинет</h1>
        <BaseButton color="red" label="Выйти" :outline="true" @click="logout" />
      </header>

      <!-- Основное содержимое -->
      <div class="user-profile__content">
        <!-- Боковая панель -->
        <aside class="user-sidebar">
          <AvatarComponent
            first-name="Иван"
            last-name="Петров"
            :width="'100px'"
            :height="'100px'"
            class="user-sidebar__avatar"
          />
          <h2 class="user-sidebar__name">{{ user.name }}</h2>
          <div class="user-sidebar__membership">
            {{ membershipStatus }}
          </div>

          <!-- Статистика -->
          <div class="user-sidebar__stats">
            <div class="user-sidebar__stat">
              <div class="user-sidebar__stat-value">{{ stats.visits }}</div>
              <div class="user-sidebar__stat-label">Посещений</div>
            </div>
            <div class="user-sidebar__stat">
              <div class="user-sidebar__stat-value">{{ stats.trainings }}</div>
              <div class="user-sidebar__stat-label">Тренировки</div>
            </div>
            <div class="user-sidebar__stat">
              <div class="user-sidebar__stat-value">{{ stats.daysLeft }}</div>
              <div class="user-sidebar__stat-label">Дней осталось</div>
            </div>
            <div class="user-sidebar__stat">
              <div class="user-sidebar__stat-value">{{ stats.freezeDays }}</div>
              <div class="user-sidebar__stat-label">Заморожено</div>
            </div>
          </div>

          <!-- Навигация -->
          <ul class="user-sidebar__nav">
            <li class="user-sidebar__nav-item">
              <a
                href="#"
                class="user-sidebar__nav-link"
                :class="{ active: activeTab === 'visits' }"
                @click.prevent="activeTab = 'visits'"
              >
                История посещений
              </a>
            </li>
            <li class="user-sidebar__nav-item">
              <a
                href="#"
                class="user-sidebar__nav-link"
                :class="{ active: activeTab === 'purchases' }"
                @click.prevent="activeTab = 'purchases'"
              >
                Мои покупки
              </a>
            </li>
            <li class="user-sidebar__nav-item">
              <a
                href="#"
                class="user-sidebar__nav-link"
                :class="{ active: activeTab === 'trainings' }"
                @click.prevent="activeTab = 'trainings'"
              >
                Персональные тренировки
              </a>
            </li>
            <li class="user-sidebar__nav-item">
              <a
                href="#"
                class="user-sidebar__nav-link"
                :class="{ active: activeTab === 'notifications' }"
                @click.prevent="activeTab = 'notifications'"
              >
                Уведомления
                <span
                  v-if="unreadNotifications"
                  class="notifications__unread"
                ></span>
              </a>
            </li>
            <li class="user-sidebar__nav-item">
              <a
                href="#"
                class="user-sidebar__nav-link"
                :class="{ active: activeTab === 'freeze' }"
                @click.prevent="activeTab = 'freeze'"
              >
                Заморозка абонемента
              </a>
            </li>
          </ul>
        </aside>

        <!-- Основной контент -->
        <main class="user-main">
          <!-- История посещений -->
          <section class="user-main__section" v-if="activeTab === 'visits'">
            <div class="user-main__section-header">
              <h2 class="user-main__section-title">История посещений</h2>
              <div class="user-main__section-actions">
                <button class="user-main__btn">Экспорт</button>
              </div>
            </div>

            <div class="visits-history">
              <div
                class="visits-history__item"
                v-for="visit in visits"
                :key="visit.id"
              >
                <div>
                  <div class="visits-history__date">
                    {{ formatDate(visit.date) }}
                  </div>
                  <div class="visits-history__time">{{ visit.time }}</div>
                </div>
                <div class="visits-history__trainer" v-if="visit.trainer">
                  Тренер: {{ visit.trainer }}
                </div>
                <div
                  class="visits-history__status"
                  :class="`visits-history__status--${visit.status}`"
                >
                  {{ visit.status === "completed" ? "Посещено" : "Пропущено" }}
                </div>
              </div>
            </div>
          </section>

          <!-- История покупок -->
          <section class="user-main__section" v-if="activeTab === 'purchases'">
            <div class="user-main__section-header">
              <h2 class="user-main__section-title">Мои покупки</h2>
              <div class="user-main__section-actions">
                <button class="user-main__btn">Фильтры</button>
              </div>
            </div>

            <div class="purchases-history">
              <div
                class="purchases-history__item"
                v-for="purchase in purchases"
                :key="purchase.id"
              >
                <img
                  :src="purchase.image || '/membership-default.jpg'"
                  alt="Абонемент"
                  class="purchases-history__image"
                />
                <div class="purchases-history__info">
                  <h3 class="purchases-history__title">{{ purchase.title }}</h3>
                  <div class="purchases-history__date">
                    Куплен: {{ formatDate(purchase.date) }}
                  </div>
                  <div class="purchases-history__price">
                    {{ purchase.price }} ₽
                  </div>
                </div>
                <div
                  class="purchases-history__status"
                  :class="`purchases-history__status--${purchase.status}`"
                >
                  {{ purchase.status === "active" ? "Активен" : "Завершен" }}
                </div>
              </div>
            </div>
          </section>

          <!-- Персональные тренировки -->
          <section class="user-main__section" v-if="activeTab === 'trainings'">
            <div class="user-main__section-header">
              <h2 class="user-main__section-title">Персональные тренировки</h2>
              <div class="user-main__section-actions">
                <button class="user-main__btn">Записаться</button>
              </div>
            </div>

            <div class="trainings-history">
              <div
                class="trainings-history__item"
                v-for="training in trainings"
                :key="training.id"
              >
                <div class="trainings-history__header">
                  <div>
                    <h3 class="trainings-history__title">
                      {{ training.title }}
                    </h3>
                    <div class="trainings-history__trainer">
                      Тренер: {{ training.trainer }}
                    </div>
                  </div>
                  <div class="trainings-history__date">
                    {{ formatDate(training.date) }}
                  </div>
                </div>

                <div class="trainings-history__content">
                  <div
                    class="trainings-history__exercise"
                    v-for="(exercise, index) in training.exercises"
                    :key="index"
                  >
                    <div class="trainings-history__exercise-icon">
                      <svg width="20" height="20" viewBox="0 0 24 24">
                        <path
                          fill="currentColor"
                          d="M12 2L4 5v6.09c0 5.05 3.41 9.76 8 10.91c4.59-1.15 8-5.86 8-10.91V5l-8-3z"
                        />
                      </svg>
                    </div>
                    <div>
                      <div class="trainings-history__exercise-name">
                        {{ exercise.name }}
                      </div>
                      <div class="trainings-history__exercise-details">
                        {{ exercise.sets }} подходов ×
                        {{ exercise.reps }} повторений
                        <span v-if="exercise.weight"
                          >× {{ exercise.weight }} кг</span
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>

          <!-- Уведомления -->
          <section
            class="user-main__section"
            v-if="activeTab === 'notifications'"
          >
            <div class="user-main__section-header">
              <h2 class="user-main__section-title">Уведомления</h2>
              <div class="user-main__section-actions">
                <button class="user-main__btn" @click="markAllAsRead">
                  Прочитать все
                </button>
              </div>
            </div>

            <div class="notifications">
              <div
                class="notifications__item"
                v-for="notification in notifications"
                :key="notification.id"
                @click="markAsRead(notification.id)"
              >
                <div
                  class="notifications__icon"
                  :class="`notifications__icon--${notification.type}`"
                >
                  <svg width="20" height="20" viewBox="0 0 24 24">
                    <path
                      fill="currentColor"
                      :d="notificationIcon(notification.type)"
                    />
                  </svg>
                </div>
                <div class="notifications__content">
                  <h3 class="notifications__title">{{ notification.title }}</h3>
                  <p class="notifications__text">{{ notification.text }}</p>
                  <div class="notifications__time">
                    {{ formatTime(notification.time) }}
                  </div>
                </div>
                <span
                  v-if="!notification.read"
                  class="notifications__unread"
                ></span>
              </div>
            </div>
          </section>

          <!-- Заморозка абонемента -->
          <section class="user-main__section" v-if="activeTab === 'freeze'">
            <div class="user-main__section-header">
              <h2 class="user-main__section-title">Заморозка абонемента</h2>
            </div>

            <form class="freeze-form" @submit.prevent="submitFreeze">
              <div class="freeze-form__group">
                <label class="freeze-form__label">Причина заморозки</label>
                <select
                  class="freeze-form__select"
                  v-model="freezeData.reason"
                  required
                >
                  <option value="">Выберите причину</option>
                  <option value="vacation">Отпуск</option>
                  <option value="illness">Болезнь</option>
                  <option value="business">Командировка</option>
                  <option value="other">Другая причина</option>
                </select>
              </div>

              <div class="freeze-form__group">
                <label class="freeze-form__label">Дата начала</label>
                <input
                  type="date"
                  class="freeze-form__input"
                  v-model="freezeData.startDate"
                  required
                />
              </div>

              <div class="freeze-form__group">
                <label class="freeze-form__label">Дата окончания</label>
                <input
                  type="date"
                  class="freeze-form__input"
                  v-model="freezeData.endDate"
                  required
                />
              </div>

              <div
                class="freeze-form__group"
                v-if="freezeData.reason === 'other'"
              >
                <label class="freeze-form__label">Укажите причину</label>
                <textarea
                  class="freeze-form__input"
                  rows="3"
                  v-model="freezeData.customReason"
                ></textarea>
              </div>

              <button type="submit" class="freeze-form__submit">
                Отправить запрос
              </button>

              <div class="freeze-form__info">
                <p>Вы можете заморозить абонемент на срок от 7 до 30 дней.</p>
                <p>
                  Осталось дней для заморозки в этом месяце:
                  {{ freezeDaysLeft }} из 14
                </p>
              </div>
            </form>
          </section>
        </main>
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss">
.user-profile {
  padding-block: 100px;
  background-color: $bg;
  color: $white;
  min-height: 100vh;

  &__header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-block: 2.5rem;
    flex-wrap: wrap;
    gap: 1rem;
  }

  &__title {
    font-size: 2rem;
    font-weight: 700;
    color: $accent;
    margin: 0;
  }

  &__logout {
    background: rgba($red, 0.2);
    color: $white;
    border: 1px solid $red;
    padding: 0.5rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s ease;

    &:hover {
      background: $red;
    }
  }

  &__content {
    display: grid;
    grid-template-columns: 300px 1fr;
    gap: 2rem;

    @media (max-width: $tablet) {
      grid-template-columns: 1fr;
    }
  }
}

.user-sidebar {
  background: $bg_block;
  border-radius: 8px;
  padding: 1.5rem;
  height: fit-content;
  backdrop-filter: blur(10px);

  &__avatar {
    margin-inline: auto;
    margin-bottom: 20px;
  }

  &__name {
    text-align: center;
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
    color: $white;
  }

  &__membership {
    text-align: center;
    color: $accent;
    font-weight: 600;
    margin-bottom: 2rem;
  }

  &__stats {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-bottom: 2rem;
  }

  &__stat {
    background: rgba($white, 0.05);
    padding: 0.75rem;
    border-radius: 6px;
    text-align: center;

    &-value {
      font-size: 1.5rem;
      font-weight: 700;
      color: $accent;
      margin-bottom: 0.25rem;
    }

    &-label {
      font-size: 0.8rem;
      color: rgba($white, 0.7);
    }
  }

  &__nav {
    list-style: none;
    padding: 0;
    margin: 0;

    &-item {
      margin-bottom: 0.5rem;
    }

    &-link {
      display: block;
      padding: 0.75rem 1rem;
      color: $white;
      text-decoration: none;
      border-radius: 6px;
      transition: all 0.3s ease;
      font-weight: 500;

      &:hover,
      &.active {
        background: rgba($accent, 0.2);
        color: $accent;
      }

      &.active {
        border-left: 3px solid $accent;
      }
    }
  }
}

.user-main {
  &__section {
    background: $bg_block;
    border-radius: 8px;
    padding: 1.5rem;
    margin-bottom: 2rem;
    backdrop-filter: blur(10px);
  }

  &__section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
    border-bottom: 1px solid rgba($white, 0.1);
    padding-bottom: 1rem;
  }

  &__section-title {
    font-size: 1.5rem;
    margin: 0;
    color: $accent;
  }

  &__section-actions {
    display: flex;
    gap: 0.5rem;
  }

  &__btn {
    background: rgba($accent, 0.1);
    color: $accent;
    border: 1px solid $accent;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-size: 0.9rem;

    &:hover {
      background: $accent;
      color: $txt;
    }

    &--danger {
      background: rgba($red, 0.1);
      color: $red;
      border-color: $red;

      &:hover {
        background: $red;
        color: $white;
      }
    }
  }
}

.visits-history {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;

  &__item {
    background: rgba($white, 0.05);
    border-radius: 6px;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.3s ease;

    &:hover {
      background: rgba($white, 0.1);
    }
  }

  &__date {
    font-weight: 600;
    color: $accent;
  }

  &__time {
    color: rgba($white, 0.7);
    font-size: 0.9rem;
  }

  &__trainer {
    font-weight: 500;
  }

  &__status {
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    font-size: 0.8rem;
    font-weight: 500;

    &--completed {
      background: rgba(#4caf50, 0.2);
      color: #4caf50;
    }

    &--missed {
      background: rgba($red, 0.2);
      color: $red;
    }
  }
}

.purchases-history {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;

  &__item {
    background: rgba($white, 0.05);
    border-radius: 6px;
    padding: 1rem;
    display: grid;
    grid-template-columns: 80px 1fr auto;
    gap: 1.5rem;
    align-items: center;

    @media (max-width: $mobile) {
      grid-template-columns: 1fr;
    }
  }

  &__image {
    width: 80px;
    height: 80px;
    object-fit: cover;
    border-radius: 6px;
  }

  &__info {
    flex: 1;
  }

  &__title {
    font-weight: 600;
    margin-bottom: 0.5rem;
  }

  &__date {
    color: rgba($white, 0.7);
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
  }

  &__price {
    font-weight: 700;
    color: $accent;
    font-size: 1.2rem;
  }

  &__status {
    padding: 0.5rem;
    border-radius: 4px;
    font-weight: 500;
    text-align: center;

    &--active {
      background: rgba($accent, 0.2);
      color: $accent;
    }

    &--expired {
      background: rgba($grey, 0.3);
      color: $grey;
    }
  }
}

.trainings-history {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;

  &__item {
    background: rgba($white, 0.05);
    border-radius: 6px;
    padding: 1.5rem;
    transition: all 0.3s ease;

    &:hover {
      background: rgba($white, 0.1);
    }
  }

  &__header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 1rem;
  }

  &__title {
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: $accent;
  }

  &__trainer {
    color: rgba($white, 0.8);
    font-size: 0.9rem;
  }

  &__date {
    background: rgba($white, 0.1);
    padding: 0.25rem 0.75rem;
    border-radius: 4px;
    font-size: 0.9rem;
  }

  &__content {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;

    @media (max-width: $mobile) {
      grid-template-columns: 1fr;
    }
  }

  &__exercise {
    display: flex;
    gap: 0.75rem;
    padding: 0.5rem;
    border-radius: 4px;
    background: rgba($white, 0.03);
  }

  &__exercise-icon {
    color: $accent;
    font-size: 1.2rem;
    margin-top: 0.2rem;
  }

  &__exercise-name {
    font-weight: 500;
    margin-bottom: 0.25rem;
  }

  &__exercise-details {
    color: rgba($white, 0.7);
    font-size: 0.85rem;
  }
}

.notifications {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;

  &__item {
    background: rgba($white, 0.05);
    border-radius: 6px;
    padding: 1rem;
    display: flex;
    gap: 1rem;
    position: relative;
  }

  &__icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;

    &--info {
      background: rgba(#2196f3, 0.2);
      color: #2196f3;
    }

    &--warning {
      background: rgba($accent, 0.2);
      color: $accent;
    }

    &--alert {
      background: rgba($red, 0.2);
      color: $red;
    }
  }

  &__content {
    flex: 1;
  }

  &__title {
    font-weight: 600;
    margin-bottom: 0.25rem;
  }

  &__text {
    color: rgba($white, 0.8);
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
  }

  &__time {
    color: rgba($white, 0.5);
    font-size: 0.8rem;
  }

  &__unread {
    position: absolute;
    top: 1rem;
    right: 1rem;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: $accent;
  }
}

.freeze-form {
  &__group {
    margin-bottom: 1.5rem;
  }

  &__label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
  }

  &__input {
    width: 100%;
    padding: 0.75rem 1rem;
    background: rgba($white, 0.05);
    border: 1px solid rgba($white, 0.1);
    border-radius: 4px;
    color: $white;
    transition: all 0.3s ease;

    &:focus {
      border-color: $accent;
      outline: none;
    }
  }

  &__select {
    width: 100%;
    padding: 0.75rem 1rem;
    background: rgba($white, 0.05);
    border: 1px solid rgba($white, 0.1);
    border-radius: 4px;
    color: $white;
    appearance: none;
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='white'%3e%3cpath d='M7 10l5 5 5-5z'/%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 1rem center;
    background-size: 1rem;
    transition: all 0.3s ease;

    &:focus {
      border-color: $accent;
      outline: none;
    }
  }

  &__submit {
    background: $accent;
    color: $txt;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
    font-weight: 600;
    transition: all 0.3s ease;

    &:hover {
      opacity: 0.9;
    }
  }

  &__info {
    margin-top: 1.5rem;
    padding: 1rem;
    background: rgba($white, 0.05);
    border-radius: 4px;
    font-size: 0.9rem;
    color: rgba($white, 0.8);
  }
}

@media (max-width: $tablet) {
  .user-profile {
    &__content {
      grid-template-columns: 1fr;
    }
  }

  .user-sidebar {
    &__stats {
      grid-template-columns: repeat(4, 1fr);
    }
  }
}

@media (max-width: $mobile) {
  .user-sidebar {
    &__stats {
      grid-template-columns: repeat(2, 1fr);
    }
  }
}
</style>
