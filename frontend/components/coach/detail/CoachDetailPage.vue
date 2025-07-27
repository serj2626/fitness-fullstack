<script setup lang="ts">
import { breadcrumbsCoachDetailPage } from "~/assets/data/breadcrumbs.data";
import { coaches } from "~/assets/data/moke.data";

const trainerStore = useTrainerStore();
const { trainer } = storeToRefs(trainerStore);
const activeTab = ref((useRoute().query.tab as string) || "contacts");

const { id } = useRoute().params;
const coachID = Array.isArray(id) ? id[0] : id;

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

await useAsyncData(`trainer-${coachID}`, () =>
  trainerStore.fetchTrainer(coachID)
);

const loadReviews = () => {
  if (!trainerStore.reviews.length) {
    trainerStore.fetchReviews(coachID);
  }
};

watch(activeTab, (newTab) => {
  if (newTab === "reviews") loadReviews();
  useRouter().replace({ query: { ...useRoute().query, tab: newTab } });
});

onUnmounted(() => {
  trainerStore.reset();
});
</script>

<template>
  <div class="coaches-detail-page">
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="breadcrumbsCoachDetailPage" />

      <div class="coaches-detail-page__layout">
        <CoachDetailProfile
          :avatar="trainer?.avatar"
          class="coaches-detail-page__sidebar"
        />

        <div class="coach-layout__main">
          <CoachDetailTabs
            :active-tab="activeTab"
            @update:active-tab="activeTab = $event"
          />

          <div class="tab-content">
            <CoachDetailContacts
              v-if="activeTab === 'contacts'"
              :name="trainer?.first_name + ' ' + trainer?.last_name"
              :position="trainer?.position || 'Должность тренера'"
              :email="trainer?.email || 'Email тренера'"
              :phone="trainer?.phone || 'Телефон тренера'"
              :socials="trainer?.socials || []"
              :keywords="trainer?.keywords || ''"
              :experience="trainer?.experience || 0"
              :education="trainer?.education || ''"
            />

            <div v-if="activeTab === 'photos'" class="photo-grid">
              <div
                v-for="(photo, index) in images"
                :key="index"
                class="photo-item"
                @click="openViewer(index)"
              >
                <NuxtImg :src="photo" class="photo-img" alt="Фото тренера" />
              </div>
            </div>
            <CoachDetailImages
              v-if="isOpen"
              :images
              :start-index
              @close="isOpen = false"
            />
            <LazyCoachDetailReviews v-if="activeTab === 'reviews'" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.coaches-detail-page {
  padding-block: 100px;

  &__layout {
    margin-top: 50px;
    display: grid;
    grid-template-columns: 300px 1fr;
    gap: 40px;

    @media (max-width: $tablet) {
      grid-template-columns: 1fr;
    }
  }

  &__sidebar {
    position: sticky;
    top: 50px;
    align-self: start;
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

.mb-20 {
  margin-bottom: 20px;
}
.mb-30 {
  margin-bottom: 30px;
}
</style>
