export enum SocialIcons {
  GITHUB = "mdi:github",
  LINKEDIN = "mdi:linkedin",
  TELEGRAM = "mdi:telegram",
  WHATSAPP = "mdi:whatsapp",
  MAIL = "mdi:email",
  PHONE = "mdi:phone",
  VK = "mdi:vk",
  GOOGLE = "mdi:google",
  YOUTUBE = "mdi:youtube",
  INSTAGRAM = "mdi:instagram",
  FACEBOOK = "mdi:facebook",
  WORK = "mdi:briefcase",
}

// Тип для TypeScript
export type TSocialIcon = keyof typeof SocialIcons;

// Вспомогательная функция
export const getSocialIcon = (icon: TSocialIcon): string => SocialIcons[icon];
