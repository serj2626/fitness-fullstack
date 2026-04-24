<script setup lang="ts">
import { api } from "~/api";
import { breadcrumbsCoachesPage } from "~/assets/data/breadcrumbs.data";
import type { ICoach } from "~/types";

const reviewsStore = useReviewsStore();

const route = useRoute();
const router = useRouter();

const activeTab = ref((route.query.tab as string) || "contacts");

const setActiveTab = (tab: string) => {
  activeTab.value = tab;
  router.replace({ query: { ...route.query, tab } });
};

const { $api } = useNuxtApp();

const { id } = useRoute().params;
const coachID = computed<string>(() => (Array.isArray(id) ? id[0] : id));

const { data: coachData } = await useAsyncData<ICoach>(
  `coach-${coachID.value}`,
  () => $api(api.coaches.detail(id as string)),
  {
    watch: [() => id],
  },
);

useLazyAsyncData("reviews-list", async () => {
  await reviewsStore.getAllReviews(1, 6, coachID.value);
  return reviewsStore.reviews;
});

onUnmounted(() => {
  reviewsStore.reset();
});
</script>

<template>
  <div class="coaches-detail-page">
    <div class="container">
      <BaseBreadCrumbs
        :breadcrumbs="breadcrumbsCoachesPage"
        :current-page="{
          title: coachData?.first_name + ' ' + coachData?.last_name,
          url: `/coaches/${coachID}`,
        }"
      />
      <div class="coaches-detail-page__layout">
        <CoachDetailProfile
          :avatar="coachData?.avatar as string"
          class="coaches-detail-page__sidebar"
        />

        <div class="coach-layout__main">
          <CoachDetailTabs
            :active-tab="activeTab"
            @update:active-tab="setActiveTab"
          />

          <div class="tab-content">
            <CoachDetailContacts
              v-if="activeTab === 'contacts'"
              :name="coachData?.first_name + ' ' + coachData?.last_name"
              :categories="coachData?.categories || []"
              :email="coachData?.email || 'Email тренера'"
              :phone="coachData?.phone || 'Телефон тренера'"
              :experience="coachData?.experience || 0"
              :socials="coachData?.socials || []"
            />
            <LazyCoachDetailServices
              v-if="activeTab === 'services'"
              :services="coachData?.services || []"
            />
            <LazyCoachDetailReviews
              v-if="activeTab === 'reviews'"
              :reviews-count="reviewsStore.count"
              :reviews="reviewsStore.reviews"
              :loading="reviewsStore.loading"
            />
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
