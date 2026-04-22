export const api = {
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
  coaches: {
    list: "/coaches/", //Получает список тренеров
    last: "/coaches/last/", //Получает последних тренеров
    order: "/coaches/order/", //Запрос на бронирование тренировки
    detail: (id: string) => `/coaches/${id}`, //Получает детальную информацию о тренере
  },
  categories: {
    list: "/categories/", //Получает список категорий
  },
  abonements: {
    list: "/abonements/", //Получает список абонементов
    order: "/abonements/order/", //Запрос на бронирование абонемента
  },
  posts: {
    list: "/posts/", //Получает посты
    last: "/posts/last/", //Получает последние посты
    detail: (slug: string) => `/posts/${slug}/`, //Получает детальную информацию о посте
  },
  contacts: {
    list: "/contacts/", //Получает контактную информацию
    feedback: "/contacts/feedback/", //Запрос на создание обратной связи
    footer: "/contacts/footer/", //Запрос на получение данных для футера
    faq: "/contacts/faq-list/", //Получает вопросы и ответы
    policy: "/contacts/policy/", //Получает политику конфиденциальности
    socials: "/contacts/socials/", //Получает социальные сети
    terms: "/contacts/terms/", //Получает пользовательское соглашение
    vacancies: "/contacts/vacancies/", //Получает вакансии
  },
  reviews: {
    list: "/coaches/reviews/", //Получает список отзывов
    create: "/coaches/reviews/create/", //Запрос на создание отзыва
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
