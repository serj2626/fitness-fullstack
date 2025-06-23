<script setup lang="ts">
import { api } from "~/api";
import { coaches } from "~/assets/data/moke.data";
import type { ICoachesListResponse } from "~/types";

const { $api } = useNuxtApp();

const { data: coachesData } = await useAsyncData<ICoachesListResponse>(
  "coaches-list-page-info",
  () => $api(api.coaches.list)
);

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
          <TrainerCard
            v-for="trainer in coachesData?.results"
            :key="trainer.id"
            :trainer
          />
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

<style scoped lang="scss">
.trainers-page {
  color: $txt;
}

.hero {
  background-color: $txt;
  color: $white;
  padding: 180px 0;
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
