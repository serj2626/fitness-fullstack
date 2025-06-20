<script setup lang="ts"></script>
<template>
  <button class="base-button-burger">
    <span class="base-button-burger__line-one"></span>
    <span class="base-button-burger__line-two"></span>
  </button>
</template>
<style scoped lang="scss">
.base-button-burger {
  // position: absolute;
  // top: 40px;
  // right: 60px;
  cursor: pointer;
  @include mediaLaptop{
    display: none;
  }

  & span {
    display: block;
    opacity: 1;
    background: $accent;
    width: 40px;
    height: 2px;
    margin-bottom: 8px;
    transition: 0.6s ease;
    box-sizing: border-box;
  }
}

.base-button-burger:hover {
  .base-button-burger__line-one {
    // rotate: -45deg;
    opacity: 1;
    transform: translateY(4px) rotate(-45deg);
  }
  .base-button-burger__line-two {
    // rotate: 45deg;
    opacity: 1;
    transform: translateY(-4px) rotate(45deg);
  }
}
</style>
