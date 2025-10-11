<script lang="ts" setup>
import type { FormField } from "~/types";

const modalsStore = useModalsStore();
const isOpen = ref<boolean>(true);

function closeModalReview() {
  isOpen.value = false;
  setTimeout(() => {
    modalsStore.closeModal("reviewCoachForm");
  }, 450);
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

const captchaInst = ref(null);

function captchaHandler(val, eventName) {
  if (eventName === "success") {
    formData.captcha.value = val;
    formData.captcha.error = "";
  } else if (eventName === "error" || eventName === "expired") {
    formData.captcha.value = "";
    formData.captcha.error = "Ошибка проверки капчи";
  } else if (eventName === "inited" && typeof val === "object") {
    captchaInst.value = val;
  }
}
</script>

<template>
  <div class="modal-coach-review">
    <BaseModalSide
      :is-open="isOpen"
      duration=".45s"
      max-width="450px"
      position="center"
      padding="20px 15px"
      @close="closeModalReview"
    >
      <BaseGridComponent>
        <template #header>
          <h2 class="modal-coach-review_title">Оцените тренера</h2>
          <p class="modal-coach-review__subtitle">
            Ваше мнение поможет другим сделать правильный выбор
          </p>
        </template>
        <template #main>
          <form
            id="reviewForm"
            class="modal-coach-review__form"
            @submit="closeModalReview"
          >
            <RatingComponent class="modal-coach-review__rating" />

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

            <BaseInputTextArea
              v-model:input-value="formData.message.value"
              v-model:error-value="formData.message.error"
              class="modal-coach-review__textarea"
              placeholder="Расскажите о вашем опыте..."
              required
            />

            <BaseCaptcha theme="dark" @verified="captchaHandler" />
          </form>
        </template>
        <template #footer>
          <BaseButton
            form="reviewForm"
            class="modal-coach-review__submit"
            type="submit"
            label="Отправить отзыв"
            size="lg"
            style="width: 100%"
          />
        </template>
      </BaseGridComponent>
    </BaseModalSide>
  </div>
</template>

<style scoped lang="scss">
.modal-coach-review {
  box-shadow: 0 0 20px white;
  max-height: 100vh;
  padding-inline: 15px;
  height: auto;
  
  &:deep(.base-modal-side__content) {
    border-radius: 10px;
  }

  &_title {
    color: $white;
    font-size: 1.8rem;
    margin-bottom: 15px;
  }

  &__subtitle {
    color: rgba($white, 0.7);
    font-size: 0.9rem;
  }
  &__rating {
    margin-bottom: 1rem;
  }
  &__textarea {
    margin-bottom: 40px;
  }

  &__form {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
}
</style>
