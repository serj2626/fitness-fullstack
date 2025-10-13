<script setup lang="ts">
import type { IAbonementResponse } from "~/types";

defineProps<{ abonements: IAbonementResponse[]; activeAbonement: number }>();

defineEmits(["active-abonement", "newStep"]);
</script>
<template>
  <div class="order-abonement-list">
    <div class="order-abonement-list__list">
      <OrderAbonementCard
        v-for="plan in abonements"
        :key="plan.id"
        :plan="plan"
        :is-active="plan.id === activeAbonement"
        @active-abonement="$emit('active-abonement', plan.id)"
      />
    </div>
    <BaseButton
      :outline="true"
      class="order-abonement-list__btn"
      label="Далее"
      @click="$emit('newStep', 2)"
    />
  </div>
</template>
<style scoped lang="scss">
.order-abonement-list {
  display: flex;
  flex-direction: column;
  gap: 35px;
}
.order-abonement-list__list {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 25px;
}
.order-abonement-list__btn {
  align-self: flex-end;
  padding: 15px 75px;
}
</style>
