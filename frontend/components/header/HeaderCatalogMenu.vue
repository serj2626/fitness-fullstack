<script lang="ts" setup>
import { headerLinks } from "~/assets/data/header-links";
import { HeroIcons } from "~/assets/icons/types/hero-icons";

const modalsStore = useModalsStore();
const isClosing = ref(false);

function closeListReviews() {
  isClosing.value = true;
}

function handleAnimationEnd() {
  if (isClosing.value) {
    modalsStore.closeModal("menu");
  }
}

onMounted(() => {
  document.documentElement.style.overflowY = "hidden";
});
onUnmounted(() => {
  document.documentElement.style.overflowY = "auto";
});
</script>
<template>
  <div
    class="header-catalog-menu container"
    :class="{ 'header-catalog-menu_close': isClosing }"
    @animationend="handleAnimationEnd"
  >
    <div class="header-catalog-menu__wraper">
      <div class="header-catalog-menu__wraper-header">
        <NuxtLink class="header-catalog-menu__wraper-header-logo" to="/">
          <span class="header-catalog-menu__wraper-header-logo-title">DV</span>
          <span class="header-catalog-menu__wraper-header-logo-text"
            >Fitness</span
          >
          <BaseDot />
        </NuxtLink>
        <button
          class="header-catalog-menu__wraper-header-burger"
          @click="closeListReviews"
        >
          <Icon
            class="header-catalog-menu__wraper-header-burger-icon"
            :name="HeroIcons.CLOSE"
          />
        </button>
      </div>
      <nav class="header-catalog-menu__wraper-list">
        <a
          v-for="(item, i) in headerLinks"
          :key="i"
          class="header-catalog-menu__wraper-list-item"
        >
          <span class="header-catalog-menu__wraper-list-item-count">{{
            i >= 9 ? i + 1 : "0" + (i + 1)
          }}</span>
          <span
            :link="item.link"
            :name="item.name"
            class-name="header-catalog-menu__wraper-list-item-link"
          >
            {{ item.name }}
          </span>
        </a>
      </nav>
      <BaseButton
        size="lg"
        label="Записаться"
        class="header-catalog-menu__wraper-button"
      />
    </div>
  </div>
</template>
<style lang="scss">
.header-catalog-menu {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background-color: black;
  overflow: hidden;
  z-index: 140;
  transition: all 0.5s ease-in-out;
  animation: open_menu 0.5s linear forwards;
  @include mediaLaptop {
    display: none;
  }

  &_close {
    animation: close_menu 0.5s ease-out forwards;
  }

  &__wraper {
    padding-block: 10px;
    // padding-inline: 12px;
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    // justify-content: space-between;
    &-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      &-logo {
        color: #fff;
        font-size: 24px;
        font-weight: 600;
        &-title {
          text-shadow: 0 0 14px #ffc451;
          margin-right: 5px;
        }
        &-text {
          font-size: 15px;
          text-transform: lowercase;
          font-weight: 500;
          opacity: 0.8;
        }
      }
      &-burger {
        display: flex;
        flex-direction: column;
        justify-content: center;
        &-icon {
          font-size: 36px;
          color: $accent;
          transition: all 0.2s ease-in;
          &:active {
            scale: 0.91;
          }
          @include mediaTablet {
            font-size: 40px;
          }
          @include mediaLaptop {
            display: none;
          }
        }
      }
    }
    &-list {
      flex: 1 1 auto;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      gap: 35px;
      margin-top: 20px;
      padding-inline: 50px;

      &-item {
        font-size: 33px;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 10px;
        color: $white;
        cursor: pointer;
        position: relative;
        transition: all 0.3s ease-in;
        &-count {
          position: absolute;
          top: 2px;
          left: -30px;
          color: $accent;
          font-size: 18px;
        }

        &::before {
          content: "";
          position: absolute;
          left: 0;
          bottom: -5px;
          width: 0;
          height: 2px;
          background-color: $accent;
          transition: width 0.3s ease-in;
        }

        &:hover::before {
          width: 100%;
        }
        &:hover {
          color: $accent;
        }
      }
    }
  }
}

@keyframes open_menu {
  from {
    opacity: 0;
    transform: translateY(-100%);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes close_menu {
  from {
    opacity: 1;
    transform: translateY(0);
  }
  to {
    opacity: 0;
    transform: translateY(-100%);
  }
}
</style>
