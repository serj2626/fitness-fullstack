<script setup lang="ts">
const { success, error: errorNotify } = useNotify();
const { formData } = useForm({
  text: { value: "", error: "", required: true },
  rating: { value: "", error: "", required: true },
});

const submit = async () => {
  if (formData.text.value && formData.rating.value  && formData.text.value.length > 5) {
    success("Отзыв отправлен", 3000);
    formData.text.value = "";
    formData.rating.value = "";
  } else {
    errorNotify("Заполните все поля");
  }
};
</script>

<template>
  <form class="review-form" @submit.prevent="submit">
    <div class="review-form__header">
      <h3 class="review-form__title">Оставить отзыв</h3>
      <RatingComponent
        v-model="formData.rating.value"
        editable
        class="review-form__rating"
      />
    </div>

    <BaseInputTextArea
      v-model:input-value="formData.text.value"
      placeholder="Расскажите о своём опыте..."
      class="review-form__textarea"
    />

    <BaseButton
      label="Оставить отзыв"
      size="md"
      color="#1a8f1a"
      class="review-form__button"
      :disabled="!formData.text.value || !formData.rating.value"
    />
  </form>
</template>

<style scoped lang="scss">
.review-form {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(2px);
  border-radius: 24px;
  padding: 24px;
  margin-bottom: 32px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: all 0.2s ease;

  &__header {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    margin-bottom: 20px;
  }

  &__title {
    font-size: 1.2rem;
    font-weight: 600;
    color: $white;
    margin: 0;
  }

  &__textarea {
    width: 100%;
    margin-bottom: 20px;

    :deep(textarea) {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 16px;

      color: $white;
      font-size: 0.95rem;
      transition: border 0.2s ease-in, box-shadow 0.4s ease-in;

      &:focus {
        border-color: $accent;
        outline: none;
        box-shadow: 5px 5px 20px rgba(252, 252, 252, 0.469);
      }
    }
  }

  &__button {
    width: 100%;
    color: $white;

    @include mediaMobile {
      width: auto;
      min-width: 180px;
      margin-left: auto;
    }
  }
}
</style>
