<script setup lang="ts">
import { ref, computed } from 'vue'
import { useModalsStore } from '~/stores/modals'

const modalsStore = useModalsStore()

// Моковые данные
const reviews = ref([
  {
    id: 1,
    name: 'Михаил Смирнов',
    avatar: '/coaches/seventeen.webp',
    rating: 5,
    date: '15 мая 2023',
    text: 'Анна - профессионал высшего класса! За 3 месяца тренировок полностью изменил своё тело. Индивидуальный подход и внимание к деталям. Рекомендую всем, кто серьёзно настроен на результат!',
    photos: [
      '/reviews/1-1.jpg',
      '/reviews/1-2.jpg'
    ]
  },
  {
    id: 2,
    name: 'Екатерина Волкова',
    avatar: '/coaches/fourteen.webp',
    rating: 4,
    date: '2 апреля 2023',
    text: 'Очень довольна тренировками. Анна подобрала программу с учётом моих проблем со спиной. Через месяц уже почувствовала значительные улучшения. Единственное - иногда задерживается на предыдущих тренировках.',
    photos: []
  },
  {
    id: 3,
    name: 'Артём Козлов',
    avatar: '/coaches/nine.jpeg',
    rating: 5,
    date: '20 марта 2023',
    text: 'Лучший тренер в клубе! Мотивирует, поддерживает и даёт реально рабочие советы по питанию. За 2 месяца -8 кг и +5 кг мышечной массы. Продолжаю заниматься!',
    photos: [
      '/coaches/one.webp'
    ]
  },
  {
    id: 4,
    name: 'Ольга Новикова',
    avatar: '/coaches/four.jpeg',
    rating: 5,
    date: '5 марта 2023',
    text: 'Занимаюсь с Анной уже год. Ни разу не пожалела о выборе. Всегда находит правильные слова, когда нет настроения тренироваться. Тело полностью преобразилось!',
    photos: []
  }
])

// Сортировка
const sortBy = ref('newest')
const sortOptions = [
  { value: 'newest', label: 'Сначала новые' },
  { value: 'highest', label: 'Высокий рейтинг' },
  { value: 'lowest', label: 'Низкий рейтинг' }
]

const sortedReviews = computed(() => {
  const sorted = [...reviews.value]
  switch (sortBy.value) {
    case 'newest':
      return sorted.sort((a, b) => new Date(b.date) - new Date(a.date))
    case 'highest':
      return sorted.sort((a, b) => b.rating - a.rating)
    case 'lowest':
      return sorted.sort((a, b) => a.rating - b.rating)
    default:
      return sorted
  }
})

// Пагинация
const shownReviews = ref(3)

// Просмотр фото
const openPhotoViewer = (photos: string[], index: number) => {
  // Здесь можно реализовать открытие полноэкранного просмотрщика
  console.log('Открыть фото:', photos[index])
}
</script>
<template>
  <div class="coach-reviews">
    <!-- Заголовок и кнопка -->
    <div class="reviews-header">
      <h2 class="reviews-title">
        Отзывы <span class="reviews-count">{{ reviews.length }}</span>
      </h2>
      <BaseButton
        label="Оставить отзыв"
        size="md"
        :outline="true"
        @click="modalsStore.openModal('reviewCoachForm')"
      />
    </div>

    <!-- Сортировка -->
    <div class="reviews-sorting">
      <button
        v-for="sort in sortOptions"
        :key="sort.value"
        :class="{ active: sortBy === sort.value }"
        @click="sortBy = sort.value"
      >
        {{ sort.label }}
      </button>
    </div>

    <!-- Список отзывов -->
    <div class="reviews-list">
      <div 
        v-for="review in sortedReviews"
        :key="review.id"
        class="review-card"
      >
        <div class="review-header">
          <div class="review-author">
            <NuxtImg 
              :src="review.avatar" 
              class="review-avatar"
              alt="Аватар"
            />
            <div class="author-info">
              <h3 class="author-name">{{ review.name }}</h3>
              <div class="review-date">{{ review.date }}</div>
            </div>
          </div>
          <RatingComponent 
            :rating="review.rating" 
            :size="20"
            readonly
          />
        </div>

        <div class="review-content">
          <p class="review-text">{{ review.text }}</p>
          
          <!-- Фото отзыва -->
          <div v-if="review.photos.length" class="review-photos">
            <NuxtImg
              v-for="(photo, index) in review.photos"
              :key="index"
              :src="photo"
              class="review-photo"
              @click="openPhotoViewer(review.photos, index)"
            />
          </div>
        </div>
      </div>
    </div>

    <!-- Кнопка "Показать еще" -->
    <BaseButton
      v-if="reviews.length > shownReviews"
      label="Показать еще"
      variant="outline"
      size="md"
      class="load-more"
      @click="shownReviews += 3"
    />
  </div>
</template>
<style scoped lang="scss">
.coach-reviews {
  padding: 20px;
  background: rgba($white, 0.03);
  border-radius: 12px;
}

.reviews-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
}

.reviews-title {
  font-size: 24px;
  font-weight: 700;
  color: $white;
  display: flex;
  align-items: center;
  gap: 10px;
}

.reviews-count {
  font-size: 16px;
  color: rgba($white, 0.7);
  font-weight: 400;
}

.reviews-sorting {
  display: flex;
  gap: 15px;
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 1px solid rgba($white, 0.1);

  button {
    background: none;
    border: none;
    color: rgba($white, 0.7);
    font-size: 14px;
    cursor: pointer;
    padding: 5px 10px;
    border-radius: 6px;
    transition: all 0.3s;

    &.active {
      background: rgba($accent, 0.2);
      color: $accent;
    }

    &:hover:not(.active) {
      color: $white;
    }
  }
}

.reviews-list {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.review-card {
  background: rgba($white, 0.05);
  border-radius: 12px;
  padding: 20px;
  transition: transform 0.3s;

  &:hover {
    transform: translateY(-3px);
  }
}

.review-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 15px;
}

.review-author {
  display: flex;
  align-items: center;
  gap: 15px;
}

.review-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid $accent;
}

.author-info {
  display: flex;
  flex-direction: column;
}

.author-name {
  font-size: 16px;
  font-weight: 600;
  color: $white;
  margin-bottom: 3px;
}

.review-date {
  font-size: 14px;
  color: rgba($white, 0.6);
}

.review-content {
  padding-left: 65px;
}

.review-text {
  font-size: 15px;
  line-height: 1.6;
  color: rgba($white, 0.9);
  margin-bottom: 15px;
}

.review-photos {
  display: flex;
  gap: 10px;
  margin-top: 15px;
}

.review-photo {
  width: 80px;
  height: 80px;
  border-radius: 8px;
  object-fit: cover;
  cursor: pointer;
  transition: transform 0.3s;

  &:hover {
    transform: scale(1.05);
  }
}

.load-more {
  margin-top: 30px;
  width: 100%;
}
</style>