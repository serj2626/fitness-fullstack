<script lang="ts" setup>
const selectedDate = ref<Date | null>(null);
const modalsStore = useModalsStore();
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

const { data: abonements } = useAbonements();

const isClosing = ref(false);
const isSubmitting = ref(false);

const closeForm = () => {
  if (isSubmitting.value) {
    useNotify().warning("Пожалуйста, дождитесь окончания бронирования");
    return;
  }
  isClosing.value = true;
};

const handleAnimationEnd = () => {
  if (isClosing.value) {
    modalsStore.closeModal("orderAbonement");
  }
};

const selectAbonement = (id: number) => {
  if (formData.abonement.value === id) {
    formData.abonement.value = null;
  } else {
    formData.abonement.value = id;
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
  abonement: FormField<number | null>;
}

const formData = reactive<FeedbackForm>({
  name: { value: "", error: "", required: true },
  phone: { value: "", error: "", required: true },
  email: { value: "", error: "", required: true },
  captcha: { value: "", error: "", required: true },
  abonement: { value: null, error: "", required: true },
});
</script>

<template>
  <div
    class="base-form-order-abonement"
    :class="{ 'base-form-order-abonement_close': isClosing }"
    @animationend="handleAnimationEnd"
  >
    <div class="base-form-order-abonement__wrapper">
      <div class="base-form-order-abonement__header">
        <h2 class="base-form-order-abonement__header-title">
          <span class="base-form-order-abonement__header-title_highlight"
            >Бронирование</span
          >
          абонемента
        </h2>
        <p class="base-form-order-abonement__header-subtitle">
          Оставьте заявку и мы подберем для вас оптимальный вариант
        </p>
      </div>

      <!-- Основное содержимое -->
      <div class="base-form-order-abonement__content">
        <div class="base-form-order-abonement__list-plans">
          <AbonementCardByForm
            v-for="plan in abonements"
            :key="plan.id"
            :plan="plan"
            :is-active="plan.id === formData.abonement.value"
            @click="selectAbonement(plan.id)"
          />
        </div>

        <VDatePicker
          v-model="selectedDate"
          :attributes="attributes"
          :min-date="new Date()"
          color="orange"
          is-dark
          title-position="left"
          trim-weeks
        />

        <form class="base-form-order-abonement__form">
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

      <!-- Сообщение об успехе -->
      <!-- <div v-else class="base-form-order-abonement__success">
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
      </div> -->
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
.base-form-order-abonement {
  position: fixed;
  top: 0;
  right: 0;
  width: 100vw;
  min-height: 100vh;
  height: 100%;
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

  &__header {
    text-align: center;
    margin-bottom: 30px;
    &-title {
      font-size: 2.2rem;
      color: $white;
      margin-bottom: 10px;
      font-weight: 700;

      &_highlight {
        color: $accent;
      }
    }

    &-subtitle {
      color: rgba($white, 0.8);
      font-size: 1rem;
    }
  }

  &__content {
    display: flex;
    flex-direction: column;
    gap: 30px;
  }

  .base-form-order-abonement__list-plans {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    margin-bottom: 20px;
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
  .base-form-order-abonement__list-plans {
    grid-template-columns: repeat(3, 1fr);
  }
}
</style>
