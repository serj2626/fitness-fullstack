<script lang="ts" setup>
const modalsStore = useModalsStore();
</script>
<template>
  <div class="coaches-detail-profile" v-bind="$attrs">
    <NuxtImg class="coaches-detail-profile__img" src="/coaches/five.webp" />
    <RatingComponent
      class="coaches-detail-profile__rating"
      :rating="4.5"
      :count="5"
    />
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
    border-radius: 15px;
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
