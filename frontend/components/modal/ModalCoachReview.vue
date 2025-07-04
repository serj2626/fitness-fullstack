<script lang="ts" setup>
const modalsStore = useModalsStore();
const isClosing = ref(false);
const isSubmitted = ref(false);

function closeListReviews() {
  isClosing.value = true;
}

function handleSubmit(e: Event) {
  e.preventDefault();
  isSubmitted.value = true;
  setTimeout(() => closeListReviews(), 1500); // Закрываем после успешной отправки
}

function handleAnimationEnd() {
  if (isClosing.value) {
    modalsStore.closeModal("reviewCoachForm");
  }
}

interface FormField<T> {
  value: T;
  error: string;
  required: boolean;
}

interface FeedbackForm {
  name: FormField<string>;
  email: FormField<string>;
  message: FormField<string>;
  captcha: FormField<string>;
}

const formData = reactive<FeedbackForm>({
  name: { value: "", error: "", required: true },
  email: { value: "", error: "", required: true },
  message: { value: "", error: "", required: true },
  captcha: { value: "", error: "", required: true },
});
</script>

<template>
  <div class="modal-coach-review__card">
    <BaseButtonClose
      top="15px"
      right="15px"
      :size="36"
      @click="modalsStore.closeModal('reviewCoachForm')"
    />

    <div class="modal-coach-review__content">
      <h2 class="modal-coach-review__title">Оцените тренера</h2>
      <p class="modal-coach-review__subtitle">
        Ваше мнение поможет другим сделать правильный выбор
      </p>

      <form class="modal-coach-review__form">
        <RatingComponent class="modal-coach-review__rating" />

        <div class="modal-coach-review__form-grid">
          <BaseInput
            v-model:input-value="formData.name.value"
            v-model:error="formData.name.error"
            class="modal-coach-review__input"
            placeholder="Ваше имя"
            required
          />
          <BaseInput
            v-model:input-value="formData.email.value"
            v-model:error="formData.email.error"
            class="modal-coach-review__input"
            placeholder="Ваш email"
            type="email"
            required
          />
        </div>

        <BaseInputTextArea
          v-model:input-value="formData.message.value"
          v-model:error-value="formData.message.error"
          class="modal-coach-review__textarea"
          placeholder="Расскажите о вашем опыте..."
          required
        />

        <BaseRecaptcha
          v-model:input-value="formData.captcha.value"
          class="modal-coach-review__recaptcha"
        />

        <BaseButton
          class="modal-coach-review__submit"
          type="submit"
          label="Отправить отзыв"
          size="lg"
          style="width: 100%;"
        />
      </form>
    </div>
  </div>
</template>

<style scoped lang="scss">
.modal-coach-review {
  &__card {
    position: relative;
    width: 100%;
    max-width: 600px;
    height: 100%;
    // max-height: 700px;
    margin-inline: auto;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    border-radius: 16px;
    padding: 40px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    overflow-x: hidden;
    overflow-y: auto;
    z-index: 2;
    border: 1px solid rgba(255, 255, 255, 0.1);

    @include mediaMobile {
      padding: 30px 20px;
      height: 100vh;
      max-height: 100vh;
      border-radius: 0;
    }
  }
  &__content {
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  &__title {
    font-size: 28px;
    font-weight: 700;
    color: white;
    margin-bottom: 8px;
    text-align: center;
    background: linear-gradient(90deg, #ffffff, #a5b4fc);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;

    @include mediaMobile {
      font-size: 24px;
    }
  }

  &__subtitle {
    font-size: 16px;
    color: rgba(255, 255, 255, 0.7);
    text-align: center;
    margin-bottom: 30px;
  }

  &__form {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  &__form-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;

    @include mediaMobile {
      grid-template-columns: 1fr;
    }
  }

  &__input:deep(.base-input__field) {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: white;
    transition: all 0.3s;

    &:focus {
      border-color: #6366f1;
      box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2);
    }

    &::placeholder {
      color: rgba(255, 255, 255, 0.4);
    }
  }

  &__textarea:deep(.base-input-text-area__input) {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: white;
    min-height: 150px;
    transition: all 0.3s;

    &:focus {
      border-color: #6366f1;
      box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2);
    }

    &::placeholder {
      color: rgba(255, 255, 255, 0.4);
    }
  }

  &__submit:deep(.base-button) {
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white;
    font-weight: 600;
    border: none;
    transition: all 0.3s;
    margin-top: 10px;

    &:hover {
      transform: translateY(-2px);
      box-shadow: 0 5px 15px rgba(99, 102, 241, 0.4);
    }
  }
}

@keyframes checkmark {
  0% {
    opacity: 0;
    transform: scale(0.5);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}
</style>
