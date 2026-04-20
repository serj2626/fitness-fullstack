<script setup lang="ts">
import { api } from "~/api";
import { breadcrumbsCoachesPage } from "~/assets/data/breadcrumbs.data";
import type { ICoach, IReview } from "~/types";

const activeTab = ref((useRoute().query.tab as string) || "contacts");

const { $api } = useNuxtApp();

const { id } = useRoute().params;
const coachID = computed(() => (Array.isArray(id) ? id[0] : id));

const { data: coachData } = await useAsyncData<ICoach>(
  `coach-${coachID.value}`,
  () => $api(api.coaches.detail(id as string)),
  {
    watch: [() => id],
  },
);

// const loadReviews = () => {
//   if (!trainerStore.reviews.length) {
//     trainerStore.fetchReviews(coachID);
//   }
// };

const { data: reviewsData } = useAsyncData<IReview[]>(
  "coaches-list-page-reviews-list",
  () =>
    $api(api.reviews.list, {
      query: {
        id: id as string,
      },
    }),
  {
    lazy: false,
  },
);

// watch(activeTab, (newTab) => {
//   if (newTab === "reviews") loadReviews();
//   useRouter().replace({ query: { ...useRoute().query, tab: newTab } });
// });

// onUnmounted(() => {
//   trainerStore.reset();
// });
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
            @update:active-tab="activeTab = $event"
          />

          <div class="tab-content">
            <CoachDetailContacts
              v-if="activeTab === 'contacts'"
              :name="coachData?.first_name + ' ' + coachData?.last_name"
              :categories="coachData?.categories || []"
              :email="coachData?.email || 'Email тренера'"
              :phone="coachData?.phone || 'Телефон тренера'"
              :experience="coachData?.experience || 0"
            />
            <LazyCoachDetailServices
              v-if="activeTab === 'services'"
              :services="coachData?.services || []"
            />
            <LazyCoachDetailReviews
              v-if="activeTab === 'reviews'"
              :reviews="reviewsData || []"
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
