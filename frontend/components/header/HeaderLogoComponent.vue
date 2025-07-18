<script setup lang="ts"></script>
<template>
  <NuxtLink class="header-logo-component" to="/">
    <span class="header-logo-component__title">DV</span>
    <span class="header-logo-component__text">Fitness</span>
    <BaseDot />
  </NuxtLink>
</template>
<style scoped lang="scss">
.header-logo-component {
  color: #fff;
  font-size: 24px;
  font-weight: 600;
  &__title {
    text-shadow: 0 0 14px #ffc451;
    margin-right: 5px;
  }
  &__text {
    font-size: 15px;
    text-transform: lowercase;
    font-weight: 500;
    opacity: 0.8;
  }
}
</style>
