<script setup lang="ts"></script>
<template>
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
          <div class="purchases-history__price">{{ purchase.price }} ₽</div>
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
</template>
<style scoped lang="scss"></style>
