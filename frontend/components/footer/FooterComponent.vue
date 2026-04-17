<script lang="ts" setup>
import { api } from "~/api";
import type { IFooterInfoTransformResponse } from "~/types";

const { $api } = useNuxtApp();

// const { data: footerData } =
//   useNuxtData<IFooterInfoTransformResponse>("footer-info");
export interface IFooterInfo {
  id: number;
  text: string;
  developer_name: string;
  developer_link: string;
  copyright: string;
}

export interface IFooterSocials {
  id: number;
  title: string;
  type: string;
  value: string;
}

const { data: footerData } = useAsyncData<IFooterInfo>("footer-info", () =>
  $api(api.contacts.footer),
);

const { data: socialsData } = useAsyncData<IFooterSocials[]>(
  "footer-socials",
  () => $api(api.contacts.socials),
);
</script>
<template>
  <footer class="footer-component container">
    <div class="footer-component__content">
      <div class="footer-component__content-copyright">
        <span>
          {{ footerData?.text || "DV Fitness" }}
          {{ footerData?.copyright || "© 2025 Все права защищены." }}
        </span>
      </div>
      <!-- <div
        v-if="footerData?.navigations && footerData?.navigations.length"
        class="footer-component__content-links"
      >
        <NuxtLink
          v-for="link in footerData?.navigations"
          :key="link.title"
          class="footer-component__content-links-item"
          :to="link.link"
        >
          {{ link.title }}
        </NuxtLink>
      </div> -->
    </div>
    <!-- {{ socialsData }} -->
    <FooterSocials :values="socialsData || []" />
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
      &-item {
        color: $white;

        &.router-link-active {
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
