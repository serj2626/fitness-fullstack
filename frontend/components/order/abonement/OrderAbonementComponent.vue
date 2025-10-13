<script setup lang="ts">
const abonementsStore = useAbonementsStore();
const {
  abonements: abonementsData,
  error,
  loading,
} = storeToRefs(abonementsStore);

const type = ref<"abonements" | "form" | "success">("success");

const activeAbonement = ref<number | null>(null);
const currentStep = ref<number>(3);

function setStep(step: number) {
  if (step === 1) {
    type.value = "abonements";
    currentStep.value = 1;
  } else if (step === 2) {
    type.value = "form";
    currentStep.value = 2;
  } else {
    type.value = "success";
    currentStep.value = 3;
  }
}
</script>
<template>
  <div class="order-abonement-component">
    <div class="container">
      <h1 class="order-abonement-component__title">Бронирование абонемента</h1>
      <OrderAbonementSteps :current-step="currentStep" @set-step="setStep" />
      <OrderAbonementList
        v-if="currentStep === 1"
        :active-abonement="activeAbonement"
        :abonements="abonementsData"
        @active-abonement="activeAbonement = $event"
        @new-step="currentStep = $event"
      />
      <OrderAbonementForm
        v-else-if="currentStep === 2"
        :active-abonement="activeAbonement"
      />
      <OrderAbonementSuccess v-else />
    </div>
  </div>
</template>
<style scoped lang="scss">
.order-abonement-component {
  &__title {
    text-align: center;
    font-size: clamp(1.5rem, 3vw, 2.5rem);
    color: $accent;
  }
}
</style>
