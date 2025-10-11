<script setup lang="ts">
import OrderAbonementComponent from "~/components/order/abonement/OrderAbonementComponent.vue";
import OrderTrainingComponent from "~/components/order/training/OrderTrainingComponent.vue";

const type = ref<"abonement" | "training">("abonement");
const modalsStore = useModalsStore();
const isOpen = ref<boolean>(true);

function closeModalOrder() {
  isOpen.value = false;
  setTimeout(() => {
    modalsStore.closeModal("order");
  }, 500);
}
const modalMap = {
  abonement: OrderAbonementComponent,
  training: OrderTrainingComponent,
};
</script>
<template>
  <BaseModalSide
    duration=".5s"
    :is-open="isOpen"
    max-width="100vw"
    position="right"
    @close="closeModalOrder"
  >
    <component
      :is="modalMap[type]"
    />
  </BaseModalSide>
</template>
<style scoped lang="scss"></style>
