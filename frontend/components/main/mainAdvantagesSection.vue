<script setup lang="ts">
// Убираем зависимость от серверных данных и defineProps
// Определяем моковые данные прямо в компоненте
interface IAdvantageResponse {
  id: number;
  icon: string;
  alt: string;
  title: string;
  description: string;
}

const advantages: IAdvantageResponse[] = [
  {
    id: 1,
    icon: "i-heroicons:rocket-launch",
    alt: "Быстрая разработка",
    title: "Высокая скорость",
    description:
      "Сокращаем время выхода продукта на рынок за счёт современных технологий и гибких методологий.",
  },
  {
    id: 2,
    icon: "i-heroicons:check-circle",
    alt: "Качество кода",
    title: "Надёжность",
    description:
      "Пишем чистый, тестируемый код с соблюдением лучших практик и стандартов.",
  },
  {
    id: 3,
    icon: "i-heroicons:phone",
    alt: "Поддержка 24/7",
    title: "Круглосуточная поддержка",
    description:
      "Всегда на связи, быстро решаем любые вопросы и проблемы клиентов.",
  },
  {
    id: 4,
    icon: "i-heroicons:user",
    alt: "Индивидуальный подход",
    title: "Персональные решения",
    description:
      "Учитываем все бизнес-требования и предлагаем оптимальную архитектуру под ваши задачи.",
  },
];
</script>

<template>
  <section class="main-advantages-section">
    <div class="container">
      <h2
        class="main-advantages-section__title"
        data-aos="zoom-in"
        data-aos-duration="1000"
      >
        Наши преимущества <BaseDot />
      </h2>
      <div class="main-advantages-section__list">
        <div
          v-for="(advantage, idx) in advantages"
          :key="advantage.id"
          class="main-advantages-section__list-card"
          data-aos="fade-up"
          :data-aos-delay="idx * 200"
          data-aos-once="true"
        >
          <Icon
            :name="advantage.icon"
            class="main-advantages-section__list-card-icon"
          />

          <h3 class="main-advantages-section__list-card-title">
            {{ advantage.title }}
          </h3>
          <p class="main-advantages-section__list-card-text">
            {{ advantage.description }}
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped lang="scss">
.main-advantages-section {
  padding: 100px 0;

  &__title {
    color: $accent;
    font-size: 2rem;
    margin-bottom: 1.5rem;
    text-align: center;
  }
  &__list {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    margin-top: 3rem;
    &-card {
      background: $bg_block;
      padding: 2rem;
      border-radius: 8px;
      text-align: center;
      border-bottom: 3px solid transparent;

      &-icon {
        margin-bottom: 1.5rem;
        width: 40px;
        height: 40px;
        color: $accent;
      }

      &-title {
        color: $accent;
        margin-bottom: 1rem;
        font-size: 1.3rem;
      }

      &-text {
        color: rgba($white, 0.8);
        line-height: 1.6;
        margin: 0;
      }
    }
  }
}
</style>
