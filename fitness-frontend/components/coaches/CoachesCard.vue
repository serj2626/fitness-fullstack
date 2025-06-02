<script lang="ts" setup>
import type { ICoach } from "~/assets/data/moke.data";
defineProps<{
  coach: ICoach;
}>();
</script>
<template>
  <NuxtLink :to="`/coaches/${coach.id}`">
    <div class="coaches-card">
      <NuxtImg class="coaches-card__img" :src="coach.img" />
      <p class="coaches-card__name">{{ coach.name }}</p>
    </div>
  </NuxtLink>
</template>
<style scoped lang="scss">
.coaches-card {
  position: relative;
  height: 500px;
  background-color: #fff;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 0 15px rgba(255, 255, 255, 0.611);
  cursor: pointer;
  &__name {
    position: absolute;
    display: none;
    top: 20%;
    left: 50%;
    transform: translateX(-50%);
    color: #fff;
    font-size: 20px;
    font-weight: 500;
    text-align: center;
    text-transform: uppercase;
    z-index: 100;
  }
  &__img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: all 0.9s ease-in;
  }
}

.coaches-card:hover {
  .coaches-card__img {
    scale: 1.1;
    filter: brightness(0.7);
  }
  .coaches-card__name {
    transition: all 0.9s ease-in;
    display: block;
    animation: show_name 0.9s linear;
  }
}
@keyframes show_name {
  from {
    opacity: 0;
    transform: translate(-50%, -100%);
  }
  to {
    opacity: 1;
    transform: translate(-50%, 0);
  }
}
</style>
