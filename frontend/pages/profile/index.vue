<script setup lang="ts">
// definePageMeta({
//   requiresAuth: true, // Только для авторизованных
//   guestOnly: true, // Только для гостей
// });
definePageMeta({
  middleware: ["auth"],
});
</script>
<template>
  <ProfilePage />
</template>
