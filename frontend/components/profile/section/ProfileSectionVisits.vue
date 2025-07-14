<script setup lang="ts"></script>
<template>
  <section class="user-main__section" v-if="activeTab === 'visits'">
    <div class="user-main__section-header">
      <h2 class="user-main__section-title">История посещений</h2>
      <div class="user-main__section-actions">
        <button class="user-main__btn">Экспорт</button>
      </div>
    </div>

    <div class="visits-history">
      <div class="visits-history__item" v-for="visit in visits" :key="visit.id">
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
</template>
<style scoped lang="scss"></style>
