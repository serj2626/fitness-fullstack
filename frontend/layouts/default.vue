<template>
  <div class="layout-default">
    <HeaderComponent />
    <slot />
    <FooterComponent v-if="!$route.meta.hideFooter" />
    <BaseButtonScrollToTop />
    <ModalComponent />
  </div>
</template>
<style lang="scss">
.ayout-default {
  min-height: 100vh;
  height: 100%;
  padding-top: 70px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
</style>
