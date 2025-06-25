<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { IQuestion } from "~/types";

defineProps<{
  faqInfo: IQuestion[] | null;
}>();

const currentIndex = ref<number | null>(null);

function toggleAccordion(id: number): void {
  currentIndex.value = currentIndex.value === id ? null : id;
}
</script>
<template>
  <div class="faq-content">
    <ul v-if="faqInfo" class="faq-content__list">
      <li
        v-for="(faq, index) in faqInfo"
        :key="faq.id"
        class="accordion"
        @click="toggleAccordion(faq.id)"
      >
        <BaseAccordionComponent :is-open="currentIndex === faq.id">
          <template #summary>
            <div class="accordion__header">
              <p class="accordion__header-question">
                <span class="accordion__header-question-number">
                  {{ index < 10 ? `0${index + 1}` : `${index + 1}` }}
                </span
                >{{ faq.question }}
              </p>
              <button class="accordion__header-btn">
                <Icon
                  class="accordion__header-btn-icon"
                  :class="{
                    'accordion__header-btn-icon_open': currentIndex === faq.id,
                  }"
                  :name="HeroIcons.PLUS"
                />
              </button>
            </div>
          </template>
          <template #default><p class="accordion__content">{{ faq.answer }}</p></template>
        </BaseAccordionComponent>
      </li>
    </ul>
  </div>
</template>
<style scoped lang="scss">
.faq-content {
  padding-block: 100px;
  &__list {
    margin-top: 50px;
    max-width: 800px;
    margin-inline: auto;
    color: $white;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
}

.accordion__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-right: 5px;
  &-question {
    display: flex;
    align-items: center;
    gap: 10px;
    &-number{
      font-weight: 700;
      font-size: 24px;
      transform: translateX(-20px) translateY(-10px);
    }
  }

  &-btn {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 6px;
    border-radius: 50%;
    background-color: $grey;
    transition: all 0.3s ease-in;
    &:hover {
      opacity: 0.6;
    }

    &-icon {
      width: 25px;
      height: 25px;
      transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
      &_open {
        rotate: -45deg;
      }
    }
  }
}

.accordion__content {
  margin-top: 10px;
  padding-left: 20px;
  color: $white;
}
</style>
