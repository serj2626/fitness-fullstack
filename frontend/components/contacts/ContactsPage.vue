<script lang="ts" setup>
import type { IContactsResponse } from "~/types";
const { data: contactsInfo } =
  useNuxtData<IContactsResponse>("all-contants-info");
</script>
<template>
  <div class="contacts-page">
    <div class="container">
      <BaseFormFeedback
        :address="contactsInfo?.address.value"
        :tel="contactsInfo?.phone.value"
      />
      <ContactsInfo v-if="contactsInfo" :contacts="contactsInfo" />
    </div>
    <BaseMap
      :map-longitude="contactsInfo?.longitude.value"
      :map-width="contactsInfo?.latitude.value"
    />
  </div>
</template>

<style lang="scss">
.contacts-page {
  padding-top: 100px;
}
</style>
