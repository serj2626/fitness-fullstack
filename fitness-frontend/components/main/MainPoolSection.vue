<script lang="ts" setup></script>

<template>
  <section id="main-pool-section" class="main-pool-section">
    <div class="main-pool-section__wraper"></div>
  </section>
</template>

<style lang="scss" scoped>
.main-pool-section {
  &__wraper {
    background-image: url(/pool.jpg);
    background-attachment: fixed;
    background-size: cover;
    height: 300px;
    @include mediaLaptop {
      height: 400px;
    }
    @include mediaDesktop {
      height: 500px;
    }
  }
}
</style>
