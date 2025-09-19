<script lang="ts" setup>
import type { IContact, IFooterInfoTransformResponse } from "~/types";
const { data: footerData } =
  useNuxtData<IFooterInfoTransformResponse>("footer-info");
</script>
<template>
  <div class="contacts-page">
    <div class="container">
      <BaseFormFeedback
        :address="footerData?.address.value"
        :tel="footerData?.phone.value"
      />
      <ContactsInfo
        :address="footerData?.address as IContact"
        :phone="footerData?.phone as IContact"
        :mode="footerData?.mode as IContact"
        :mail="footerData?.mail as IContact"
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
