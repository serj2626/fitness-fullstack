<script setup lang="ts">
import type { IContact } from "~/types";

defineProps<{
  mail: IContact;
  phone: IContact;
  mode: IContact;
  address: IContact;
}>();
</script>
<template>
  <div class="contacts-info">
    <div class="contacts-info__list">
      <div class="contacts-info__list-mail">
        <div class="contacts-info__list-mail-title">
          {{ mail.type_display || "Почта" }}
        </div>
        <a
          :href="`mailto:${mail.value}`"
          class="contacts-info__list-mail-value"
        >
          {{ mail.value || "bs-dev@bk.ru" }}
        </a>
      </div>
      <div class="contacts-info__list-phone">
        <div class="contacts-info__list-phone-title">
          {{ phone.type_display || "Телефон" }}
        </div>
        <a :href="`tel:${phone.value}`" class="contacts-info__list-phone-value">
          {{ phone.value || "+7 (999) 999-99-99" }}
        </a>
      </div>
      <div class="contacts-info__list-mode">
        <div class="contacts-info__list-mode-title">
          {{ mode.type_display || "Режим работы" }}
        </div>
        <div class="contacts-info__list-mode-value">
          {{ mode.value || "Пн-Пт: 9:00 - 18:00" }}
        </div>
      </div>
      <div class="contacts-info__list-address">
        <div class="contacts-info__list-address-title">
          {{ address.type_display || "Адрес" }}
        </div>
        <div class="contacts-info__list-address-value">
          {{ address.value || "СПБ, улица Будапештская дом 89" }}
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
