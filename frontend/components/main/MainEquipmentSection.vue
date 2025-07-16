<script setup lang="ts">
import type { IEequipmentResponse } from "~/types";

const activeTab = ref(0);

const props = defineProps<{ data: Record<string, IEequipmentResponse> }>();

const tabs = computed(() => {
  return Object.keys(props.data);
});
</script>

<template>
  <section class="main-equipment-section">
    <div class="container">
      <h2 class="main-equipment-section__title">Наши залы и оборудование</h2>
      <div class="main-equipment-section__tabs">
        <button
          v-for="(tab, index) in tabs"
          :key="index"
          :class="[
            'main-equipment-section__tabs-button',
            { active: activeTab === index },
          ]"
          @click="activeTab = index"
        >
          {{ tab }}
        </button>
      </div>
      <div class="main-equipment-section__content">
        <MainEquipmentCard
          v-for="(tab, index) in tabs"
          v-show="activeTab === index"
          :key="index"
          :equipment="data[tab]"
        />
      </div>
    </div>
  </section>
</template>
<style scoped lang="scss">
.main-equipment-section {
  padding: 5rem 0;
  background: $bg;

  &__title {
    text-align: center;
    margin-bottom: 2rem;
    color: $accent;
    font-size: 2rem;
  }
  &__tabs {
    display: flex;
    justify-content: center;
    margin-bottom: 2rem;
    flex-wrap: wrap;
    gap: 0.5rem;
    &-button {
      background: transparent;
      color: $white;
      border: none;
      padding: 0.75rem 1.5rem;
      font-size: 1rem;
      cursor: pointer;
      border-radius: 4px;
      transition: all 0.3s ease;
      position: relative;

      &:hover {
        color: $accent;
      }

      &.active {
        color: $accent;
        font-weight: 600;

        &::after {
          content: "";
          position: absolute;
          bottom: -8px;
          left: 50%;
          transform: translateX(-50%);
          width: 50%;
          height: 2px;
          background: $accent;
        }
      }
    }
  }
}
</style>
