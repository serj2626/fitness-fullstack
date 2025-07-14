<script setup lang="ts">
import type { IEequipmentResponse } from "~/types";
const tabs = ["Кардио-зона", "Силовая зона", "Групповые программы"];
const activeTab = ref(0);

defineProps<{ equipments: IEequipmentResponse[] }>();
</script>

<template>
  <section class="main-equipment-section">
    <div class="container">
      <h2 class="main-equipment-section__title">Наши залы и оборудование</h2>
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
            <img
              src="/first-section.jpg"
              alt="Силовая зона"
              class="gym-image"
            />
          </div>
        </div>
        <div v-if="activeTab === 2" class="gym-tab-content">
          <div class="gym-description">
            <h3>Групповые программы</h3>
            <p>
              Специально оборудованный зал для групповых занятий с
              профессиональным звуком, освещением и всем необходимым инвентарем.
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
</template>
<style scoped lang="scss">
.main-equipment-section {
  padding: 5rem 0;
  background: $bg;

  &__title {
    text-align: center;
    margin-bottom: 2rem;
    color: $accent;
    font-size: 2rem;
  }
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
</style>
