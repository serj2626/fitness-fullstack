export enum HeroIcons {
  ARROW_UP = "heroicons:arrow-up",
  ARROW_RIGHT = "heroicons:arrow-right-solid",
  BURGER_MENU = "heroicons:bars-3",
  CHAT = "heroicons:chat-bubble-left-ellipsis",
  CHECK = "heroicons:check",
  CLOCK = "heroicons:clock",
  CLOSE = "heroicons:x-mark",
  COMPANY = "heroicons:building-office-2",
  DOWN = "heroicons:chevron-down",
  EYE = "heroicons:eye",
  EYE_CLOSE = "heroicons:eye-slash",
  FILE = "heroicons:document",
  HAND = "heroicons:hand-thumb-up",
  HOME = "heroicons:home",
  MAIL = "heroicons:envelope",
  MARKER = "heroicons:map-pin",
  PASSWORD = "heroicons:lock-closed",
  PAUSE = "heroicons:pause",
  PLUS = "heroicons:plus",
  SEARCH = "heroicons:magnifying-glass",
  SEND = "heroicons:paper-airplane",
  START = "heroicons:play",
  UP = "heroicons:chevron-up",
  USER = "heroicons:user",
  STAR = "heroicons:star",
  CHEVRON_RIGHT = "heroicons:chevron-right-solid",
  CHEVRON_LEFT = "heroicons:chevron-left-solid",
}

// Тип для TypeScript
export type AppIcon = keyof typeof HeroIcons;

// Вспомогательная функция для получения иконки
export const getIcon = (icon: AppIcon) => HeroIcons[icon];
