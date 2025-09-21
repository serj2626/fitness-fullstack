<script lang="ts" setup>
import type { IFooterInfoTransformResponse } from "~/types";

const { data: footerData } =
  useNuxtData<IFooterInfoTransformResponse>("footer-info");
</script>
<template>
  <footer class="footer-component container">
    <div class="footer-component__content">
      <div class="footer-component__content-copyright">
        <span>
          {{ footerData?.site_name || "DV Fitness" }}
          {{ footerData?.copyright || "© 2025 Все права защищены." }}
        </span>
      </div>
      <div
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
      </div>
    </div>
    <FooterSocials
      :tg="footerData?.tg?.value"
      :whatsapp="footerData?.whatsapp.value"
      :mail="footerData?.mail.value"
      :phone="footerData?.phone.value"
    />
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
