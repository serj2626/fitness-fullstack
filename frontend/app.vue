<script setup lang="ts">
import { api } from "~/api";
import type { IContactData } from "~/types";
const { $api } = useNuxtApp();

 await useAsyncData(
  "all-contants-info",
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
  <div>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
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
