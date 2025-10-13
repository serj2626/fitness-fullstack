<script setup lang="ts">
defineProps<{
  currentStep: number;
}>();

defineEmits(["setStep"]);
</script>
<template>
  <div class="order-abonement-steps">
    <ul class="order-abonement-steps__list">
      <BaseButton
        class="order-abonement-steps__list-item"
        :class="{
          active: currentStep === 1,
        }"
        label="1"
        @click="$emit('setStep', 1)"
      />
      <BaseButton
        class="order-abonement-steps__list-item"
        :class="{
          active: currentStep === 2,
        }"
        :disabled="currentStep < 2"
        label="2"
        @click="$emit('setStep', 2)"
      />
      <BaseButton
        class="order-abonement-steps__list-item"
        :class="{
          active: currentStep === 3,
        }"
        :disabled="currentStep < 3"
        label="3"
        @click="$emit('setStep', 3)"
      />
    </ul>
  </div>
</template>
<style scoped lang="scss">
.order-abonement-steps {
  padding: 40px 0;
}
.order-abonement-steps__list {
  display: flex;
  justify-content: center;
  gap: 25px;
}
.order-abonement-steps__list-item {
  border-radius: 50%;
  position: relative;

  &.active {
    background: $accent;

    &::after {
      content: "";
      position: absolute;
      bottom: -15px;
      left: 0;
      width: 100%;
      height: 2px;
      border-radius: 50%;
      border: 2px solid $accent;
    }
  }
}
</style>
