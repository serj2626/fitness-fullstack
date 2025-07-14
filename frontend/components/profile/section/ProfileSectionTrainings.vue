<script setup lang="ts"></script>
<template>
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
                {{ exercise.sets }} подходов × {{ exercise.reps }} повторений
                <span v-if="exercise.weight">× {{ exercise.weight }} кг</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<style scoped lang="scss"></style>
