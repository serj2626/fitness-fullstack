<template>
  <div class="layout-default">
    <HeaderComponent />
    <slot />
    <FooterComponent />
    <BaseButtonScrollToTop />
    <ModalComponent />
    <LazyBaseAlertBaseAlerCookie />
  </div>
</template>
<style lang="scss">
.ayout-default {
  min-height: 100vh;
  height: 100%;
}
</style>
