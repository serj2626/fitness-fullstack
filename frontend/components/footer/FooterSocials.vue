<script setup lang="ts">
import { SocialIcons } from "~/assets/icons/types/social-icons";
const {
  tg = "",
  whatsapp = "",
  mail = "",
  phone = "",
} = defineProps<{
  tg?: string;
  whatsapp?: string;
  mail?: string;
  phone?: string;
}>();
</script>
<template>
  <div class="footer-socials">
    <a :href="tg" class="footer-socials__link" title="telegram">
      <Icon :name="SocialIcons.TELEGRAM" class="footer-socials__link-icon" />
    </a>
    <a :href="whatsapp" class="footer-socials__link" title="whatsapp">
      <Icon :name="SocialIcons.WHATSAPP" class="footer-socials__link-icon" />
    </a>
    <a :href="`mailto:${mail}`" class="footer-socials__link" title="почта">
      <Icon :name="SocialIcons.MAIL" class="footer-socials__link-icon" />
    </a>
    <a :href="`phone:${phone}`" class="footer-socials__link" title="телефон">
      <Icon :name="SocialIcons.PHONE" class="footer-socials__link-icon" />
    </a>
  </div>
</template>
<style scoped lang="scss">
.footer-socials {
  display: flex;
  align-items: center;
  gap: 5px;

  &__link {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 44px;
    height: 44px;
    border-radius: 50%;
    background-color: transparent;
    color: #fff;
    transition: all 0.3s ease;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.25);

    &:hover {
      transform: translateY(-3px) scale(1.05);
      box-shadow: 0 6px 14px rgba(0, 0, 0, 0.35);

      .footer-socials__link-icon {
        color: $accent;
      }
    }

    // разные цвета для соцсетей
    &-icon {
      pointer-events: none;
      font-size: 22px;
    }

    // &[href*="t.me"] {
    //   background: #229ed9; // telegram
    //   &:hover {
    //     box-shadow: 0 6px 14px rgba(34, 158, 217, 0.5);
    //   }
    // }

    // &[href*="wa.me"],
    // &[href*="whatsapp"] {
    //   background: #25d366; // whatsapp
    //   &:hover {
    //     box-shadow: 0 6px 14px rgba(37, 211, 102, 0.5);
    //   }
    // }

    // &[href*="mailto"] {
    //   background: #ea4335; // gmail-style red
    //   &:hover {
    //     box-shadow: 0 6px 14px rgba(234, 67, 53, 0.5);
    //   }
    // }
  }
}
</style>
