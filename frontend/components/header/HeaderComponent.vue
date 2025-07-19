<script lang="ts" setup>
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import { headerLinks } from "~/assets/data/header-links";

const route = useRoute();

const getCurrentRouteName = computed(() => {
  return route.name;
});

const modalsStore = useModalsStore();
const authStore = useAuthStore();

const isHidden = ref<boolean>(false);
const lastScrollY = ref<number>(0);

const handleScroll = () => {
  const currentScroll = window.scrollY;

  if (currentScroll > lastScrollY.value && currentScroll > 80) {
    isHidden.value = true; // скролл вниз – прячем
  } else {
    isHidden.value = false; // скролл вверх – показываем
  }

  lastScrollY.value = currentScroll;
};

const getRoutes = computed(() => {
  return headerLinks.value.filter((item) => {
    if (item.value != "profile") {
      return item;
    } else if (item.value === "profile" && authStore.isAuthenticated) {
      return item;
    }
  });
});

onMounted(() => {
  window.addEventListener("scroll", handleScroll);
});

onUnmounted(() => {
  window.removeEventListener("scroll", handleScroll);
});
</script>
<template>
  <header
    class="header-component"
    :class="{
      'header-component_hidden': isHidden,
      'header-component_opacity': !isHidden && lastScrollY > 0,
    }"
  >
    <div class="container">
      <nav class="header-component__wraper">
        <HeaderLogoComponent />
        <ul class="header-component__wraper-list">
          <NuxtLink
            v-for="item in getRoutes"
            :key="item.name"
            class="header-component__wraper-list-item"
            :class="{
              'header-component__wraper-list-item_active':
                getCurrentRouteName === item.value,
            }"
            :to="item.link"
          >
            {{ item.name }}
          </NuxtLink>
          <a
            v-if="!authStore.isAuthenticated"
            class="header-component__wraper-list-item"
            to="/"
            @click="modalsStore.openModal('login')"
          >
            Войти
          </a>
        </ul>
        <BaseButton
          size="md"
          label="Купить абонемент"
          :outline="true"
          @click="modalsStore.openModal('orderAbonement')"
        />
        <button
          class="header-component__wraper-burger"
          @click="modalsStore.openModal('menu')"
        >
          <Icon
            class="header-component__wraper-burger-icon"
            :name="HeroIcons.BURGER_MENU"
          />
        </button>
      </nav>
    </div>
  </header>
</template>
<style lang="scss">
.header-component {
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  transition: all 0.5s ease-in-out;
  background-color: transparent;
  padding-block: 10px;
  &_opacity {
    // display: none;
    background-color: rgba(0, 0, 0, 0.7);
    @include mediaLaptop {
      display: block;
    }
  }
  &_hidden {
    // display: none;
    transition: transform 0.5s ease-in-out;
    transform: translateY(-100%);
    @include mediaLaptop {
      display: block;
    }
  }
  &__wraper {
    // padding-inline: 12px;
    display: flex;
    align-items: center;
    justify-content: space-between;

    &-list {
      display: none;
      align-items: center;
      gap: 15px;
      @include mediaLaptop {
        display: flex;
        margin-left: auto;
        margin-right: auto;
      }
      @include mediaDesktop {
        gap: 30px;
      }
      &-item {
        font-size: 15px;
        color: $header_link;
        padding-block: 18px;
        transition: color 0.3s ease-in-out;
        @include mediaDesktop {
          font-size: 16px;
        }
        &_active {
          color: $accent;
        }
      }
    }

    &-buy {
      display: none;
      @include mediaLaptop {
        display: block;
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
}
</style>
