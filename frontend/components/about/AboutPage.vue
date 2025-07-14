<script setup lang="ts">
import { ref } from "vue";

const activeTab = ref(0);
const tabs = ["Кардио-зона", "Силовая зона", "Групповые программы"];

const team = ref([
  {
    name: "Алексей Смирнов",
    position: "Главный тренер",
    experience: "Опыт: 12 лет",
    specialties: ["Силовой тренинг", "Кроссфит", "Подготовка к соревнованиям"],
    photo: "/trainer1.jpg",
  },
  {
    name: "Мария Иванова",
    position: "Тренер групповых программ",
    experience: "Опыт: 8 лет",
    specialties: ["Пилатес", "Йога", "Функциональный тренинг"],
    photo: "/trainer2.jpg",
  },
  {
    name: "Дмитрий Петров",
    position: "Тренер по боксу",
    experience: "Опыт: 10 лет",
    specialties: ["Бокс", "Кикбоксинг", "Самооборона"],
    photo: "/trainer3.jpg",
  },
  {
    name: "Анна Козлова",
    position: "Тренер по растяжке",
    experience: "Опыт: 6 лет",
    specialties: ["Стретчинг", "Гибкость", "Партерная гимнастика"],
    photo: "/trainer4.jpg",
  },
]);
</script>
<template>
  <div class="about-page">
    <!-- Герой-секция -->
    <section class="about-hero">
      <div class="about-hero__content">
        <h1 class="about-hero__title">Наш клуб — это больше чем спорт</h1>
        <p class="about-hero__subtitle">
          Место, где рождаются победы и меняются жизни
        </p>
      </div>
    </section>

    <!-- О клубе -->
    <section class="about-section">
      <div class="container">
        <div class="about-grid">
          <div class="about-grid__content">
            <h2 class="about-title">О нашем клубе</h2>
            <div class="about-text">
              <p>
                Мы создали пространство, где каждый может найти свой путь к
                здоровью и совершенству. Наш клуб объединяет профессионалов
                фитнес-индустрии и тех, кто только начинает свой спортивный
                путь.
              </p>
              <p>
                С 2010 года мы помогаем нашим клиентам достигать своих целей,
                используя современные методики тренировок и индивидуальный
                подход.
              </p>
            </div>
            <ul class="about-features">
              <li class="about-feature">
                <div class="about-feature__icon">
                  <svg width="32" height="32" viewBox="0 0 24 24">
                    <path
                      fill="#ffc451"
                      d="M12 3L2 12h3v8h6v-6h2v6h6v-8h3L12 3zm0 4.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5z"
                    />
                  </svg>
                </div>
                <div class="about-feature__text">
                  <h3>3 этажа</h3>
                  <p>Современных тренировочных зон</p>
                </div>
              </li>
              <li class="about-feature">
                <div class="about-feature__icon">
                  <svg width="32" height="32" viewBox="0 0 24 24">
                    <path
                      fill="#ffc451"
                      d="M12 6v3l4-4-4-4v3c-4.42 0-8 3.58-8 8 0 1.57.46 3.03 1.24 4.26L6.7 14.8c-.45-.83-.7-1.79-.7-2.8 0-3.31 2.69-6 6-6zm6.76 1.74L17.3 9.2c.44.84.7 1.79.7 2.8 0 3.31-2.69 6-6 6v-3l-4 4 4 4v-3c4.42 0 8-3.58 8-8 0-1.57-.46-3.03-1.24-4.26z"
                    />
                  </svg>
                </div>
                <div class="about-feature__text">
                  <h3>20+ направлений</h3>
                  <p>Групповых и индивидуальных тренировок</p>
                </div>
              </li>
              <li class="about-feature">
                <div class="about-feature__icon">
                  <svg width="32" height="32" viewBox="0 0 24 24">
                    <path
                      fill="#ffc451"
                      d="M17 10.5V7c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1v-3.5l4 4v-11l-4 4zM14 13h-3v3H9v-3H6v-2h3V8h2v3h3v2z"
                    />
                  </svg>
                </div>
                <div class="about-feature__text">
                  <h3>5000+</h3>
                  <p>Довольных клиентов</p>
                </div>
              </li>
            </ul>
          </div>
          <div class="about-grid__image">
            <img
              src="/first-section.jpg"
              alt="Интерьер клуба"
              class="about-image"
            />
          </div>
        </div>
      </div>
    </section>

    <!-- Наши преимущества -->
    <section class="advantages-section">
      <div class="container">
        <h2 class="section-title">Наши преимущества</h2>
        <div class="advantages-grid">
          <div class="advantage-card">
            <div class="advantage-card__icon">
              <svg width="48" height="48" viewBox="0 0 24 24">
                <path
                  fill="#ffc451"
                  d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"
                />
              </svg>
            </div>
            <h3 class="advantage-card__title">Профессиональные тренеры</h3>
            <p class="advantage-card__text">
              Все наши специалисты имеют международные сертификации и минимум 5
              лет опыта работы
            </p>
          </div>
          <div class="advantage-card">
            <div class="advantage-card__icon">
              <svg width="48" height="48" viewBox="0 0 24 24">
                <path
                  fill="#ffc451"
                  d="M19 3h-4.18C14.4 1.84 13.3 1 12 1c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm0 4c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm6 12H6v-1.4c0-2 4-3.1 6-3.1s6 1.1 6 3.1V19z"
                />
              </svg>
            </div>
            <h3 class="advantage-card__title">Индивидуальный подход</h3>
            <p class="advantage-card__text">
              Персональные программы тренировок и питания для каждого клиента
            </p>
          </div>
          <div class="advantage-card">
            <div class="advantage-card__icon">
              <svg width="48" height="48" viewBox="0 0 24 24">
                <path
                  fill="#ffc451"
                  d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.31-8.86c-1.77-.45-2.34-.94-2.34-1.67 0-.84.79-1.43 2.1-1.43 1.38 0 1.9.66 1.94 1.64h1.71c-.05-1.34-.87-2.57-2.49-2.97V5H10.9v1.69c-1.51.32-2.72 1.3-2.72 2.81 0 1.79 1.49 2.69 3.66 3.21 1.95.46 2.34 1.15 2.34 1.87 0 .53-.39 1.39-2.1 1.39-1.6 0-2.23-.72-2.32-1.64H8.04c.1 1.7 1.36 2.66 2.86 2.97V19h2.34v-1.67c1.52-.29 2.72-1.16 2.73-2.77-.01-2.2-1.9-2.96-3.66-3.42z"
                />
              </svg>
            </div>
            <h3 class="advantage-card__title">Гибкая система лояльности</h3>
            <p class="advantage-card__text">
              Скидки, заморозки и бонусы для наших постоянных клиентов
            </p>
          </div>
          <div class="advantage-card">
            <div class="advantage-card__icon">
              <svg width="48" height="48" viewBox="0 0 24 24">
                <path
                  fill="#ffc451"
                  d="M18 8c0-3.31-2.69-6-6-6S6 4.69 6 8c0 4.5 6 11 6 11s6-6.5 6-11zm-8 0c0-1.1.9-2 2-2s2 .9 2 2-.89 2-2 2c-1.1 0-2-.9-2-2zM5 20v2h14v-2H5z"
                />
              </svg>
            </div>
            <h3 class="advantage-card__title">Удобное расположение</h3>
            <p class="advantage-card__text">
              Центр города, собственная парковка и легкая доступность на
              общественном транспорте
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Залы и оборудование -->
    <section class="gym-section">
      <div class="container">
        <h2 class="section-title">Наши залы и оборудование</h2>
        <div class="gym-tabs">
          <button
            v-for="(tab, index) in tabs"
            :key="index"
            :class="['gym-tab', { active: activeTab === index }]"
            @click="activeTab = index"
          >
            {{ tab }}
          </button>
        </div>
        <div class="gym-content">
          <div v-if="activeTab === 0" class="gym-tab-content">
            <div class="gym-description">
              <h3>Кардио-зона</h3>
              <p>
                Просторная зона с современными кардио-тренажерами от ведущих
                мировых производителей. Беговые дорожки с амортизацией, эллипсы,
                велотренажеры и гребные тренажеры.
              </p>
              <ul class="gym-equipment">
                <li>12 беговых дорожек TechnoGym</li>
                <li>8 эллиптических тренажеров Life Fitness</li>
                <li>6 велотренажеров Matrix</li>
                <li>4 гребных тренажера Concept2</li>
              </ul>
            </div>
            <div class="gym-slider">
              <img src="/first-section.jpg" alt="Кардио-зона" class="gym-image" />
            </div>
          </div>
          <div v-if="activeTab === 1" class="gym-tab-content">
            <div class="gym-description">
              <h3>Силовая зона</h3>
              <p>
                Полностью укомплектованная зона для силовых тренировок с
                профессиональным оборудованием Hammer Strength, TechnoGym и
                Eleiko.
              </p>
              <ul class="gym-equipment">
                <li>Мультистанции Hammer Strength</li>
                <li>Свободные веса до 50 кг</li>
                <li>Функциональные рамы Eleiko</li>
                <li>Зона CrossFit с покрытием</li>
              </ul>
            </div>
            <div class="gym-slider">
              <img src="/first-section.jpg" alt="Силовая зона" class="gym-image" />
            </div>
          </div>
          <div v-if="activeTab === 2" class="gym-tab-content">
            <div class="gym-description">
              <h3>Групповые программы</h3>
              <p>
                Специально оборудованный зал для групповых занятий с
                профессиональным звуком, освещением и всем необходимым
                инвентарем.
              </p>
              <ul class="gym-equipment">
                <li>Зал 150 м² с амортизирующим покрытием</li>
                <li>Система зеркал и хореографических станков</li>
                <li>Полный набор оборудования для функционального тренинга</li>
                <li>Профессиональная аудиосистема</li>
              </ul>
            </div>
            <div class="gym-slider">
              <img
                src="/first-section.jpg"
                alt="Групповые программы"
                class="gym-image"
              />
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Команда -->
    <section class="team-section">
      <div class="container">
        <h2 class="section-title">Наша команда</h2>
        <p class="section-subtitle">
          Профессионалы с международным опытом и любовью к своему делу
        </p>
        <div class="team-grid">
          <div v-for="(member, index) in team" :key="index" class="team-card">
            <img
              :src="member.photo"
              :alt="member.name"
              class="team-card__image"
            />
            <div class="team-card__content">
              <h3 class="team-card__name">{{ member.name }}</h3>
              <p class="team-card__position">{{ member.position }}</p>
              <p class="team-card__experience">{{ member.experience }}</p>
              <ul class="team-card__specialties">
                <li v-for="(specialty, i) in member.specialties" :key="i">
                  {{ specialty }}
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Контакты -->
    <section class="contacts-section">
      <div class="container">
        <div class="contacts-grid">
          <div class="contacts-info">
            <h2 class="section-title">Контакты</h2>
            <div class="contacts-item">
              <svg width="24" height="24" viewBox="0 0 24 24">
                <path
                  fill="#ffc451"
                  d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"
                />
              </svg>
              <p>г. Москва, ул. Спортивная, 15</p>
            </div>
            <div class="contacts-item">
              <svg width="24" height="24" viewBox="0 0 24 24">
                <path
                  fill="#ffc451"
                  d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"
                />
              </svg>
              <p>info@fitnessclub.ru</p>
            </div>
            <div class="contacts-item">
              <svg width="24" height="24" viewBox="0 0 24 24">
                <path
                  fill="#ffc451"
                  d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56-.35-.12-.74-.03-1.01.24l-1.57 1.97c-2.83-1.35-5.48-3.9-6.89-6.83l1.95-1.66c.27-.28.35-.67.24-1.02-.37-1.11-.56-2.3-.56-3.53 0-.54-.45-.99-.99-.99H4.19C3.65 3 3 3.24 3 3.99 3 13.28 10.73 21 20.01 21c.71 0 .99-.63.99-1.18v-3.45c0-.54-.45-.99-.99-.99z"
                />
              </svg>
              <p>+7 (495) 123-45-67</p>
            </div>
            <div class="contacts-item">
              <svg width="24" height="24" viewBox="0 0 24 24">
                <path
                  fill="#ffc451"
                  d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"
                />
              </svg>
              <p>Пн-Пт: 7:00 - 23:00<br />Сб-Вс: 8:00 - 22:00</p>
            </div>
            <button class="contacts-button">Записаться на экскурсию</button>
          </div>
          <div class="contacts-map">
            <iframe
              src="https://yandex.ru/map-widget/v1/?um=constructor%3A8a1d8f1b1b1b1b1b1b1b1b1b1b1b1b1b1b1&amp;source=constructor"
              width="100%"
              height="100%"
              frameborder="0"
            ></iframe>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped lang="scss">
/* Основные стили страницы */
.about-page {
  color: $white;
  background-color: $bg;
}

.container {
  max-width: $desktop;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.section-title {
  font-size: 2rem;
  color: $accent;
  text-align: center;
  margin-bottom: 1.5rem;
  position: relative;

  &::after {
    content: "";
    display: block;
    width: 80px;
    height: 3px;
    background: $accent;
    margin: 1rem auto 0;
  }
}

.section-subtitle {
  text-align: center;
  font-size: 1.2rem;
  color: rgba($white, 0.8);
  max-width: 800px;
  margin: 0 auto 3rem;
}

/* Герой секция */
.about-hero {
  height: 60vh;
  min-height: 500px;
  background: linear-gradient(rgba($bg, 0.7), rgba($bg, 0.7)),
    url("/gym-hero.jpg") center/cover no-repeat;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 2rem;

  &__content {
    max-width: 800px;
  }

  &__title {
    font-size: 3rem;
    color: $white;
    margin-bottom: 1.5rem;
    line-height: 1.2;

    @media (max-width: $tablet) {
      font-size: 2.5rem;
    }
  }

  &__subtitle {
    font-size: 1.5rem;
    color: $accent;
    font-weight: 300;

    @media (max-width: $tablet) {
      font-size: 1.2rem;
    }
  }
}

/* О клубе */
.about-section {
  padding: 5rem 0;
  background: $bg_block;
}

.about-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;

  @media (max-width: $tablet) {
    grid-template-columns: 1fr;
  }

  &__image {
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  }
}

.about-title {
  font-size: 2rem;
  color: $accent;
  margin-bottom: 1.5rem;
}

.about-text {
  margin-bottom: 2rem;
  line-height: 1.6;

  p {
    margin-bottom: 1rem;
  }
}

.about-image {
  width: 100%;
  height: auto;
  display: block;
  transition: transform 0.5s ease;

  &:hover {
    transform: scale(1.03);
  }
}

.about-features {
  list-style: none;
  padding: 0;
  margin: 2rem 0 0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;

  @media (max-width: $mobile) {
    grid-template-columns: 1fr;
  }
}

.about-feature {
  display: flex;
  gap: 1rem;
  align-items: flex-start;
  background: rgba($white, 0.05);
  padding: 1.5rem;
  border-radius: 8px;
  transition: all 0.3s ease;

  &:hover {
    background: rgba($accent, 0.1);
    transform: translateY(-5px);
  }

  &__icon {
    flex-shrink: 0;
  }

  &__text {
    h3 {
      margin: 0 0 0.5rem;
      color: $accent;
      font-size: 1.3rem;
    }

    p {
      margin: 0;
      color: rgba($white, 0.7);
      font-size: 0.9rem;
    }
  }
}

/* Преимущества */
.advantages-section {
  padding: 5rem 0;
  background: url("/pattern.png") center/cover;
}

.advantages-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-top: 3rem;
}

.advantage-card {
  background: $bg_block;
  padding: 2rem;
  border-radius: 8px;
  text-align: center;
  transition: all 0.3s ease;
  border-bottom: 3px solid transparent;

  &:hover {
    transform: translateY(-10px);
    border-bottom-color: $accent;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  }

  &__icon {
    margin-bottom: 1.5rem;
  }

  &__title {
    color: $accent;
    margin-bottom: 1rem;
    font-size: 1.3rem;
  }

  &__text {
    color: rgba($white, 0.8);
    line-height: 1.6;
    margin: 0;
  }
}

/* Залы и оборудование */
.gym-section {
  padding: 5rem 0;
  background: $bg_block;
}

.gym-tabs {
  display: flex;
  justify-content: center;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.gym-tab {
  background: transparent;
  color: $white;
  border: none;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  cursor: pointer;
  border-radius: 4px;
  transition: all 0.3s ease;
  position: relative;

  &:hover {
    color: $accent;
  }

  &.active {
    color: $accent;
    font-weight: 600;

    &::after {
      content: "";
      position: absolute;
      bottom: -8px;
      left: 50%;
      transform: translateX(-50%);
      width: 50%;
      height: 2px;
      background: $accent;
    }
  }
}

.gym-content {
  background: rgba($white, 0.05);
  border-radius: 8px;
  overflow: hidden;
}

.gym-tab-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 400px;

  @media (max-width: $tablet) {
    grid-template-columns: 1fr;
  }
}

.gym-description {
  padding: 2rem;

  h3 {
    color: $accent;
    font-size: 1.5rem;
    margin-top: 0;
  }

  p {
    line-height: 1.6;
    margin-bottom: 1.5rem;
  }
}

.gym-equipment {
  list-style: none;
  padding: 0;
  margin: 1.5rem 0 0;

  li {
    position: relative;
    padding-left: 1.5rem;
    margin-bottom: 0.5rem;

    &::before {
      content: "";
      position: absolute;
      left: 0;
      top: 0.6em;
      width: 8px;
      height: 8px;
      background: $accent;
      border-radius: 50%;
    }
  }
}

.gym-slider {
  position: relative;
  overflow: hidden;

  @media (max-width: $tablet) {
    height: 300px;
  }
}

.gym-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;

  &:hover {
    transform: scale(1.05);
  }
}

/* Команда */
.team-section {
  padding: 5rem 0;
  background: url("/team-bg.jpg") center/cover fixed;
  position: relative;

  &::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba($bg, 0.9);
    z-index: 0;
  }
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  position: relative;
  z-index: 1;
}

.team-card {
  background: $bg_block;
  border-radius: 8px;
  overflow: hidden;
  transition: all 0.3s ease;

  &:hover {
    transform: translateY(-10px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
  }

  &__image {
    width: 100%;
    height: 300px;
    object-fit: cover;
    display: block;
  }

  &__content {
    padding: 1.5rem;
  }

  &__name {
    color: $accent;
    margin: 0 0 0.5rem;
    font-size: 1.3rem;
  }

  &__position {
    color: $white;
    font-weight: 500;
    margin: 0 0 0.5rem;
  }

  &__experience {
    color: rgba($white, 0.7);
    font-size: 0.9rem;
    margin: 0 0 1rem;
  }

  &__specialties {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;

    li {
      background: rgba($accent, 0.1);
      color: $accent;
      padding: 0.25rem 0.5rem;
      border-radius: 4px;
      font-size: 0.8rem;
    }
  }
}

/* Контакты */
.contacts-section {
  padding: 5rem 0;
  background: $bg_block;
}

.contacts-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;

  @media (max-width: $tablet) {
    grid-template-columns: 1fr;
  }
}

.contacts-info {
  @media (max-width: $tablet) {
    order: 2;
  }
}

.contacts-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;

  p {
    margin: 0;
    line-height: 1.6;
  }
}

.contacts-button {
  background: $accent;
  color: $txt;
  border: none;
  padding: 1rem 2rem;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 1.5rem;
  display: inline-block;

  &:hover {
    background: darken($accent, 10%);
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba($accent, 0.3);
  }
}

.contacts-map {
  height: 400px;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);

  iframe {
    filter: grayscale(30%) contrast(90%);
    transition: filter 0.3s ease;
  }

  &:hover iframe {
    filter: grayscale(0%) contrast(100%);
  }

  @media (max-width: $tablet) {
    order: 1;
    height: 300px;
  }
}
</style>
