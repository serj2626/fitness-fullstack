<script lang="ts" setup>
const modalsStore = useModalsStore();

// Моковые данные абонементов
const plans = ref([
  {
    id: 1,
    name: "Стандарт",
    price: 3000,
    features: [
      "Посещение в любое время",
      "Тренажерный зал",
      "Групповые занятия",
      "1 персональная тренировка",
    ],
    discount: 10,
  },
  {
    id: 2,
    name: "Премиум",
    price: 5000,
    features: [
      "Безлимитное посещение",
      "Все зоны клуба",
      "5 персональных тренировок",
      "Сауна и SPA",
    ],
    popular: true,
  },
  {
    id: 3,
    name: "Базовый",
    price: 2000,
    features: [
      "Дневное посещение (до 17:00)",
      "Тренажерный зал",
      "Фитнес-тестирование",
    ],
  },
]);

// Состояния формы
const isClosing = ref(false);
const isSubmitting = ref(false);
const submitSuccess = ref(false);

// Данные формы
const formData = reactive({
  name: "",
  phone: "",
  email: "",
  plan: null as (typeof plans.value)[0] | null,
  recaptcha: "",
});

// Закрытие формы с анимацией
const closeForm = () => {
  if (isSubmitting.value) {
    useNotify().warning("Пожалуйста, дождитесь окончания бронирования");
    return;
  }
  isClosing.value = true;
};

// Обработка окончания анимации
const handleAnimationEnd = () => {
  if (isClosing.value) {
    modalsStore.closeModal("orderAbonement");
    resetForm();
  }
};

// Сброс формы
const resetForm = () => {
  formData.name = "";
  formData.phone = "";
  formData.email = "";
  formData.plan = null;
  formData.recaptcha = "";
  isSubmitting.value = false;
  submitSuccess.value = false;
  isClosing.value = false;
};

// Отправка формы
const submitForm = async () => {
  if (!validateForm()) return;

  isSubmitting.value = true;

  try {
    // Имитация запроса к API
    await new Promise((resolve) => setTimeout(resolve, 1500));

    submitSuccess.value = true;
    useNotify().success(
      `Абонемент "${formData.plan?.name}" успешно забронирован!`
    );
    setTimeout(closeForm, 2000);
  } catch (error) {
    useNotify().error("Ошибка при бронировании");
  } finally {
    isSubmitting.value = false;
  }
};

// Валидация формы
const validateForm = () => {
  if (!formData.name.trim()) {
    useNotify().error("Введите ваше имя");
    return false;
  }

  if (!formData.phone.trim()) {
    useNotify().error("Введите номер телефона");
    return false;
  }

  if (!formData.plan) {
    useNotify().error("Выберите тип абонемента");
    return false;
  }

  return true;
};
</script>

<template>
  <div
    class="subscription-form"
    :class="{ 'subscription-form_close': isClosing }"
    @animationend="handleAnimationEnd"
  >
    <div class="subscription-form__wrapper">
      <!-- Заголовок формы -->
      <div class="subscription-form__header">
        <h2 class="subscription-form__title">
          <span class="highlight">Бронирование</span> абонемента
        </h2>
        <p class="subscription-form__subtitle">
          Оставьте заявку и мы подберем для вас оптимальный вариант
        </p>
      </div>

      <!-- Основное содержимое -->
      <div class="subscription-form__content" v-if="!submitSuccess">
        <!-- Выбор абонемента -->
        <div class="subscription-plans">
          <div
            v-for="plan in plans"
            :key="plan.id"
            class="subscription-plan"
            :class="{
              active: formData.plan?.id === plan.id,
              popular: plan.popular,
            }"
            @click="formData.plan = plan"
          >
            <h3 class="plan-title">{{ plan.name }}</h3>
            <p class="plan-price">{{ plan.price }} ₽</p>
            <ul class="plan-features">
              <li v-for="feature in plan.features" :key="feature">
                {{ feature }}
              </li>
            </ul>
            <div class="plan-badge" v-if="plan.discount">
              -{{ plan.discount }}%
            </div>
            <div class="plan-badge popular" v-if="plan.popular">Популярный</div>
          </div>
        </div>

        <!-- Поля формы -->
        <form class="subscription-form__fields" @submit.prevent="submitForm">
          <BaseInput
            v-model="formData.name"
            placeholder="Ваше имя"
            icon="user"
            required
          />

          <BaseInput
            v-model="formData.phone"
            type="tel"
            placeholder="Телефон"
            icon="phone"
            required
          />

          <BaseInput
            v-model="formData.email"
            type="email"
            placeholder="Email"
            icon="email"
          />

          <BaseRecaptcha v-model="formData.recaptcha" />

          <BaseButton
            type="submit"
            size="lg"
            label="Записаться"
            :loading="isSubmitting"
            class="submit-btn"
          />
        </form>
      </div>

      <!-- Сообщение об успехе -->
      <div class="subscription-form__success" v-else>
        <div class="success-icon">
          <svg width="64" height="64" viewBox="0 0 24 24" fill="none">
            <path
              d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"
              fill="$accent"
            />
          </svg>
        </div>
        <h3>Спасибо за заявку!</h3>
        <p>Мы свяжемся с вами для подтверждения брони</p>
        <p class="success-plan" v-if="formData.plan">
          Выбранный абонемент: <strong>{{ formData.plan.name }}</strong>
        </p>
      </div>
    </div>
    <BaseButtonClose
      color="#ffc451"
      top="20px"
      right="20px"
      :size="48"
      @click="closeForm"
    />
  </div>
</template>

<style scoped lang="scss">
.subscription-form {
  position: fixed;
  top: 0;
  right: 0;
  width: 100vw;
  height: 100vh;
  background: $bg;
  z-index: 1000;
  overflow-y: auto;
  animation: slideIn 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);

  &_close {
    animation: slideOut 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  }

  &__wrapper {
    position: relative;
    height: 100%;
    padding: 60px 20px 30px;
    display: flex;
    flex-direction: column;
    max-width: 900px;
    margin: 0 auto;
  }

  &__close-btn {
    position: absolute;
    top: 20px;
    right: 20px;
    background: none;
    border: none;
    color: $accent;
    cursor: pointer;
    z-index: 10;
    padding: 5px;
    transition: opacity 0.3s;

    &:hover {
      opacity: 0.8;
    }

    &:disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }
  }

  &__header {
    text-align: center;
    margin-bottom: 30px;
  }

  &__title {
    font-size: 2.2rem;
    color: $white;
    margin-bottom: 10px;
    font-weight: 700;

    .highlight {
      color: $accent;
    }
  }

  &__subtitle {
    color: rgba($white, 0.8);
    font-size: 1rem;
  }

  &__content {
    display: flex;
    flex-direction: column;
    gap: 30px;
  }

  .subscription-plans {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    margin-bottom: 20px;
  }

  .subscription-plan {
    position: relative;
    background: lighten($bg, 5%);
    border: 2px solid lighten($bg, 10%);
    border-radius: 12px;
    padding: 20px;
    cursor: pointer;
    transition: all 0.3s ease;
    overflow: hidden;

    &:hover {
      transform: translateY(-5px);
      border-color: $accent;
    }

    &.active {
      border-color: $accent;
      box-shadow: 0 0 0 2px $accent;
    }

    &.popular {
      border-color: $accent;

      &::before {
        content: "";
        position: absolute;
        top: 0;
        right: 0;
        width: 0;
        height: 0;
        border-style: solid;
        border-width: 0 50px 50px 0;
        border-color: transparent $accent transparent transparent;
      }
    }
  }

  .plan-title {
    color: $white;
    font-size: 1.3rem;
    margin-bottom: 10px;
  }

  .plan-price {
    color: $accent;
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 15px;
  }

  .plan-features {
    color: rgba($white, 0.8);
    padding-left: 20px;
    margin-bottom: 0;
    line-height: 1.6;

    li {
      margin-bottom: 8px;
      position: relative;

      &::before {
        content: "•";
        color: $accent;
        position: absolute;
        left: -15px;
      }
    }
  }

  .plan-badge {
    position: absolute;
    top: 15px;
    right: 15px;
    background: $red;
    color: $white;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;

    &.popular {
      background: $accent;
      color: $txt;
      top: 8px;
      right: 8px;
      transform: rotate(45deg);
      width: 80px;
      text-align: center;
      right: -25px;
      top: 15px;
    }
  }

  &__fields {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  .submit-btn {
    margin-top: 10px;
    background: $accent;
    color: $txt;
    font-weight: 600;
    transition: all 0.3s;

    &:hover:not(:disabled) {
      transform: translateY(-2px);
      box-shadow: 0 4px 15px rgba($accent, 0.3);
    }
  }

  &__success {
    text-align: center;
    margin: auto;
    max-width: 400px;
    padding: 40px 0;

    h3 {
      color: $accent;
      font-size: 1.8rem;
      margin: 20px 0 10px;
    }

    p {
      color: rgba($white, 0.8);
      font-size: 1.1rem;
      margin-bottom: 5px;
    }

    .success-plan {
      margin-top: 15px;
      color: $accent;
    }
  }

  .success-icon {
    margin: 0 auto;
    width: 80px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba($accent, 0.1);
    border-radius: 50%;
  }
}

@keyframes slideIn {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes slideOut {
  from {
    transform: translateX(0);
    opacity: 1;
  }
  to {
    transform: translateX(100%);
    opacity: 0;
  }
}

@include mediaTablet {
  .subscription-plans {
    grid-template-columns: repeat(3, 1fr);
  }
}
</style>
