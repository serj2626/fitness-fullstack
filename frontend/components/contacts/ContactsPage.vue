<script lang="ts" setup>
import { api } from "~/api";
import type { IContactData } from "~/types";
const { $api } = useNuxtApp();

const { data: contactsInfo } = await useAsyncData(
  "contacts-page-info",
  () => $api<IContactData[]>(api.contacts.list),
  {
    transform: (data) => {
      const res: Record<string, IContactData> = {};
      for (const item of data) {
        res[item.type] = item;
      }
      return res;
    },
  }
);
</script>
<template>
  <div class="contacts-page">
    <div class="container">
      <BaseFormFeedback />
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
