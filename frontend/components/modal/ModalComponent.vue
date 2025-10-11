<script setup lang="ts">
const modalsStore = useModalsStore();
const { activeModals, isAnyModalOpen } = storeToRefs(modalsStore);
</script>
<template>
  <div
    v-if="isAnyModalOpen"
    class="modal-wrapper"
    role="dialog"
    @click.self="modalsStore.closeAllModals()"
  >
    <LazyBaseFormOrderAbonement
      v-if="activeModals.has('orderAbonement')"
      key="orderAbonement"
    />
    <LazyBaseFormOrder v-if="activeModals.has('order')" key="order" />
    <LazyModalService v-if="activeModals.has('service')" key="service" />
    <LazyBaseFormOrderTraining
      v-if="activeModals.has('orderTraining')"
      key="orderTraining"
    />
    <LazyModalAuth v-if="activeModals.has('auth')" key="auth" />
    <LazyHeaderCatalogMenu v-if="activeModals.has('menu')" key="menu" />
    <LazyModalCoachReview
      v-if="activeModals.has('reviewCoachForm')"
      key="reviewCoachForm"
    />
  </div>
</template>
<style lang="scss" scoped>
.modal-wrapper {
  position: fixed;
  bottom: 0;
  right: 0;
  left: 0;
  top: 0;
  z-index: 110;
  background: rgba(0, 0, 0, 0.47);
}

.fade-modal-enter-active,
.fade-modal-leave-active {
  opacity: 1;
  transition: opacity 0.3s ease-in;
}
.fade-modal-enter-from,
.fade-modal-leave-to {
  opacity: 0;
  transition: opacity 0.3s ease-in;
}
</style>
