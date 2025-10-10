<script setup lang="ts">
import type { IServicesResponse } from "~/types";
const modalsStore = useModalsStore();

const data = modalsStore.activeModals.get("service") as
  | IServicesResponse
  | undefined;

const close = ref(false);

const isOpen = ref<boolean>(true);

const closeModal = () => {
  close.value = true;
  setTimeout(() => {
    modalsStore.closeModal("service");
  }, 450);
};
</script>

<template>
  <div class="modal-service">
      <BaseModalSide duration=".45s" :is-open="isOpen" @close="closeModal">
    <BaseGridComponent>
      <template #header>
        <div class="modal-service__header">
          <p class="modal-service__header-title">
            {{ data?.alt || "Услуга" }}
          </p>
        </div>
      </template>
      <template #main>
        <div class="modal-service_content">
          <div class="modal-service_content-image">
            <NuxtImg
              :src="getMedia(data?.img_url || '')"
              alt="Услуга"
              class="modal-service_content-image__img"
              loading="lazy"
              format="webp"
            />
          </div>

          <div class="modal-service_content-main">
            <BaseWysiwyg v-if="data?.content" :html="data.content" />
          </div>
        </div>
      </template>
    </BaseGridComponent>
  </BaseModalSide>
  </div>
</template>

<style scoped lang="scss">
.modal-service {
  &__header {
    padding: 1rem 0;

    &-title {
      font-size: 2rem;
      font-weight: 600;
      color: $white;
    }
  }

  &_content {
    display: flex;
    flex-direction: column;
    gap: 2rem;

    &-image {
      position: relative;
      width: 100%;
      min-height: 250px;
      height: auto;
      max-height: 60vh;
      aspect-ratio: 16/9;
      margin-bottom: 2.5rem;
      border-radius: 16px;
      overflow: hidden;

      &__img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center center;
        transition: transform 0.3s ease;
      }
    }
  }
}


// /* Прокрутка */
// .modal-service_content::-webkit-scrollbar {
//   width: 6px;
// }

// .modal-service_content::-webkit-scrollbar-track {
//   background: rgba(255, 255, 255, 0.05);
//   border-radius: 3px;
// }

// .modal-service_content::-webkit-scrollbar-thumb {
//   background: $accent;
//   border-radius: 3px;
// }

// .modal-service_content::-webkit-scrollbar-thumb:hover {
//   background: linear-gradient(180deg, #8b5cf6 0%, #ec4899 100%);
// }

</style>
