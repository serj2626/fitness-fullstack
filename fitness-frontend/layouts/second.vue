<template>
  <div class="app">
    <HeaderComponent />
    <slot />
    <BaseButtonScrollToTop />
    <ModalComponent />
    <LazyBaseAlertBaseAlerCookie />
  </div>
</template>
<style lang="scss">
.app {
}
</style>
