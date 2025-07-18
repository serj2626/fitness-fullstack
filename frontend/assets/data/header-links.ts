export const headerLinks = ref<{ name: string; link: string; value: string }[]>(
  [
    {
      name: "Главная",
      link: "/",
      value: "index",
    },
    {
      name: "Тренеры",
      link: "/coaches",
      value: "coaches",
    },
    {
      name: "Расписание",
      link: "/schedule",
      value: "schedule",
    },
    {
      name: "Контакты",
      link: "/contacts",
      value: "contacts",
    },
    {
      name: "Мой профиль",
      link: "/profile",
      value: "profile",
    },
  ]
);
