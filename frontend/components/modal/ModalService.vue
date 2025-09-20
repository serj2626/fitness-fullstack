<script setup lang="ts">
const modalsStore = useModalsStore();
const close = ref(false);

const closeModal = () => {
  close.value = true;
  setTimeout(() => {
    modalsStore.closeModal("menu");
  }, 500);
};
</script>

<template>
  <div class="modal-data" @click.self="closeModal">
    <div
      class="modal-data__content"
      :class="{ 'modal-data__content_close': close }"
    >
      <BaseButtonClose
        :size="33"
        top="20px"
        right="20px"
        class="modal-data__close-btn"
        @click="closeModal"
      />
    </div>
  </div>
</template>

<style scoped lang="scss">
.modal-data {
  position: fixed;
  top: 0;
  right: 0;
  width: 100vw;
  height: 100vh;
  backdrop-filter: blur(10px);
  z-index: 1000;
  display: flex;
  justify-content: flex-start;
  align-items: stretch;

  &__content {
    position: relative;
    width: 100vw;
    height: 100%;
    animation: slideInLeft 0.5s ease-in-out forwards;
    background-color: $warning;
    padding: 2rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow-y: auto;
    border-right: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 0 50px rgba(0, 0, 0, 0.3);

    @include mediaTablet {
      width: 40vw;
    }
    @include mediaLaptop {
      width: 30vw;
    }

    &_close {
      animation: slideOutLeft 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
  }
}

// Анимации
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

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

// Адаптивность
@include mediaMobile {
  .modal-data__content {
    padding: 1.5rem;
  }

  .modal-data__content-nav-list-item-link {
    padding: 0.875rem 1.25rem;
  }
}
</style>
