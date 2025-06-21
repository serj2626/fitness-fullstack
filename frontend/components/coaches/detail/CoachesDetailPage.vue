<script setup lang="ts">
import { coaches } from "~/assets/data/moke.data";
const modalsStore = useModalsStore();
const activeTab = ref('contacts');


const isOpen = ref(false);
const startIndex = ref(0);

const openViewer = (index: number) => {
  startIndex.value = index;
  isOpen.value = true;
};
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
const images = computed(() => {
  const listImages = coaches.slice(0, 8).map((item) => item.img);
  return listImages;
});

const tabs = [
  { id: 'contacts', label: 'Контакты' },
  { id: 'photos', label: 'Фотографии' },
  { id: 'reviews', label: 'Отзывы' }
];

// Остальной код (images, openViewer и т.д.) без изменений
</script>

<template>
  <div class="coaches-detail-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs class="mb-30" />
      
      <div class="coach-layout">
        <!-- Блок профиля (остаётся слева) -->
        <CoachesDetailProfile class="coach-layout__sidebar" />
        
        <!-- Основной контент -->
        <div class="coach-layout__main">
          <!-- Кнопки-табы -->
          <div class="tab-buttons">
            <button 
              v-for="tab in tabs"
              :key="tab.id"
              :class="{ 'active': activeTab === tab.id }"
              @click="activeTab = tab.id"
            >
              {{ tab.label }}
            </button>
          </div>
          
          <!-- Контент -->
          <div class="tab-content">
            <!-- Контакты -->
            <CoachesDetailContacts v-if="activeTab === 'contacts'" />
            
            <!-- Галерея -->
            <div v-if="activeTab === 'photos'" class="photo-grid">
              <div 
                v-for="(photo, index) in images"
                :key="index"
                class="photo-item"
                @click="openViewer(index)"
              >
                <NuxtImg 
                  :src="photo" 
                  class="photo-img"
                  alt="Фото тренера"
                />
              </div>
            </div>

                 <CoachesDetailImages
        v-if="isOpen"
        :images
        :start-index
        @close="isOpen = false"
      />
            
            <!-- Отзывы -->
            <CoachesDetailReviews v-if="activeTab === 'reviews'" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped lang="scss">
.coaches-detail-page {
  padding: 40px 0;
  background: $bg;
}

.coach-layout {
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 40px;
  
  @media (max-width: $tablet) {
    grid-template-columns: 1fr;
  }
  
  &__sidebar {
    position: sticky;
    top: 20px;
    align-self: start;
  }
}

.tab-buttons {
  display: flex;
  border-bottom: 1px solid rgba($white, 0.1);
  margin-bottom: 30px;
  
  button {
    padding: 12px 25px;
    color: rgba($white, 0.7);
    position: relative;
    font-weight: 500;
    
    &.active {
      color: $accent;
      
      &::after {
        content: '';
        position: absolute;
        bottom: -1px;
        left: 0;
        width: 100%;
        height: 2px;
        background: $accent;
      }
    }
  }
}

.photo-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 15px;
}

.photo-item {
  border-radius: 12px;
  overflow: hidden;
  aspect-ratio: 1/1;
  transition: transform 0.3s;
  
  &:hover {
    transform: scale(1.03);
  }
}

.photo-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.reviews-section {
  padding-top: 20px;
}

.mb-20 { margin-bottom: 20px; }
.mb-30 { margin-bottom: 30px; }
</style>