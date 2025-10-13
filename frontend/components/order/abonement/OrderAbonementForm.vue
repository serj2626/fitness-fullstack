<script setup lang="ts">
import type { FormField } from "~/types";

interface FeedbackForm {
  name: FormField<string>;
  email: FormField<string>;
  phone: FormField<string>;
  captcha: FormField<string>;
  abonement: FormField<number | null>;
  date: FormField<Date | null>;
}

const formData = reactive<FeedbackForm>({
  name: { value: "", error: "", required: true },
  phone: { value: "", error: "", required: true },
  email: { value: "", error: "", required: true },
  captcha: { value: "", error: "", required: true },
  abonement: { value: null, error: "", required: true },
  date: { value: null, error: "", required: true },
});
</script>
<template>
  <form class="order-abonement-form">
    <BaseGridComponent>
      <template #header>
        <h3 class="order-abonement-form__title">Выберите дату</h3>
      </template>
      <template #main>
        <div class="order-abonement-form__main">
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
            placeholder="Почта"
            icon="email"
          />
          <VDatePicker
            v-model="formData.date.value"
            color="orange"
            title-position="left"
            trim-weeks
          />
        </div>
      </template>
      <template #footer>
        <div class="order-abonement-form__footer">
          <BaseCaptcha
            theme="dark"
            @verified="formData.captcha.value = $event"
          />

          <BaseButton
            type="submit"
            size="lg"
            label="Записаться"
            style="width: 100%"
          />
        </div>
      </template>
    </BaseGridComponent>
  </form>
</template>
<style scoped lang="scss">
.order-abonement-form {
  max-width: 500px;
  width: 100%;
  margin: 0 auto;
}
.order-abonement-form__title {
  text-align: center;
  font-size: clamp(1.5rem, 3vw, 2.5rem);
  color: $accent;
}
.order-abonement-form__main {
  display: flex;
  flex-direction: column;
  gap: 15px;
}
.order-abonement-form__footer {
  display: flex;
  flex-direction: column;
  gap: 15px;
}
</style>
