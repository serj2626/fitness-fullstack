<script lang="ts" setup>
const modalsStore = useModalsStore();
defineProps<{
  avatar: string | null;
  rating: number;
}>();
</script>
<template>
  <div class="coaches-detail-profile" v-bind="$attrs">
    <NuxtImg
      format="webp"
      lazy="loading"
      class="coaches-detail-profile__img"
      :src="getPhoto(avatar as string)"
      alt="Аватар"
    />

    <RatingComponent
      class="coaches-detail-profile__rating"
      :rating="rating"
      :count="5"
    />
    <p style="text-align: center; margin-top: 10px; color: sandybrown">
      {{ Math.floor(rating) }}  из 5
    </p>
    <BaseButton
      size="lg"
      label="Записаться"
      class="coaches-detail-profile__button"
      @click="modalsStore.openModal('orderTraining')"
    />
  </div>
</template>
<style scoped lang="scss">
.coaches-detail-profile {
  &__img {
    width: 100%;
    height: auto;
    border-radius: 10px;
    margin-bottom: 30px;
  }
  &__rating {
  }
  &__button {
    display: block;
    width: 100%;
    margin-top: 20px;
  }
}
</style>
