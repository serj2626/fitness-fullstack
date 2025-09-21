<script setup lang="ts">
defineProps<{ title: string; description?: string }>();
</script>
<template>
  <section class="pages-top-section">
    <div class="container">
      <h1>{{ title }}</h1>
      <p v-if="description">{{ description }}</p>
    </div>
  </section>
</template>
<style scoped lang="scss">
.pages-top-section {
  background-color: $txt;
  color: $white;
  padding: 120px 0;
  text-align: center;

  h1 {
    font-size: 3rem;
    margin-bottom: 20px;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: $accent;
  }

  p {
    font-size: 1.2rem;
    opacity: 0.9;
  }
}
</style>
