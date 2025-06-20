<script lang="ts" setup>
import { coaches } from "~/assets/data/moke.data";
const modalsStore = useModalsStore();

const isOpen = ref(false);
const startIndex = ref(0);

const openViewer = (index: number) => {
  startIndex.value = index;
  isOpen.value = true;
};

const images = computed(() => {
  const listImages = coaches.slice(0, 8).map((item) => item.img);
  return listImages;
});

const breadcrumbs = ref([
  {
    title: "Главная",
    url: "/",
  },
  {
    title: "Тренеры",
    url: "/coaches",
  },
  {
    title: "Тренер",
    url: "/coaches/1",
  },
]);
</script>
<template>
  <div class="coaches-detail-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs />
      <div class="coaches-detail-page__content">
        <CoachesDetailProfile class="coaches-detail-page__content-profile" />
        <div class="coaches-detail-page__content-main">
          <div class="coaches-detail-page__content-main-actions">
            <button class="coaches-detail-page__content-main-actions-item">
              Контакты
            </button>
            <button
              class="coaches-detail-page__content-main-actions-item"
              @click="modalsStore.openModal('reviewCoachForm')"
            >
              Отзывы
            </button>
            <button class="coaches-detail-page__content-main-actions-item">
              Фотографии
            </button>
          </div>
          <div class="coaches-detail-page__content-main-concats">
            <CoachesDetailContacts />
          </div>
          <div class="coaches-detail-page__content-main-images">
            <NuxtImg
              v-for="(photo, index) in images"
              :key="index"
              :src="photo"
              class="coaches-detail-page__content-main-images-item"
              @click="openViewer(index)"
            />
          </div>
        </div>
      </div>
      <CoachesDetailImages
        v-if="isOpen"
        :images
        :start-index
        @close="isOpen = false"
      />
    </div>
  </div>
</template>
<style lang="scss" scoped>
.coaches-detail-page {
  padding-block: 80px 30px;

  &__content {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 50px;
    padding-block: 50px;
    overflow: visible;

    &-profile {
      position: sticky;
      top: 80px;

      // ✅ Для надежности можно добавить:
      align-self: start;
    }

    &-main {
      display: flex;
      flex-direction: column;
      gap: 20px;

      &-actions {
        display: flex;
        justify-content: center;
        gap: 40px;

        &-item {
          position: relative;
          border-radius: 5px;
          background-color: $bg;
          color: $white;
          font-size: 17px;
          font-weight: 500;
          cursor: pointer;
          transition: all 0.3s ease-in;

          &:hover {
            color: $accent;
          }

          &:before {
            content: "";
            position: absolute;
            left: 0;
            bottom: -4px;
            width: 100%;
            height: 2px;
            background-color: $accent;
          }
        }
      }

      &-images {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;

        &-item {
          width: 100%;
          height: 250px;
          object-fit: cover;
          border-radius: 20px;
          box-shadow: 0 0 15px rgba(255, 255, 255, 0.611);
          cursor: pointer;
        }
      }
    }
  }
}
</style>
