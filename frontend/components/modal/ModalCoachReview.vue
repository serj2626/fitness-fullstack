<script lang="ts" setup>
const modalsStore = useModalsStore();
const isClosing = ref(false);

function closeModalReview() {
  isClosing.value = true;
  setTimeout(() => {
    modalsStore.closeModal("reviewCoachForm");
  }, 300);
}

useEscapeKey(closeModalReview);

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
  <div class="modal-overlay" @click.self="closeModalReview">
    <div class="modal-coach-review__card" :class="{ closing: isClosing }">
      <BaseButtonClose
        top="15px"
        right="15px"
        :size="36"
        @click="closeModalReview"
      />

      <div class="modal-coach-review__content">
        <h2 class="modal-coach-review__title">Оцените тренера</h2>
        <p class="modal-coach-review__subtitle">
          Ваше мнение поможет другим сделать правильный выбор
        </p>

        <form class="modal-coach-review__form" @submit="closeModalReview">
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
            style="width: 100%"
          />
        </form>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: flex-start;
  z-index: 1000;
}

.modal-coach-review {
  &__card {
    position: relative;
    width: 100%;
    max-width: 100%;
    height: 100vh;
    margin-left: 0;
    background: $bg;
    padding: 40px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    overflow-x: hidden;
    overflow-y: auto;
    z-index: 2;
    border: 1px solid rgba(255, 255, 255, 0.1);
    animation: slideInLeft 0.3s ease-out forwards;

    &.closing {
      animation: slideOutLeft 0.3s ease-in forwards;
    }

    @include mediaTablet {
      padding: 30px 20px;
      max-width: 30vw;
    }

    @include mediaLaptop {
      max-width: 40vw;
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

@keyframes slideInLeft {
  from {
    transform: translateX(-100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes slideOutLeft {
  from {
    transform: translateX(0);
    opacity: 1;
  }
  to {
    transform: translateX(-100%);
    opacity: 0;
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
