<script lang="ts" setup>
import AuthFormLogin from "../auth/form/AuthFormLogin.vue";
import AuthFormRegister from "../auth/form/AuthFormRegister.vue";
import AuthFormPasswordRecovery from "../auth/form/AuthFormPasswordRecovery.vue";

const modalsStore = useModalsStore();
const isOpen = ref<boolean>(true);

const closeModal = () => {
  isOpen.value = false;
  setTimeout(() => {
    modalsStore.closeModal("auth");
  }, 350);
};

const type = ref<"login" | "register" | "passwordRecovery">("login");

const modalMap = {
  login: AuthFormLogin,
  register: AuthFormRegister,
  passwordRecovery: AuthFormPasswordRecovery,
};
</script>

<template>
  <BaseModalSide
    max-width="450px"
    position="center"
    duration=".35s"
    :is-open="isOpen"
    @close="closeModal"
  >
    <component
      :is="modalMap[type]"
      :open-register-form="(type = 'register')"
      :open-password-recovery-form="(type = 'passwordRecovery')"
      :open-login-form="(type = 'login')"
    />
  </BaseModalSide>
</template>
