<script lang="ts" setup>
import { api } from "~/api";
import type { IFooterResponse } from "~/types";
const { $api } = useNuxtApp();

const { data: footerData } = await useAsyncData<IFooterResponse>(
  "footer-info",
  () => $api(api.contacts.footer)
);

function getIcon(title: string) {
  return `mdi:${title}`;
}
</script>
<template>
  <footer class="footer-component container">
    <div class="footer-component__content">
      <div class="footer-component__content-copyright">
        <span>{{ footerData?.site_name }}{{ footerData?.copyright }}</span>
      </div>
      <div class="footer-component__content-links">
        <NuxtLink
          v-for="link in footerData?.links"
          :key="link.title"
          class="footer-component__content-links-policy"
          :to="link.link"
        >
          {{ link.title }}
        </NuxtLink>
      </div>
    </div>
    <div class="footer-component__social">
      <Icon
        v-for="icon in footerData?.icons"
        :key="icon.title"
        class="footer-component__social-link"
        size="30"
        :name="getIcon(icon.title)"
      />
    </div>
  </footer>
</template>
<style lang="scss" scoped>
.footer-component {
  padding-block: 20px;
  border-top: 1px solid #ffc55178;
  display: flex;
  flex-direction: column;
  gap: 30px;
  color: $white;

  @include mediaTablet {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }

  &__content {
    display: flex;
    flex-direction: column;
    gap: 10px;
    &-copyright {
      font-size: 15px;
      font-weight: 500;
      opacity: 0.8;
    }
    &-links {
      display: flex;
      flex-direction: column;
      gap: 10px;
      font-size: 15px;
      font-weight: 500;
      opacity: 0.8;
      cursor: pointer;

      @include mediaCustom(600px) {
        flex-direction: row;
        align-items: center;
        gap: 20px;
      }

      &-policy,
      &-agreement {
        color: $white;
        transition: all 0.3s ease-in;
        &:hover {
          color: $accent;
        }
      }
    }
  }
  &__social {
    display: flex;
    gap: 10px;
    &-link {
      cursor: pointer;
      transition: all 0.3s ease-in;
      &:hover {
        color: $accent;
      }
    }
  }
}
</style>
