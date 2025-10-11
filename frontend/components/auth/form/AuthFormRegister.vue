<script setup lang="ts">
import { api } from "~/api";
import type { FormField } from "~/types";

const { $api } = useNuxtApp();

defineEmits(["openLoginForm"]);

interface FeedbackForm {
  email: FormField<string>;
  phone: FormField<string>;
  password: FormField<string>;
  password2: FormField<string>;
  agree: FormField<boolean>;
  captcha: FormField<string>;
}

const captchaInst = ref(null);

const formData = reactive<FeedbackForm>({
  email: { value: "", error: "", required: true },
  phone: { value: "", error: "", required: true },
  password: { value: "", error: "", required: true },
  password2: { value: "", error: "", required: true },
  agree: { value: false, error: "", required: true },
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
  <div class="modal-register">
    <div class="modal-register__wrapper">
      <div class="modal-register__header">
        <h3>Создать аккаунт</h3>
        <p>Заполните форму для регистрации</p>
      </div>

      <form class="modal-register__form" @submit.prevent="submitForm">
        <BaseInput
          v-model:input-value="formData.email.value"
          v-model:error="formData.email.error"
          type="email"
          placeholder="Email"
          icon="email"
          required
        />
        <BaseInput
          v-model:input-value="formData.phone.value"
          v-model:error="formData.phone.error"
          placeholder="Ваш телефон"
          icon="user"
          required
        />

        <BaseInput
          v-model:input-value="formData.password.value"
          v-model:error="formData.password.error"
          type="password"
          placeholder="Пароль"
          icon="lock"
          required
        />

        <BaseInput
          v-model:input-value="formData.password2.value"
          v-model:error="formData.password2.error"
          type="password"
          placeholder="Повторите пароль"
          icon="lock"
          required
        />
        <BaseInputCheckbox
          v-model:agree-value="formData.agree.value"
          v-model:agree-error="formData.agree.error"
        >
          <span @click.stop
            >Я согласен с <a href="#">правилами</a> и
            <NuxtLink to="/policy">политикой конфиденциальности</NuxtLink></span
          >
        </BaseInputCheckbox>
        <BaseCaptcha theme="dark" @verified="captchaHandler" />

        <BaseButton
          type="submit"
          size="lg"
          style="width: 100%"
          label="Зарегистрироваться"
        />

        <div class="modal-register__footer">
          <span>Уже есть аккаунт?</span>
          <button type="button" @click="$emit('openLoginForm')">Войти</button>
        </div>
      </form>
    </div>
  </div>
</template>
<style scoped lang="scss">
.modal-register {
  &__wrapper {
    position: relative;
    background: $bg;
    border-radius: 12px;
    padding: 40px 30px;
    width: 100%;
    box-shadow: 0 0 20px #fff;
  }

  &__header {
    text-align: center;
    margin-bottom: 30px;

    h3 {
      color: $white;
      font-size: 1.8rem;
      margin-bottom: 8px;
    }

    p {
      color: rgba($white, 0.7);
      font-size: 0.9rem;
    }
  }

  &__form {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  &__agree {
    display: flex;
    align-items: flex-start;
    gap: 8px;
    color: rgba($white, 0.8);
    font-size: 0.85rem;
    line-height: 1.4;
    cursor: pointer;
    margin-top: 10px;

    input {
      margin-top: 3px;
      accent-color: $accent;
      flex-shrink: 0;
    }

    a {
      color: $accent;
      text-decoration: none;

      &:hover {
        text-decoration: underline;
      }
    }
  }

  &__submit {
    margin-top: 10px;
    background: $accent;
    color: $txt;
    font-weight: 600;
  }

  &__footer {
    text-align: center;
    margin-top: 20px;
    color: rgba($white, 0.7);
    font-size: 0.9rem;

    button {
      background: none;
      border: none;
      color: $accent;
      cursor: pointer;
      margin-left: 5px;
      font-weight: 500;
    }
  }
}
</style>
