export const api = {
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
  coaches: {
    list: "/trainings/trainers/",
    detail: (id: string) => `/trainings/trainers/${id}`,
  },
  abonements: {
    list: "/abonements/",
  },
  legal: {
    policy: "/legal/policy/", //Получает политику
    oferta: "/legal/offerta/", //Получает оферту
    aboutcompany: "/legal/about-company/", //Получает информацию о компании
    cookiepolicy: "/legal/cookie-policy/", //Получает политику cookie
    services: "/legal/services/", //Получает информацию о услугах
  },
  contacts: {
    contacts: "/contacts/", //Получает контактную информацию
    feedback: "/contacts/feedback/", //Запрос на создание обратной связи
    footer: "/contacts/footer/", //Запрос на получение данных для футера
  },
  seo: {
    url: (url: string = "") => `/seo/${url}`, //Возвращает сео для конкретной страницы
  },
};
