<script lang="ts" setup>
const modalsStore = useModalsStore();
defineProps<{
  avatar: string | undefined;
}>();
</script>
<template>
  <div class="coaches-detail-profile" v-bind="$attrs">
    <NuxtImg class="coaches-detail-profile__img" :src="avatar" alt="Аватар" />

    <RatingComponent
      class="coaches-detail-profile__rating"
      :rating="4.5"
      :count="5"
    />
    <p style="text-align: center;margin-top: 10px; color: sandybrown">4 из 5</p>
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
