<script lang="ts" setup>
import { useContactsStore } from "~/stores/contacts";
const contactsStore = useContactsStore();
const { footerInfo, socials, contactsList, loaded } =
  storeToRefs(contactsStore);
</script>
<template>
  <div class="contacts-page">
    <div class="container">
      <BaseFormFeedback
      />
      <ContactsInfo
        :address="contactsList?.address as string"
        :phone="contactsList?.phone as string"
        :mode="contactsList?.mode as string"
        :email="contactsList?.email as string"
      />
    </div>
    <BaseMap />
  </div>
</template>

<style lang="scss">
.contacts-page {
  padding-top: 100px;
}
</style>
