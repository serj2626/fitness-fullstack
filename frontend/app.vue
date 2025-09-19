<script setup lang="ts">
import { api } from "~/api";
import type {
  IContact,
  IFooterInfo,
  IFooterInfoTransformResponse,
} from "~/types";
const { $api } = useNuxtApp();

await useAsyncData<IFooterInfoTransformResponse>(
  "footer-info",
  () => $api(api.contacts.footer),
  {
    transform: (data: IFooterInfo) => {
      const contactsMap = data.contacts.reduce((acc, item) => {
        acc[item.type] = item;
        return acc;
      }, {} as Record<string, IContact>);

      const { contacts, ...rest } = data;

      return {
        ...rest,
        ...contactsMap,
      };
    },
  }
);
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
    <BaseSeoMeta />
  </div>
</template>
<style lang="scss">
.page-enter-active,
.page-leave-active {
  transition: all 0.3s ease-in;
  transition-duration: 0.4s;
}

.page-enter-from,
.page-leave-to {
  opacity: 0;
  filter: blur(1rem);
}
</style>
