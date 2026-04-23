<script setup lang="ts">
defineProps<{
  email: string;
  phone: string[];
  mode: string;
  address: string;
}>();
</script>
<template>
  <div class="contacts-info">
    <div class="contacts-info__list">
      <div v-if="email" class="contacts-info__list-mail">
        <div class="contacts-info__list-mail-title">Почта</div>
        <a :href="`mailto:${email}`" class="contacts-info__list-mail-value">
          {{ email || "bs-dev@bk.ru" }}
        </a>
      </div>
      <div v-if="phone" class="contacts-info__list-phone">
        <div class="contacts-info__list-phone-title">Телефон</div>
        <a
          v-for="(value, index) in phone"
          :key="index"
          :href="`tel:${value}`"
          class="contacts-info__list-phone-value"
        >
          {{ value || "+7 (999) 999-99-99" }}
        </a>
      </div>
      <div v-if="mode" class="contacts-info__list-mode">
        <div class="contacts-info__list-mode-title">Режим работы</div>
        <div class="contacts-info__list-mode-value">
          {{ mode || "Пн-Пт: 9:00 - 18:00" }}
        </div>
      </div>
      <div v-if="address" class="contacts-info__list-address">
        <div class="contacts-info__list-address-title">Адрес</div>
        <div class="contacts-info__list-address-value">
          {{ address || "СПБ, улица Будапештская дом 89" }}
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss">
.contacts-info {
  &__list {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    margin-bottom: 50px;
    &-mail,
    &-phone,
    &-address,
    &-mode {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    &-mode-title,
    &-mail-title,
    &-phone-title,
    &-address-title {
      color: aliceblue;
      font-size: 20px;
      font-weight: 600;
    }
    &-mail-value,
    &-phone-value,
    &-address-value,
    &-mode-value {
      color: aliceblue;
    }
  }
}
</style>
