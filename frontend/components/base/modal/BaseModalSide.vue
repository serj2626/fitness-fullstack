<script setup lang="ts">
const {
  isOpen = true,
  maxWidth = "736px",
  position = "right",
  background = "white",
  duration = ".3s",
} = defineProps<{
  isOpen?: boolean;
  maxWidth?:
    | "400px"
    | "450px"
    | "500px"
    | "550px"
    | "600px"
    | "650px"
    | "700px"
    | "736px"
    | "750px"
    | "800px"
    | "850px"
    | "900px"
    | "950px";

  position?: "left" | "right" | "center";
  background?: "white" | "blue";
  duration?: ".3s" | ".35s" | ".4s" | ".45s" | ".5s";
}>();

const emit = defineEmits<{
  close: [];
}>();

const handleEsc = (e: KeyboardEvent) => {
  if (e.key === "Escape") {
    emit("close");
  }
};

onMounted(() => {
  document.addEventListener("keydown", handleEsc);
});
onUnmounted(() => {
  document.removeEventListener("keydown", handleEsc);
});
</script>

<template>
  <div
    class="base-modal-side"
    :class="[`base-modal-side_${position}`, `base-modal-side_${background}`]"
    @click.self="emit('close')"
  >
    <div
      class="base-modal-side__content"
      :class="[
        `base-modal-side__content_${position}`,
        `base-modal-side__content_${background}`,
        { 'base-modal-side__content_close': !isOpen },
      ]"
    >
      <BaseButtonClose
        :size="36"
        color="black"
        top="15px"
        right="15px"
        class="base-modal-side__close"
        @click="emit('close')"
      />

      <slot />
    </div>
  </div>
</template>

<style scoped lang="scss">
@include slide-animation("right", 100%, 0);
@include slide-animation("left", -100%, 0);

.base-modal-side {
  position: fixed;
  top: 0;
  right: 0;
  width: 100vw;
  height: 100vh;
  display: flex;
  z-index: 9999;

  &_left {
    justify-content: flex-start;
  }
  &_right {
    justify-content: flex-end;
  }

  &_center {
    justify-content: center;
    align-items: center;
  }

  &__content {
    padding: 24px 40px 24px 16px;
    max-width: v-bind(maxWidth);
    width: 100%;
    position: relative;

    &_white {
      background-color: $bg-light;
    }
    &_blue {
      background: $gradient-menu-mobile;

      .base-modal-side__close {
        color: $white;
      }
    }

    &_right {
      height: 100%;
      animation: right-in 0.3s ease forwards;

      &.base-modal-side__content_close {
        animation: right-out 0.3s ease forwards;
      }
    }

    &_left {
      height: 100%;
      animation: left-in 0.3s ease forwards;

      &.base-modal-side__content_close {
        animation: left-out 0.3s ease forwards;
      }
    }

    &_center {
      animation: center-in v-bind(duration) ease forwards;

      &.base-modal-side__content_close {
        animation: center-out v-bind(duration) ease forwards;
      }
    }
  }
}

@keyframes center-in {
  from {
    opacity: 0;
    transform: translateY(-100%);
    opacity: 0;
  }
  to {
    opacity: 1;
    transform: translateY(0);
    opacity: 1;
  }
}

@keyframes center-out {
  from {
    opacity: 1;
    transform: translateY(0);
    opacity: 1;
  }
  to {
    opacity: 0;
    transform: translateY(-100%);
    opacity: 0;
  }
}
</style>
