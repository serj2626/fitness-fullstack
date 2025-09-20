<script setup lang="ts">
import type { IServicesResponse } from "~/types";
const modalsStore = useModalsStore();

const data: IServicesResponse | undefined =
  modalsStore.activeModals.get("service");

const close = ref(false);

const closeModal = () => {
  close.value = true;
  setTimeout(() => {
    modalsStore.closeModal("service");
  }, 500);
};
</script>

<template>
  <div class="modal-data" @click.self="closeModal">
    <div
      class="modal-data__content"
      :class="{ 'modal-data__content_close': close }"
    >
      <div class="modal-data__content-header">
        <div class="header-content">
          <p class="modal-data__content-header-title">
            {{ data?.alt || "Услуга" }}
          </p>
          <BaseButtonClose
            :size="40"
            top="25px"
            right="25px"
            @click="closeModal"
          />
        </div>
      </div>

      <div class="image-container">
        <NuxtImg
          :src="data?.avatar || ''"
          alt="Услуга"
          class="modal-data__content-img"
          loading="lazy"
          format="webp"
        />
      </div>

      <div class="modal-data__content-main">
        <BaseWysiwyg v-if="data?.content" :html="data.content" />
      </div>
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
  z-index: 160;
  display: flex;
  justify-content: flex-end;
  align-items: stretch;

  &__content {
    position: relative;
    width: 100vw;
    height: 100%;
    animation: slideInLeft 0.5s ease-in-out forwards;
    background: $bg;
    padding: 2.5rem;
    display: flex;
    color: $white;
    flex-direction: column;
    overflow-y: auto;
    border-right: 1px solid rgba(99, 102, 241, 0.3);
    box-shadow: 0 0 50px rgba(0, 0, 0, 0.5);

    @include mediaTablet {
      width: 50vw;
    }
    @include mediaLaptop {
      width: 45vw;
    }

    &_close {
      animation: slideOutLeft 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    &-header {
      margin-bottom: 2rem;

      .header-content {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        position: relative;

        &:deep(.base-button-close) {
          position: static;
        }
      }

      &-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: $white;
        margin: 0;
        background: linear-gradient(
          135deg,
          #ffffff 0%,
          #a5b4fc 50%,
          #6366f1 100%
        );
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 4px 20px rgba(99, 102, 241, 0.3);
        line-height: 1.2;
        max-width: 80%;
      }
    }
  }
}

.image-container {
  position: relative;
  width: 100%;
  height: 450px;
  margin-bottom: 2.5rem;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.modal-data__content-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center center;
  transition: transform 0.3s ease;
}

.modal-data__content-main {
  flex-grow: 2;
  position: relative;
  z-index: 2;

  :deep(*) {
    color: rgba(255, 255, 255, 0.9);
    line-height: 1.7;
  }

  :deep(h1),
  :deep(h2),
  :deep(h3),
  :deep(h4) {
    color: $white;
    margin-top: 2rem;
    margin-bottom: 1rem;
    background: linear-gradient(135deg, #ffffff 0%, #a5b4fc 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  :deep(a) {
    color: #8b5cf6;
    text-decoration: none;
    border-bottom: 1px solid rgba(139, 92, 246, 0.3);
    transition: all 0.3s ease;

    &:hover {
      color: #6366f1;
      border-bottom-color: #6366f1;
    }
  }

  :deep(ul),
  :deep(ol) {
    padding-left: 1.5rem;
    margin: 1.5rem 0;
  }

  :deep(li) {
    margin: 0.5rem 0;
    position: relative;
  }

  :deep(strong) {
    color: $white;
    font-weight: 600;
  }
}

// Анимации
@keyframes slideInLeft {
  from {
    transform: translateX(100%);
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
    transform: translateX(100%);
    opacity: 0;
  }
}

// // Адаптивность
// @include mediaMobile {
//   .modal-data__content {
//     padding: 1.5rem;

//     &-header-title {
//       font-size: 1.8rem;
//       max-width: 70%;
//     }
//   }

//   .image-container {
//     height: 200px;
//     margin-bottom: 2rem;
//   }
// }

// @include mediaTablet {
//   .modal-data__content {
//     border-radius: 24px 0 0 24px;
//     // margin: 1rem 0;
//     height: calc(100vh - 2rem);
//   }
// }

// Прокрутка
.modal-data__content::-webkit-scrollbar {
  width: 6px;
}

.modal-data__content::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 3px;
}

.modal-data__content::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg, #6366f1 0%, #8b5cf6 100%);
  border-radius: 3px;
}

.modal-data__content::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(180deg, #8b5cf6 0%, #ec4899 100%);
}
</style>
