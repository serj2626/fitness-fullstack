<script setup lang="ts">
import type { ICoachService } from "~/types";

const props = defineProps<{ services: ICoachService[] }>();

const getPrice = (price: number | null) => {
  if (price) return `${price} ₽`;
  return "Не указана";
};

const sortedServices = computed(() => {
  const serviceListSorted: Record<string, ICoachService[]> = {};
  props.services.forEach((service) => {
    if (serviceListSorted[service.title]) {
      serviceListSorted[service.title].push(service);
    } else {
      serviceListSorted[service.title] = [service];
    }
  });

  const sortedServicesByPrice: Record<string, ICoachService[]> = {};
  for (const title in serviceListSorted) {
    sortedServicesByPrice[title] = serviceListSorted[title].sort(
      (a, b) => a.price - b.price,
    );
  }

  return sortedServicesByPrice;
});
</script>
<template>
  <div class="coach-detail-services">
    <ul v-if="services.length" class="coach-detail-services__list">
      <div class="coach-detail-services__header">
        <span>Услуга</span>
        <span>Цена</span>
      </div>
      <!-- {{
        sortedServices
      }} -->
      <li
        v-for="service in services"
        :key="service.id"
        class="coach-detail-services__item"
      >
        <div class="coach-detail-services__info">
          <span class="coach-detail-services__name">
            {{ service?.title }}
          </span>
          <span class="coach-detail-services__duration">
            {{ service?.time }} мин
          </span>
        </div>

        <div class="coach-detail-services__separator" />

        <div class="coach-detail-services__price">
          {{ getPrice(service?.price) }}
        </div>
      </li>
    </ul>
    <BaseEmpty v-else text="Услуги отсутствуют" />
  </div>
</template>
<style scoped lang="scss">
.coach-detail-services {
  background: rgba(255, 255, 255, 0.05);
  padding: 15px 25px;
  color: white;

  &__duration {
    font-size: 13px;
    color: rgba(255, 255, 255, 0.7);
  }

  &__info {
    display: flex;
    flex-direction: column;
    gap: 4px;
    max-width: 60%;
  }

  &__list {
    display: flex;
    flex-direction: column;
    gap: 8px; // Небольшой отступ между карточками
    padding: 0;
    list-style: none;
  }

  &__header {
    padding: 12px 16px;
    border-radius: 12px;
    display: flex;
    justify-content: space-between;
    margin-bottom: 30px;
    font-weight: 600;
  }

  &__item {
    display: flex;
    align-items: baseline; // Чтобы цена была на уровне первой строки названия
    padding: 12px 16px;
    border-radius: 12px;
    transition: all 0.2s ease-in-out;
    cursor: default;
    font-size: 14px;
  }

  &__separator {
    flex: 1;
    margin: 0 12px;
    border-bottom: 1px dashed gray;
    position: relative;
    top: -4px;
  }
}
</style>
