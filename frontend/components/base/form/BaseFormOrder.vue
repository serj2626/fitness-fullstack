<script setup lang="ts">
const modalsStore = useModalsStore();
const isOpen = ref<boolean>(true);

function closeModalOrder() {
  isOpen.value = false;
  setTimeout(() => {
    modalsStore.closeModal("order");
  }, 600);
}
</script>
<template>
  <BaseModalSide
    duration=".6s"
    :is-open="isOpen"
    max-width="100vw"
    position="right"
    padding="10px"
    color-icon="#ffc451"
    timing="ease-out"
    @close="closeModalOrder"
  >
    <OrderAbonementComponent />
  </BaseModalSide>
</template>
<style scoped lang="scss"></style>
