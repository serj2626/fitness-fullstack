<script setup lang="ts"></script>
<template>
  <div class="base-grid-modal">
    <div class="base-grid-modal__header">
      <slot name="header" />
    </div>

    <div class="base-grid-modal__main">
      <slot name="main" />
    </div>

    <div class="base-grid-modal__footer">
      <slot name="footer" />
    </div>
  </div>
</template>
<style scoped lang="scss">
.base-grid-modal {
  width: 100%;
  height: 100%;
  position: relative;
  display: flex;
  flex-direction: column;

  &__header {
    margin-bottom: 24px;
  }

  &__main {
    flex: 1;
    overflow-y: auto;
  }

  &__footer {
    margin-top: 24px;
  }
}
</style>