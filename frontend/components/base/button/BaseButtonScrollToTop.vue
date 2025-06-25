<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";
import { HeroIcons } from "~/assets/icons/types/hero-icons";

const showButton = ref(false);

const checkScroll = () => {
  showButton.value = window.scrollY > window.innerHeight;
};

const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
};

onMounted(() => {
  window.addEventListener("scroll", checkScroll);
});
onUnmounted(() => {
  window.removeEventListener("scroll", checkScroll);
});
</script>

<template>
  <button v-if="showButton" class="scroll-to-top" @click="scrollToTop">
    <Icon :name="HeroIcons.ARROW_UP" size="26" />
  </button>
</template>

<style scoped lang="scss">
.scroll-to-top {
  position: fixed;
  bottom: 20px;
  left: 40px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: $accent;
  color: #fff;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  box-shadow: 0 0 15px $accent;
  transition: all 0.3s ease;
  z-index: 999;
  animation: scaleBtn 0.5s linear;

  &:hover {
    opacity: 0.8;
  }
  &:active {
    scale: 0.9;
  }
}

@keyframes scaleBtn {
  0% {
    transform: scale(1);
    opacity: 0.5;
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}
</style>
