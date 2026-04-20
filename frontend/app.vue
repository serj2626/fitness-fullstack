<script setup lang="ts">
import { useContactsStore } from "./stores/contacts";

const contactsStore = useContactsStore();
await contactsStore.loadAll();
</script>
<template>
  <div>
    <BaseButtonScrollToTop />
    <NuxtLayout :key="$route.meta.layout || $route.name">
      <NuxtLoadingIndicator />
      <NuxtPage />
    </NuxtLayout>
    <LazyBaseAlertCookie />
    <LazyBaseNotifications />
    <!-- <BaseSeoMeta /> -->
  </div>
</template>
<style lang="scss">
.page-enter-active,
.page-leave-active {
  transition: all 0.4s ease-in;
  transition-duration: 0.4s;
}

.page-enter-from,
.page-leave-to {
  opacity: 0;
  filter: blur(1rem);
}
</style>
