<script setup lang="ts">
import type { IContactsResponse } from "~/types";

defineProps<{ contacts: IContactsResponse }>();
</script>
<template>
  <div class="contacts-info">
    <div class="contacts-info__list">
      <div class="contacts-info__list-mail">
        <div class="contacts-info__list-mail-title">
          {{ contacts.mail.second_type }}
        </div>
        <div class="contacts-info__list-mail-value">
          {{ contacts.mail.value }}
        </div>
      </div>
      <div class="contacts-info__list-phone">
        <div class="contacts-info__list-phone-title">
          {{ contacts.phone.second_type }}
        </div>
        <div class="contacts-info__list-phone-value">
          {{ contacts.phone.value }}
        </div>
      </div>
      <div class="contacts-info__list-mode">
        <div class="contacts-info__list-mode-title">
          {{ contacts.mode.second_type }}
        </div>
        <div class="contacts-info__list-mode-value">
          {{ contacts.mode.value }}
        </div>
      </div>
      <div class="contacts-info__list-address">
        <div class="contacts-info__list-address-title">
          {{ contacts.address.second_type }}
        </div>
        <div class="contacts-info__list-address-value">
          {{ contacts.address.value }}
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
