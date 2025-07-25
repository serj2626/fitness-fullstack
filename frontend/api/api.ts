export const api = {
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
  coaches: {
    list: "/trainings/trainers/",
    detail: (id: string) => `/trainings/trainers/${id}`,
    reviews: (id: string) => `/trainings/trainers/${id}/reviews/`,
    reviewsCreate: (id: string) => `/trainings/trainers/${id}/reviews/create/`,
  },
  abonements: {
    list: "/abonements/",
  },
  posts: {
    list: "/gym/posts/", //Получает посты
    last: "/gym/posts/last/", //Получает последние посты
    detail: (slug: string) => `/gym/posts/${slug}/`, //Получает детальную информацию о посте
  },
  gym: {
    services: "/gym/services/", //Получает информацию о услугах
    advantages: "/gym/advantages/", //Получает преимущества
    equipment: "/gym/equipments/", //Получает информацию об оборудовании
    faq: "/gym/faq/", //Получает вопросы и ответы
  },
  legal: {
    policy: "/legal/policy/", //Получает политику
    oferta: "/legal/offerta/", //Получает оферту
    aboutcompany: "/legal/about-company/", //Получает информацию о компании
    cookie: "/legal/cookie-policy/", //Получает политику cookie
    services: "/legal/services/", //Получает информацию о услугах
  },
  contacts: {
    list: "/contacts/", //Получает контактную информацию
    feedback: "/contacts/feedback/", //Запрос на создание обратной связи
    footer: "/contacts/footer/", //Запрос на получение данных для футера
  },
  users: {
    login: "/users/login/", //Запрос на авторизацию
    register: "/users/register/", //Запрос на регистрацию
    refresh: "/users/token/refresh/", //Запрос на обновление токена
    verify: "/users/token/verify/", //Запрос на проверку токена
    me: "/users/me/", //Запрос на получение информации о пользователе
  },
  seo: {
    url: (url: string = "") => `/seo/${url}`, //Возвращает сео для конкретной страницы
  },
};
