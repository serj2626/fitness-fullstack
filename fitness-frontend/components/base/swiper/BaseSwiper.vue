<script setup lang="ts">
const {
  defaultCount = 1,
  defaultBetween = 20,
  mobileCount = 1,
  mobileBetween = 20,
  tabletCount = 3,
  tabletBetween = 30,
  laptopCount = 4,
  laptopBetween = 20,
  desctopCount = 4,
  desctopBetween = 20,
  autoDelay = 1500,
  loop = true,
} = defineProps<{
  defaultCount?: number;
  defaultBetween?: number;
  mobileCount?: number;
  mobileBetween?: number;
  tabletCount?: number;
  tabletBetween?: number;
  laptopCount?: number;
  laptopBetween?: number;
  desctopCount?: number;
  desctopBetween?: number;
  autoDelay?: number;
  loop?: boolean;
  pagination?: boolean;
}>();

const containerRef = ref(null);
const swiper = useSwiper(containerRef, {
  parallax: true,
  loop,
  ...(autoDelay > 0 && {
    autoplay: {
      delay: autoDelay,
      disableOnInteraction: false,
    },
  }),
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    renderBullet: function (index, className) {
      return `<span class="${className}"><span class="bullet-inner"></span></span>`;
    },
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    0: {
      slidesPerView: defaultCount,
      spaceBetween: defaultBetween,
    },
    375: {
      slidesPerView: mobileCount,
      spaceBetween: mobileBetween,
    },
    768: {
      slidesPerView: tabletCount,
      spaceBetween: tabletBetween,
    },
    1024: {
      slidesPerView: laptopCount,
      spaceBetween: laptopBetween,
    },
    1200: {
      slidesPerView: desctopCount,
      spaceBetween: desctopBetween,
    },
  },
});
onMounted(() => {
  console.log(swiper.instance);
});
</script>

<template>
  <ClientOnly>
    <swiper-container ref="containerRef" :init="false">
      <slot />
      <div class="swiper-pagination"></div>
    </swiper-container>
  </ClientOnly>
</template>
<style lang="scss" scoped>
.swiper-pagination {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-top: 16px;
}

.swiper-pagination-bullet {
  position: relative;
  width: 40px;
  height: 6px;
  background-color: #e0e0e0; /* серый цвет */
  border-radius: 3px;
  transition: background-color 0.3s;
}

.swiper-pagination-bullet-active {
  background-color: #c1a27d; /* бежевый цвет */
}

.swiper-pagination-bullet-active::after {
  content: '';
  position: absolute;
  top: -6px;
  left: 50%;
  transform: translateX(-50%);
  border-left: 6px solid transparent;
  border-right: 6px solid transparent;
  border-bottom: 6px solid #c1a27d;
}
</style>