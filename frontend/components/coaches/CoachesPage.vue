<!-- <script lang="ts" setup>
import { coaches } from "~/assets/data/moke.data";
</script>

<template>
  <div class="coaches-page">
    <div class="container">
      <div class="coaches-page__search">
        <p class="coaches-page__search-title">Найти своего тренера</p>
        <form class="coaches-page__search-form">
          <div class="coaches-page__search-form-group">
            <label for="select">Выберите направление</label>
            <select id="select">
              <option value="">Все направления</option>
              <option value="month">Фитнес тренер</option>
              <option value="quarter">Инструктор по йоге</option>
              <option value="year">Инструктор по плаванию</option>
              <option value="year">Тренер по боксу</option>
            </select>
          </div>
          <div class="coaches-page__search-form-actions">
            <BaseButton
              class="coaches-page__search-form-actions-submit"
              size="md"
              label="Найти"
            />
            <BaseButton size="md" label="Сбросить" />
          </div>
        </form>
      </div>
      <ul class="coaches-page__content-list">
        <CoachesCard v-for="coach in coaches" :key="coach.id" :coach="coach" />
      </ul>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.coaches-page {
  padding-block: 100px;

  &__search {
    position: static;
    top: 20px;
    z-index: 90;

    @include mediaLaptop {
      position: sticky;
    }

    padding: 50px;
    margin-block: 50px 100px;
    display: flex;
    flex-direction: column;
    gap: 40px;
    border-radius: 15px;
    background-color: $bg;
    box-shadow: 0 0 10px white;

    &-form {
      display: flex;
      align-items: center;
      justify-content: space-between;
      color: $white;

      &-group {
        display: flex;
        flex-direction: column;
        gap: 10px;
      }
      &-actions {
        display: flex;
        gap: 10px;
        align-items: center;
        &-submit {
          background-color: $accent;
          color: $txt;
        }
      }
    }
    &-title {
      font-size: 35px;
      color: $accent;
      text-transform: uppercase;
    }
  }

  &__title {
    font-size: 50px;
    color: $accent;
    text-align: center;
  }

  &__content {
    display: grid;
    grid-template-columns: 1fr 3fr;
    gap: 30px; // расстояние между колонками
    margin-top: 150px;

    &-search {
      position: sticky;
      top: 100px;
      align-self: start;
      color: $white;
      &-close {
        position: relative;
        margin-top: 60px;
        display: flex;
        align-items: center;
        justify-content: end;
        gap: 10px;
        font-size: 17px;
        font-weight: 500;

        &::before {
          content: "";
          position: absolute;
          bottom: -5px;
          left: 0;
          width: 100%;
          height: 2px;
          background-color: $white;
        }
      }
      &-list {
        display: flex;
        flex-direction: column;
        gap: 15px;
        & li {
          padding: 10px 15px;
          border-radius: 10px;
          cursor: pointer;
          background-color: rgb(101, 95, 95);
          border: none;
          transition: all 0.3s ease-in;

          &:hover {
            box-shadow: 0 0 10px #fdfdfd98;
          }
        }
      }
    }

    &-list {
      display: grid;
      grid-template-columns: 1fr;
      gap: 10px;
      @include mediaTablet{
        grid-template-columns: repeat(2, 1fr);
      }
      @include mediaLaptop{
        grid-template-columns: repeat(3, 1fr);
      }
    }
  }
}

.coaches-page__content-search-close:hover::before {
  transition: all 0.3s ease-in;
  width: 0;
}
</style> -->

<template>
  <div class="trainers-page">
    <!-- Шапка -->
    <section class="hero">
      <div class="container">
        <h1>НАШИ ТРЕНЕРЫ</h1>
        <p>Профессионалы, которые выжмут из тебя все соки</p>
      </div>
    </section>

    <!-- Основной контент -->
    <main class="main-content">
      <div class="container">
        <!-- Фильтры -->
        <div class="filters">
          <button
            v-for="category in categories"
            :key="category.id"
            @click="setActiveCategory(category.id)"
            :class="{ active: activeCategory === category.id }"
          >
            {{ category.name }}
          </button>
        </div>

        <!-- Сетка тренеров -->
        <div class="trainers-grid">
          <div
            v-for="trainer in filteredTrainers"
            :key="trainer.id"
            class="trainer-card"
            @click="openModal(trainer)"
          >
            <div class="trainer-image">
              <img :src="trainer.photo" :alt="trainer.name" />
              <span class="specialization">{{ trainer.specialization }}</span>
            </div>
            <div class="trainer-info">
              <h3>{{ trainer.name }}</h3>
              <p class="experience">{{ trainer.experience }} лет опыта</p>
              <p class="bio">{{ trainer.short_bio }}</p>
              <button
                @click="$router.push(`/coaches/${trainer.id}`)"
                class="btn-book"
              >
                Профиль
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- Модальное окно -->
    <div v-if="selectedTrainer" class="modal" :class="{ active: isModalOpen }">
      <div class="modal-overlay" @click="closeModal"></div>
      <div class="modal-content">
        <button class="modal-close" @click="closeModal">&times;</button>
        <div class="modal-body">
          <div class="modal-image">
            <img :src="selectedTrainer.photo" :alt="selectedTrainer.name" />
          </div>
          <div class="modal-info">
            <h2>{{ selectedTrainer.name }}</h2>
            <p class="specialization">{{ selectedTrainer.specialization }}</p>

            <div class="details">
              <div class="detail-item">
                <span class="detail-label">Опыт:</span>
                <span class="detail-value"
                  >{{ selectedTrainer.experience }} лет</span
                >
              </div>
              <div class="detail-item">
                <span class="detail-label">Направления:</span>
                <span class="detail-value">{{
                  selectedTrainer.directions.join(", ")
                }}</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Сертификаты:</span>
                <span class="detail-value">{{
                  selectedTrainer.certificates.join(", ")
                }}</span>
              </div>
            </div>

            <p class="full-bio">{{ selectedTrainer.full_bio }}</p>

            <div class="modal-actions">
              <button class="btn-primary">Записаться на тренировку</button>
              <div class="social-links">
                <a
                  v-if="selectedTrainer.social_instagram"
                  :href="selectedTrainer.social_instagram"
                  target="_blank"
                >
                  <i class="icon-instagram"></i>
                </a>
                <a
                  v-if="selectedTrainer.social_telegram"
                  :href="selectedTrainer.social_telegram"
                  target="_blank"
                >
                  <i class="icon-telegram"></i>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// Имитация данных из API Django
const trainers = ref([
  {
    id: 1,
    name: "Алексей Иванов",
    photo: "/coaches/eight.jpeg",
    specialization: "Силовой тренинг",
    experience: 8,
    short_bio: "Сделает из тебя машину за 3 месяца",
    full_bio:
      "Мастер спорта по пауэрлифтингу. Тренерский стаж 8 лет. Специализация: силовые тренировки, коррекция фигуры, подготовка к соревнованиям.",
    directions: ["Пауэрлифтинг", "Бодибилдинг", "Кроссфит"],
    certificates: ["FPA", "ACSM", "NASM"],
    social_instagram: "https://instagram.com",
    social_telegram: "https://t.me",
    category: "strength",
  },
  {
    id: 2,
    name: "Мария Петрова",
    photo: "/coaches/nine.jpeg",
    specialization: "Йога",
    experience: 5,
    short_bio: "Научит тебя гибкости и балансу",
    full_bio:
      "Сертифицированный инструктор по йоге (RYT 500). Практикует более 10 лет. Проводит занятия по хатха-йоге, виньяса-флоу и йоге для начинающих.",
    directions: ["Хатха-йога", "Виньяса", "Йогатерапия"],
    certificates: ["RYT 500", "Yoga Alliance"],
    social_instagram: "https://instagram.com",
    category: "yoga",
  },
  // Добавьте остальных тренеров...
]);

const categories = ref([
  { id: "all", name: "Все тренеры" },
  { id: "strength", name: "Силовые" },
  { id: "yoga", name: "Йога" },
  { id: "crossfit", name: "Кроссфит" },
  { id: "boxing", name: "Бокс" },
]);

const activeCategory = ref("all");
const isModalOpen = ref(false);
const selectedTrainer = ref(null);

const filteredTrainers = computed(() => {
  if (activeCategory.value === "all") return trainers.value;
  return trainers.value.filter(
    (trainer) => trainer.category === activeCategory.value
  );
});

const setActiveCategory = (categoryId) => {
  activeCategory.value = categoryId;
};

const openModal = (trainer) => {
  selectedTrainer.value = trainer;
  isModalOpen.value = true;
  document.body.style.overflow = "hidden";
};

const closeModal = () => {
  isModalOpen.value = false;
  document.body.style.overflow = "auto";
};
</script>

<style scoped lang="scss">
.trainers-page {
  font-family: "Roboto", sans-serif;
  color: $txt;
}

.container {
  max-width: $desktop;
  margin: 0 auto;
  padding: 0 20px;
}

.hero {
  background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)),
    url("/images/trainers-bg.jpg") center/cover;
  color: $white;
  padding: 100px 0;
  text-align: center;

  h1 {
    font-size: 3rem;
    margin-bottom: 20px;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: $accent;
  }

  p {
    font-size: 1.2rem;
    opacity: 0.9;
  }
}

.main-content {
  padding: 60px 0;
}

.filters {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 40px;
  justify-content: center;

  button {
    background: none;
    border: 1px solid $grey;
    padding: 8px 20px;
    border-radius: 20px;
    cursor: pointer;
    transition: all 0.3s;
    font-weight: 500;

    &.active,
    &:hover {
      background: $accent;
      border-color: $accent;
      color: $txt;
    }
  }
}

.trainers-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 30px;

  @media (max-width: $tablet) {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  }

  @media (max-width: $mobile) {
    grid-template-columns: 1fr;
  }
}

.trainer-card {
  background: $white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 5px 15px rgba(255, 243, 243, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
  cursor: pointer;

  &:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
  }
}

.trainer-image {
  position: relative;
  height: 300px;
  overflow: hidden;

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s;
  }

  .specialization {
    position: absolute;
    bottom: 20px;
    left: 20px;
    background: $accent;
    color: $txt;
    padding: 5px 15px;
    border-radius: 20px;
    font-weight: 600;
  }

  &:hover img {
    transform: scale(1.05);
  }
}

.trainer-info {
  padding: 20px;

  h3 {
    font-size: 1.4rem;
    margin-bottom: 5px;
  }

  .experience {
    color: $grey;
    margin-bottom: 10px;
    font-size: 0.9rem;
  }

  .bio {
    color: $grey;
    margin-bottom: 20px;
    line-height: 1.5;
  }
}

.btn-book {
  width: 100%;
  background: $accent;
  color: $txt;
  border: none;
  padding: 12px;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.3s;
  text-transform: uppercase;
  letter-spacing: 1px;

  &:hover {
    background: darken($accent, 10%);
  }
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s;

  &.active {
    opacity: 1;
    pointer-events: all;
  }
}

.modal-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
}

.modal-content {
  background: $white;
  border-radius: 8px;
  max-width: 900px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
  z-index: 2;
}

.modal-close {
  position: absolute;
  top: 20px;
  right: 20px;
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: $grey;
  transition: color 0.3s;

  &:hover {
    color: $error;
  }
}

.modal-body {
  display: flex;
  padding: 40px;

  @media (max-width: $tablet) {
    flex-direction: column;
  }
}

.modal-image {
  flex: 1;
  min-width: 300px;
  margin-right: 40px;

  img {
    width: 100%;
    height: auto;
    border-radius: 8px;
  }

  @media (max-width: $tablet) {
    margin-right: 0;
    margin-bottom: 30px;
  }
}

.modal-info {
  flex: 2;

  h2 {
    font-size: 2rem;
    margin-bottom: 10px;
  }

  .specialization {
    color: $accent;
    font-weight: 600;
    margin-bottom: 20px;
    display: inline-block;
  }
}

.details {
  margin-bottom: 30px;

  .detail-item {
    margin-bottom: 10px;
    display: flex;
  }

  .detail-label {
    font-weight: 600;
    min-width: 120px;
    color: $grey;
  }

  .detail-value {
    flex: 1;
  }
}

.full-bio {
  line-height: 1.8;
  margin-bottom: 30px;
}

.modal-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.btn-primary {
  background: $accent;
  color: $txt;
  border: none;
  padding: 12px 24px;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;

  &:hover {
    background: darken($accent, 10%);
  }
}

.social-links {
  display: flex;
  gap: 15px;

  a {
    color: $grey;
    font-size: 1.5rem;
    transition: color 0.3s;

    &:hover {
      color: $accent;
    }
  }
}
</style>
