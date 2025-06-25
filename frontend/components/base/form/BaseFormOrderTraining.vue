<script lang="ts" setup>
import { ref, computed, watch } from "vue";
import { coaches } from "~/assets/data/moke.data";
import { useModalsStore } from "~/stores/modals";


const modalsStore = useModalsStore();

// Состояния компонента
const isClosing = ref(false);
const isSubmitting = ref(false);
const selectedDate = ref<Date | null>(null);
const selectedTime = ref<string | null>(null);
const selectedCoach = ref<string | null>(null);
const submitSuccess = ref(false);

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

// Временные слоты
const timeSlots = ref([
  "09:00",
  "10:00",
  "11:00",
  "12:00",
  "14:00",
  "15:00",
  "16:00",
  "17:00",
  "18:00",
]);

// Занятые временные слоты (можно заменить на API запрос)
const busyTimes = computed(() => {
  if (!selectedDate.value) return [];
  // Здесь можно добавить логику получения занятых слотов
  return ["10:00", "14:00"]; // Пример занятых слотов
});

// Доступные временные слоты
const availableTimes = computed(() => {
  return timeSlots.value.filter((time) => !busyTimes.value.includes(time));
});

// Сброс времени при изменении даты
watch(selectedDate, () => {
  selectedTime.value = null;
});

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
    modalsStore.closeModal("orderTraining");
  }
};

// Валидация формы
const validateForm = () => {
  if (!selectedDate.value) {
    useNotify().error("Выберите дату тренировки");
    return false;
  }

  if (!selectedTime.value) {
    useNotify().error("Выберите время тренировки");
    return false;
  }

  if (!selectedCoach.value) {
    useNotify().error("Выберите тренера");
    return false;
  }

  return true;
};

// Отправка формы
const submitForm = async () => {
  if (!validateForm()) return;

  isSubmitting.value = true;

  try {
    // Имитация запроса к API
    await new Promise((resolve) => setTimeout(resolve, 1500));

    const formData = {
      date: selectedDate.value,
      time: selectedTime.value,
      coach: selectedCoach.value,
      client: {
        name: formData.name.value,
        phone: formData.phone.value,
        email: formData.email.value,
      },
    };

    submitSuccess.value = true;
    useNotify().success(
      `Запись на ${formData.date?.toLocaleDateString()} в ${
        formData.time
      } успешно оформлена!`
    );
    setTimeout(closeForm, 2000);
  } catch (error) {
    useNotify().error("Ошибка при отправке формы");
  } finally {
    isSubmitting.value = false;
  }
};


interface FormField<T> {
  value: T;
  error: string;
  required: boolean;
}

interface FeedbackForm {
  name: FormField<string>;
  email: FormField<string>;
  phone: FormField<string>;
  captcha: FormField<string>;
  abonement: FormField<string>;
}

const formData = reactive<FeedbackForm>({
  name: { value: "", error: "", required: true },
  phone: { value: "", error: "", required: true },
  email: { value: "", error: "", required: true },
  captcha: { value: "", error: "", required: true },
  abonement: { value: "", error: "", required: true },
});
</script>

<template>
  <div
    class="base-form-order-training"
    :class="{ 'base-form-order-training_close': isClosing }"
    @animationend="handleAnimationEnd"
  >
    <div class="base-form-order-training__wrapper">
      <div v-if="!submitSuccess">
        <!-- Заголовок формы -->
        <div class="base-form-order-training__header">
          <h2 class="base-form-order-training__header-title">
            <span class="base-form-order-training__header-title_highlight"
              >Персональная</span
            >
            тренировка
          </h2>
          <p class="base-form-order-training__header-subtitle">
            Заполните форму и наш менеджер свяжется с вами для подтверждения
          </p>
        </div>

        <div class="base-form-order-training__content">
          <div class="base-form-order-training__calendar">
            <VDatePicker
              v-model="selectedDate"
              :attributes="attributes"
              :min-date="new Date()"
              color="orange"
              is-dark
              title-position="left"
              trim-weeks
            />

            <!-- Блок выбора времени -->
            <div class="time-selection" v-if="selectedDate">
              <h3 class="time-selection__title">Выберите время</h3>
              <div class="time-slots">
                <button
                  v-for="time in availableTimes"
                  :key="time"
                  class="time-slot"
                  :class="{
                    'time-slot--selected': selectedTime === time,
                    'time-slot--busy': busyTimes.includes(time),
                  }"
                  @click="selectedTime = time"
                  :disabled="busyTimes.includes(time)"
                >
                  {{ time }}
                </button>
              </div>
            </div>

            <div class="calendar-legend">
              <div class="legend-item">
                <span class="legend-busy"></span>
                <span>Занято</span>
              </div>
              <div class="legend-item">
                <span class="legend-today"></span>
                <span>Сегодня</span>
              </div>
              <div class="legend-item">
                <span class="legend-selected"></span>
                <span>Выбрано</span>
              </div>
            </div>
          </div>

          <form
            class="base-form-order-training__form"
            @submit.prevent="submitForm"
          >
            <BaseInput
              v-model:input-value="formData.name.value"
              v-model:error="formData.name.error"
              placeholder="Ваше имя"
              icon="user"
              required
            />

            <BaseInput
              v-model:input-value="formData.phone.value"
              v-model:error="formData.phone.error"
              type="tel"
              placeholder="Телефон"
              icon="phone"
              required
            />

            <BaseInput
              v-model:input-value="formData.email.value"
              v-model:error="formData.email.error"
              type="email"
              placeholder="Email"
              icon="email"
              required
            />

            <BaseInputSelect
              v-model="selectedCoach"
              :options="coaches"
              placeholder="Выберите тренера"
              icon="coach"
              required
            />

            <BaseRecaptcha v-model="formData.captcha.value" />

            <BaseButton
              type="submit"
              size="lg"
              label="Записаться"
              :loading="isSubmitting"
              style="width: 100%"
            />
          </form>
        </div>
      </div>

      <!-- Сообщение об успехе -->
      <div v-else class="base-form-order-training__success">
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
.base-form-order-training {
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

    &-title {
      font-size: 2.5rem;
      color: $white;
      margin-bottom: 10px;
      font-weight: 700;

      &_highlight {
        color: $accent;
      }
    }

    &-subtitle {
      color: rgba($white, 0.8);
      font-size: 1.1rem;
    }
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

  .time-selection {
    margin-top: 20px;
    padding-top: 20px;
    border-top: 1px solid rgba($white, 0.1);

    &__title {
      color: $white;
      font-size: 1.2rem;
      margin-bottom: 15px;
    }
  }

  .time-slots {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;

    @media (max-width: $mobile) {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  .time-slot {
    background: rgba($white, 0.1);
    border: 1px solid rgba($white, 0.2);
    color: $white;
    padding: 8px 12px;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
    font-size: 0.9rem;
    text-align: center;

    &:hover {
      background: rgba($accent, 0.2);
      border-color: $accent;
    }

    &--selected {
      background: $accent;
      color: $txt;
      font-weight: bold;
    }

    &--busy {
      opacity: 0.5;
      cursor: not-allowed;
      text-decoration: line-through;
    }
  }

  .calendar-legend {
    display: flex;
    gap: 15px;
    margin-top: 20px;
    justify-content: center;
    flex-wrap: wrap;

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

    .legend-selected {
      display: inline-block;
      width: 16px;
      height: 16px;
      background: $accent;
      border-radius: 50%;
    }
  }

  &__form {
    display: flex;
    flex-direction: column;
    gap: 20px;
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
