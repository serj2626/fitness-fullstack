<script setup lang="ts">
import type { IAbonement } from "~/types";

const { plan } = defineProps<{ plan: IAbonement }>();

defineEmits(["activeAbonement"]);

const countFreeze = computed(() => {
  return plan.days_freezing > 0
    ? `${plan.days_freezing} дней заморозки`
    : "Без заморозки";
});
</script>

<template>
  <div class="order-abonement-card">
    <BaseGridComponent>
      <template #header>
        <h3 class="order-abonement-card__title">
          {{ plan.name }}
        </h3>
        <div class="order-abonement-card__price-section">
          <p class="order-abonement-card__price">
            {{ formatNumberCustom(plan.price) }} ₽
          </p>
          <p class="order-abonement-card__mounts">
            {{ plan.count_months }} мес.
          </p>
        </div>
        <!-- <div v-if="1 > 0" class="order-abonement-card__sale">-4%</div> -->
        <div v-if="plan.is_popular" class="order-abonement-card__popular">
          Популярный
        </div>
      </template>
      <template #main>
        <ul class="order-abonement-card__features">
          <li
            v-for="feature in plan.services.services"
            :key="feature"
            class="order-abonement-card__feature"
          >
            {{ feature }}
          </li>
        </ul>
      </template>
      <template #footer>
        <div class="order-abonement-card__divider" />
        <div class="order-abonement-card__freeze">
          <svg
            class="order-abonement-card__freeze-icon"
            width="20"
            height="20"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M12 2V22M12 2L8 6M12 2L16 6M12 22L8 18M12 22L16 18M20 12H4M19 8L5 8M19 16L5 16"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
          <span>{{ countFreeze }}</span>
        </div>
        <BaseButton
          style="width: 100%"
          size="lg"
          class="order-abonement-card__btn"
          label="Выбрать"
          @click="$emit('activeAbonement', plan.id)"
        />
      </template>
    </BaseGridComponent>
  </div>
</template>

<style scoped lang="scss">
.order-abonement-card {
  position: relative;
  background: lighten($bg, 5%);
  border: 2px solid lighten($bg, 10%);
  border-radius: 16px;
  padding: 24px;
  cursor: pointer;
  transition: all 0.3s ease;
  overflow: hidden;

  // Градиентный акцент сверху
  &::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, $accent, lighten($accent, 15%));
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  &:hover {
    transform: translateY(-5px);
    border-color: $accent;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);

    &::before {
      opacity: 1;
    }
  }

  &_active {
    border-color: $accent;
    box-shadow:
      0 0 0 2px $accent,
      0 10px 25px rgba(0, 0, 0, 0.2);

    &::before {
      opacity: 1;
    }
  }

  &__title {
    color: $white;
    font-size: 1.4rem;
    font-weight: 700;
    margin-bottom: 16px;
    line-height: 1.3;
  }

  &__price-section {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    margin-bottom: 20px;
  }

  &__price {
    color: $accent;
    font-size: 2rem;
    font-weight: 800;
    margin: 0;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  }

  &__mounts {
    color: rgba($white, 0.8);
    font-size: 1rem;
    font-weight: 500;
    margin: 0;
    background: rgba($accent, 0.1);
    padding: 6px 12px;
    border-radius: 20px;
    border: 1px solid rgba($accent, 0.3);
  }

  &__features {
    color: rgba($white, 0.9);
    padding-left: 20px;
    margin-bottom: 0;
    line-height: 1.6;

    li {
      margin-bottom: 12px;
      position: relative;
      padding-left: 8px;
      display: flex;
      align-items: center;

      &::before {
        content: "•";
        color: $accent;
        position: absolute;
        left: -15px;
        font-size: 1.5rem;
      }
    }
  }

  &__divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, $accent, transparent);
    width: 100%;
    margin: 20px 0;
  }

  &__freeze {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 20px;
    color: rgba($white, 0.8);
    font-size: 0.95rem;
    background: rgba($accent, 0.05);
    padding: 10px 15px;
    border-radius: 10px;
    border: 1px solid rgba($accent, 0.1);
  }

  &__freeze-icon {
    color: $accent;
    flex-shrink: 0;
  }

  &__sale {
    position: absolute;
    top: 15px;
    right: 15px;
    background: linear-gradient(135deg, $red, darken($red, 10%));
    color: $white;
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 700;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    z-index: 2;
  }

  &__popular {
    position: absolute;
    top: 45px;
    right: -25px;
    background: linear-gradient(135deg, $accent, lighten($accent, 10%));
    color: rgba($txt, 0.8);
    padding: 5px 30px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 700;
    transform: rotate(45deg);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    z-index: 2;
  }
}
</style>
