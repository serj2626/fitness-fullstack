<script setup lang="ts">
defineProps({
  isOpen: {
    type: Boolean,
    default: true,
  },
});

const modalsStore = useModalsStore();
const emit = defineEmits(["close"]);

const email = ref("");
const errorMessage = ref("");
const successMessage = ref("");

const closeModal = () => {
  emit("close");
  resetForm();
};

const resetForm = () => {
  email.value = "";
  errorMessage.value = "";
  successMessage.value = "";
};

const handleSubmit = async () => {
  try {
    // Здесь API-запрос к Django (например, через useFetch)
    const { data, error } = await useFetch("/api/auth/password/reset/", {
      method: "POST",
      body: { email: email.value },
    });

    if (error.value) {
      throw new Error(error.value.data?.detail || "Ошибка сервера");
    }

    successMessage.value = "Письмо с инструкциями отправлено на ваш email!";
    setTimeout(closeModal, 3000);
  } catch (err) {
    errorMessage.value = err.message || "Произошла ошибка";
  }
};
</script>
<template>
  <div class="modal-password-recovery">
    <div class="modal-password-recovery__content">
      <BaseButtonClose
        top="10px"
        right="10px"
        :size="26"
        @click="modalsStore.closeModal('passwordRecovery')"
      />
      <div class="modal-password-recovery__header">
        <h2 class="modal-password-recovery__title">Восстановление пароля</h2>
        <p class="modal-password-recovery__subtitle">
          Укажите email, который вы использовали при регистрации
        </p>
      </div>

      <form class="modal-password-recovery__form" @submit.prevent="handleSubmit">
        <BaseInput
          v-model="email"
          type="email"
          placeholder="Ваш email"
          required
          class="modal-password-recovery__input"
        />
        <BaseButton
          type="submit"
          label="Отправить ссылку"
          size="lg"
          style="width: 100%"
        />

        <p v-if="errorMessage" class="modal-password-recovery__error">
          {{ errorMessage }}
        </p>

        <p v-if="successMessage" class="modal-password-recovery__success">
          {{ successMessage }}
        </p>
      </form>
    </div>
  </div>
</template>
<style scoped lang="scss">
.modal-password-recovery {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

  &__content {
    position: relative;
    width: 100%;
    max-width: 500px;
    background: $bg;
    border-radius: 12px;
    padding: 40px;
    box-shadow: 0 0 20px #fff;
    z-index: 2;
    border: 1px solid rgba($accent, 0.3);

    @media (max-width: $tablet) {
      padding: 30px 20px;
      margin: 0 15px;
    }
  }

  &__close {
    position: absolute;
    top: 20px;
    right: 20px;
    background: transparent;
    border: none;
    cursor: pointer;
    color: $header_link;
    transition: transform 0.3s;

    &:hover {
      transform: rotate(90deg);
      color: $accent;
    }
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
