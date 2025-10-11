<script setup lang="ts">
import { api } from "~/api";
import type { FormField } from "~/types";

defineProps({
  isOpen: {
    type: Boolean,
    default: true,
  },
});

const emit = defineEmits(["close"]);
const { $api } = useNuxtApp();
const captchaInst = ref(null);

interface FeedbackForm {
  email: FormField<string>;
  captcha: FormField<string>;
}

const formData = reactive<FeedbackForm>({
  email: { value: "", error: "", required: true },
  captcha: { value: "", error: "", required: true },
});

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
const submitForm = async () => {
  console.log("submitForm", formData);

  try {
    const res = await $api(api.users.register, {
      method: "POST",
      body: {
        email: formData.email.value,
        phone: formData.phone.value,
        password: formData.password.value,
        password2: formData.password2.value,
      },
    });
    console.log(res);
  } catch (error) {
    console.log(error);
  }
};
</script>
<template>
  <div class="modal-password-recovery">
    <div class="modal-password-recovery__content">
      <div class="modal-password-recovery__header">
        <h2 class="modal-password-recovery__title">Восстановление пароля</h2>
        <p class="modal-password-recovery__subtitle">
          Укажите email, который вы использовали при регистрации
        </p>
      </div>

      <form
        class="modal-password-recovery__form"
        @submit.prevent="submitForm"
      >
        <BaseInput
          v-model:input-value="formData.email.value"
          v-model:error="formData.email.error"
          type="email"
          placeholder="Ваш email"
          required
          class="modal-password-recovery__input"
        />
        <BaseCaptcha theme="dark" @verified="captchaHandler" />
        <BaseButton
          type="submit"
          label="Отправить ссылку"
          size="lg"
          style="width: 100%"
        />
<!-- 
        <p v-if="errorMessage" class="modal-password-recovery__error">
          {{ errorMessage }}
        </p>

        <p v-if="successMessage" class="modal-password-recovery__success">
          {{ successMessage }}
        </p> -->
      </form>
    </div>
  </div>
</template>
<style scoped lang="scss">
.modal-password-recovery {
  &__content {
    position: relative;
    width: 100%;
    background: $bg;
    border-radius: 12px;
    padding: 40px;
    box-shadow: 0 0 20px #fff;
    z-index: 2;
    border: 1px solid rgba($accent, 0.3);
  }

  &__header {
    margin-bottom: 30px;
    text-align: center;
  }

  &__title {
    font-size: 24px;
    color: $white;
    margin-bottom: 10px;
    font-weight: 700;

    @media (max-width: $tablet) {
      font-size: 20px;
    }
  }

  &__subtitle {
    font-size: 16px;
    color: rgba($white, 0.7);
    line-height: 1.5;
  }

  &__form {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  &__input:deep(.base-input__field) {
    background: rgba($white, 0.05);
    border: 1px solid rgba($white, 0.1);
    color: $white;
    width: 100%;

    &:focus {
      border-color: $accent;
      box-shadow: 0 0 0 2px rgba($accent, 0.2);
    }

    &::placeholder {
      color: rgba($white, 0.4);
    }
  }

  &__submit:deep(.base-button) {
    background: $accent;
    color: $txt;
    font-weight: 600;
    border: none;
    transition: all 0.3s;

    &:hover {
      transform: translateY(-2px);
      box-shadow: 0 5px 15px rgba($accent, 0.4);
    }
  }

  &__error {
    color: $error;
    font-size: 14px;
    text-align: center;
    margin-top: 10px;
  }

  &__success {
    color: $accent;
    font-size: 14px;
    text-align: center;
    margin-top: 10px;
  }
}
</style>
