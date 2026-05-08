<script setup lang="ts">
const store = useReviewsStore();

const { id } = useRoute().params;

const coachId = computed<string>(() => (Array.isArray(id) ? id[0] : id));

const { success, error: errorNotify } = useNotify();
const { formData } = useForm({
  text: { value: "", error: "", required: true },
  rating: { value: "", error: "", required: true },
  anonymous: { value: false, error: "", required: false },
});

const submit = async () => {
  const text = formData.text.value.trim();
  const rating = Number(formData.rating.value);

  // 🔥 Жёсткая валидация
  if (!text || !rating || text.length <= 5 || rating < 1 || rating > 5) {
    errorNotify("Заполните все поля и выберите рейтинг");
    return;
  }

  const payload = {
    coach: coachId.value,
    rating,
    text,
    anonymous: formData.anonymous.value, // 🔥 Передаём чекбокс!
    user: null,
  };

  try {
    await store.createNewReview(payload);
    success("Отзыв отправлен", 3000);

    formData.text.value = "";
    formData.rating.value = "";
    formData.anonymous.value = false;
  } catch {
    errorNotify("Произошла ошибка при отправке. Попробуйте позже.");
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
        size="md"
        class="review-form__rating"
      />
    </div>

    <BaseInputTextArea
      v-model:input-value="formData.text.value"
      placeholder="Расскажите о своём опыте..."
      class="review-form__textarea"
    />
    <div class="review-form__footer">
      <BaseInputCheckbox>
        <span class="review-form__footer-checkbox-label">
          Отправить анонимно
        </span>
      </BaseInputCheckbox>
      <BaseButton
        label="Оставить отзыв"
        size="md"
        color="#1a8f1a"
        class="review-form__footer-button"
        :disabled="!formData.text.value || !formData.rating.value"
      />
    </div>
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
      transition:
        border 0.2s ease-in,
        box-shadow 0.4s ease-in;

      &:focus {
        border-color: $accent;
        outline: none;
        box-shadow: 5px 5px 20px rgba(252, 252, 252, 0.469);
      }
    }
  }
  &__footer {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    &-button {
      color: $white;
    }
  }
}
</style>
