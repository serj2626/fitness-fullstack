<script lang="ts" setup>
import { useContactsStore } from "~/stores/contacts";

// import type {
//   IContactsFooterInfo,
//   IContactsList,
//   IContactsSocials,
// } from "~/types";
// import { api } from "~/api";

// const { $api } = useNuxtApp();
// // const { data: footerData } =
// //   useNuxtData<IFooterInfoTransformResponse>("footer-info");

// const [{ data: footerData }, { data: socialsData }, { data: contactsData }] =
//   await Promise.all([
//     useAsyncData("contacts-page-footer-info", () =>
//       $api<IContactsFooterInfo>(api.contacts.footer),
//     ),
//     useAsyncData("contacts-page-socials", () =>
//       $api<IContactsSocials>(api.contacts.socials),
//     ),
//     useAsyncData("contacts-page-list", () =>
//       $api<IContactsList>(api.contacts.list),
//     ),
//   ]);

const contactsStore = useContactsStore();
const { footerInfo, socials, contactsList, loaded } =
  storeToRefs(contactsStore);
</script>
<template>
  <div class="contacts-page">
    <div class="container" style="background-color: aliceblue; color: black">
      <!-- <BaseFormFeedback
        :address="contactsData?.address.value"
        :tel="contactsData?.phone.value"
      /> -->
      <!-- <ContactsInfo
        :address="footerData?.address as IContact"
        :phone="footerData?.phone as IContact"
        :mode="footerData?.mode as IContact"
        :mail="footerData?.mail as IContact"
      /> -->
      {{ footerInfo }} <br>
      {{ socials }} <br>
      {{ contactsList }} <br>
      {{ loaded }}
    </div>
    <BaseMap />
  </div>
</template>

<style lang="scss">
.contacts-page {
  padding-top: 100px;
}
</style>
