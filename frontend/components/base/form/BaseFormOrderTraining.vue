<script lang="ts" setup>
import { coaches } from "~/assets/data/moke.data";
const modalsStore = useModalsStore();

// Состояния компонента
const isClosing = ref(false);
const isSubmitting = ref(false);
const submitSuccess = ref(false);
const selectedDate = ref<Date | null>(null);

// Данные формы
const formData = reactive({
  name: "",
  phone: "",
  email: "",
  coach: null,
  recaptcha: "",
});

// Занятые даты для календаря
const busyDates = ["2025-05-04", "2025-05-07", "2025-05-10"];
const attributes = [
  {
    key: "busy",
    highlight: { backgroundColor: "$red", borderColor: "$error" },
    dates: busyDates,
  },
  {
    key: "today",
    highlight: { backgroundColor: "$accent", borderColor: "$accent" },
    dates: [new Date()],
  },
];

// Закрытие формы с анимацией
const closeForm = () => {
  if (isSubmitting.value) {
    useNotify().warning("Пожалуйста, дождитесь окончания отправки");
    return;
  }
  isClosing.value = true;
};

// Обработчик окончания анимации
const handleAnimationEnd = () => {
  if (isClosing.value) {
    resetForm();
    modalsStore.closeModal("orderTraining");
  }
};

// Сброс формы
const resetForm = () => {
  formData.name = "";
  formData.phone = "";
  formData.email = "";
  formData.coach = null;
  formData.recaptcha = "";
  selectedDate.value = null;
  isSubmitting.value = false;
  submitSuccess.value = false;
  isClosing.value = false;
};

// Отправка формы
// const submitForm = async () => {
//   if (!validateForm()) return;

//   isSubmitting.value = true;

//   try {
//     // Имитация запроса к API
//     await new Promise(resolve => setTimeout(resolve, 1500));

//     submitSuccess.value = true;
//     useNotify().success('Запись успешно оформлена!');
//     setTimeout(closeForm, 2000);
//   } catch (error) {
//     useNotify().error('Ошибка при отправке формы');
//   } finally {
//     isSubmitting.value = false;
//   }
// };

const submitForm = async () => {
  isSubmitting.value = true;
};

// Валидация формы
const validateForm = () => {
  if (!selectedDate.value) {
    useNotify().error("Выберите дату тренировки");
    return false;
  }

  if (!formData.name.trim()) {
    useNotify().error("Введите ваше имя");
    return false;
  }

  if (!formData.phone.trim()) {
    useNotify().error("Введите номер телефона");
    return false;
  }

  return true;
};
</script>

<template>
  <div
    class="training-form"
    :class="{ 'training-form_close': isClosing }"
    @animationend="handleAnimationEnd"
  >
    <div class="training-form__wrapper">
      <!-- Заголовок формы -->
      <div class="training-form__header">
        <h2 class="training-form__title">
          <span class="highlight">Персональная</span> тренировка
        </h2>
        <p class="training-form__subtitle">
          Заполните форму и наш менеджер свяжется с вами для подтверждения
        </p>
      </div>

      <!-- Основное содержимое -->
      <div class="training-form__content" v-if="!submitSuccess">
        <!-- Календарь -->
        <div class="training-form__calendar">
          <VDatePicker
            v-model="selectedDate"
            :attributes="attributes"
            :min-date="new Date()"
            color="orange"
            is-dark
            title-position="left"
            trim-weeks
          />
          <div class="calendar-legend">
            <div class="legend-item">
              <span class="legend-busy"></span>
              <span>Занято</span>
            </div>
            <div class="legend-item">
              <span class="legend-today"></span>
              <span>Сегодня</span>
            </div>
          </div>
        </div>

        <!-- Поля формы -->
        <form class="training-form__fields" @submit.prevent="submitForm">
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
            required
          />

          <BaseInputSelect
            v-model="formData.coach"
            :options="coaches"
            placeholder="Выберите тренера"
            icon="coach"
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
      <div class="training-form__success" v-else>
        <div class="success-icon">
          <svg width="64" height="64" viewBox="0 0 24 24" fill="none">
            <path
              d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"
              fill="$accent"
            />
          </svg>
        </div>
        <h3>Спасибо за заявку!</h3>
        <p>Мы свяжемся с вами в ближайшее время</p>
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
.training-form {
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
    max-width: 1200px;
    margin: 0 auto;
  }

  &__header {
    text-align: center;
    margin-bottom: 30px;
  }

  &__title {
    font-size: 2.5rem;
    color: $white;
    margin-bottom: 10px;
    font-weight: 700;

    .highlight {
      color: $accent;
    }
  }

  &__subtitle {
    color: rgba($white, 0.8);
    font-size: 1.1rem;
  }

  &__content {
    display: grid;
    grid-template-columns: 1fr;
    gap: 30px;

    @media (min-width: $tablet) {
      grid-template-columns: 1fr 1fr;
      align-items: flex-start;
    }
  }

  &__calendar {
    background: lighten($bg, 5%);
    border-radius: 12px;
    padding: 20px;
    position: sticky;
    top: 20px;

    :deep(.vc-container) {
      border: none;
      background: transparent;
      width: 100%;
    }

    :deep(.vc-title) {
      color: $white;
    }

    :deep(.vc-day-content) {
      color: $white;
      font-weight: 500;
    }

    :deep(.vc-highlight) {
      background: $accent;
      color: $txt;
    }
  }

  .calendar-legend {
    display: flex;
    gap: 15px;
    margin-top: 20px;
    justify-content: center;

    .legend-item {
      display: flex;
      align-items: center;
      gap: 5px;
      color: $white;
      font-size: 0.9rem;
    }

    .legend-busy {
      display: inline-block;
      width: 16px;
      height: 16px;
      background: $red;
      border-radius: 50%;
    }

    .legend-today {
      display: inline-block;
      width: 16px;
      height: 16px;
      background: $accent;
      border-radius: 50%;
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

    &:hover {
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

  .close-btn {
    position: absolute;
    top: 20px;
    right: 20px;
    z-index: 10;
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
</style>
