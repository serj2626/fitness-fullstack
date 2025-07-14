<script setup lang="ts"></script>
<template>
  <section class="main-advantages-section">
    <div class="container">
      <h2 class="main-advantages-section__title">Наши преимущества</h2>
      <div class="main-advantages-section__list">
        <div class="main-advantages-section__list-card">
          <div class="amain-advantages-section__list-card__icon">
            <svg width="48" height="48" viewBox="0 0 24 24">
              <path
                fill="#ffc451"
                d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"
              />
            </svg>
          </div>
          <h3 class="main-advantages-section__list-card__title">
            Профессиональные тренеры
          </h3>
          <p class="main-advantages-section__list-card__text">
            Все наши специалисты имеют международные сертификации и минимум 5
            лет опыта работы
          </p>
        </div>
        <div class="main-advantages-section__list-card">
          <div class="advantage-card__icon">
            <svg width="48" height="48" viewBox="0 0 24 24">
              <path
                fill="#ffc451"
                d="M19 3h-4.18C14.4 1.84 13.3 1 12 1c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm0 4c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm6 12H6v-1.4c0-2 4-3.1 6-3.1s6 1.1 6 3.1V19z"
              />
            </svg>
          </div>
          <h3 class="main-advantages-section__list-card__title">
            Индивидуальный подход
          </h3>
          <p class="main-advantages-section__list-card__text">
            Персональные программы тренировок и питания для каждого клиента
          </p>
        </div>
        <div class="main-advantages-section__list-card">
          <div class="main-advantages-section__list-card__icon">
            <svg width="48" height="48" viewBox="0 0 24 24">
              <path
                fill="#ffc451"
                d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.31-8.86c-1.77-.45-2.34-.94-2.34-1.67 0-.84.79-1.43 2.1-1.43 1.38 0 1.9.66 1.94 1.64h1.71c-.05-1.34-.87-2.57-2.49-2.97V5H10.9v1.69c-1.51.32-2.72 1.3-2.72 2.81 0 1.79 1.49 2.69 3.66 3.21 1.95.46 2.34 1.15 2.34 1.87 0 .53-.39 1.39-2.1 1.39-1.6 0-2.23-.72-2.32-1.64H8.04c.1 1.7 1.36 2.66 2.86 2.97V19h2.34v-1.67c1.52-.29 2.72-1.16 2.73-2.77-.01-2.2-1.9-2.96-3.66-3.42z"
              />
            </svg>
          </div>
          <h3 class="main-advantages-section__list-card__title">
            Гибкая система лояльности
          </h3>
          <p class="main-advantages-section__list-card__text">
            Скидки, заморозки и бонусы для наших постоянных клиентов
          </p>
        </div>
        <div class="main-advantages-section__list-card">
          <div class="main-advantages-section__list-card__icon">
            <svg width="48" height="48" viewBox="0 0 24 24">
              <path
                fill="#ffc451"
                d="M18 8c0-3.31-2.69-6-6-6S6 4.69 6 8c0 4.5 6 11 6 11s6-6.5 6-11zm-8 0c0-1.1.9-2 2-2s2 .9 2 2-.89 2-2 2c-1.1 0-2-.9-2-2zM5 20v2h14v-2H5z"
              />
            </svg>
          </div>
          <h3 class="main-advantages-section__list-card__title">
            Удобное расположение
          </h3>
          <p class="main-advantages-section__list-card__text">
            Центр города, собственная парковка и легкая доступность на
            общественном транспорте
          </p>
        </div>
      </div>
    </div>
  </section>
</template>
<style scoped lang="scss">
.main-advantages-section {
  padding: 100px 0;
  background: url("/pattern.png") center/cover;

  &__title {
    color: $accent;
    font-size: 2rem;
    margin-bottom: 1.5rem;
    text-align: center;
  }
  &__list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin-top: 3rem;
    &-card {
      background: $bg_block;
      padding: 2rem;
      border-radius: 8px;
      text-align: center;
      transition: all 0.3s ease;
      border-bottom: 3px solid transparent;

      &:hover {
        transform: translateY(-10px);
        border-bottom-color: $accent;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
      }

      &__icon {
        margin-bottom: 1.5rem;
      }

      &__title {
        color: $accent;
        margin-bottom: 1rem;
        font-size: 1.3rem;
      }

      &__text {
        color: rgba($white, 0.8);
        line-height: 1.6;
        margin: 0;
      }
    }
  }
}
</style>
