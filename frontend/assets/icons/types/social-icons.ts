export enum SocialIcons {
  GITHUB = "fa6-brands:github",
  LINKEDIN = "mdi:linkedin",
  TELEGRAM = "fa6-brands:telegram",
  WHATSAPP = "fa6-brands:whatsapp",
  MAIL = "fa6-solid:envelope",
  PHONE = "fa6-solid:phone",
  VK = "fa6-brands:vk",
  GOOGLE = "fa6-brands:google",
  YANDEX = "fa6-brands:yandex",
  USER = "fa6-solid:user",
  WORK = "fa6-solid:building",
  VK_RI = "ri:vk-fill",
  TG_RI = "ri:telegram-fill",
  WHATSAPP_RI = "ri:whatsapp-fill",
  GITHUB_RI = "ri:github-fill",
  MAIL_RI = "ri:mail-fill",
  PHONE_RI = "ri:phone-fill",
}

// Тип для TypeScript
export type SocialIcon = keyof typeof SocialIcons;

// Вспомогательная функция
export const getSocialIcon = (icon: SocialIcon): string => SocialIcons[icon];
