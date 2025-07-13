<template>
  <div class="second-layout">
    <HeaderComponent />
    <slot />
    <BaseButtonScrollToTop />
    <ModalComponent />
  </div>
</template>
<style lang="scss">
.second-layout {
  min-height: 100vh;
  height: 100%;
}
</style>
