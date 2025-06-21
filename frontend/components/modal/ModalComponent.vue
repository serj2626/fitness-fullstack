<script setup lang="ts">
import { LazyModalPasswordRecovery } from '#components';

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
    <LazyModalPasswordRecovery
      v-if="activeModals.has('passwordRecovery')"
      key="orderAbonement"
    />
    <LazyBaseFormOrderTraining
      v-if="activeModals.has('orderTraining')"
      key="orderTraining"
    />
    <LazyModalLogin v-if="activeModals.has('login')" key="login" />
    <LazyModalRegister v-if="activeModals.has('register')" key="register" />
    <LazyHeaderCatalogMenu
      v-if="activeModals.has('menu')"
      key="orderAbonement"
    />
    <LazyModalCoachReview
      v-if="activeModals.has('reviewCoachForm')"
      key="orderAbonement"
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
