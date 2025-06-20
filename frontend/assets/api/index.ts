export const api = {
    headers: {
      'Content-Type': 'application/json',
      Accept: 'application/json',
    },
    pages: {
      specialists: '/pages/specialists/', //Возвращает информацию для страницы специалистов
      portfolio: '/pages/portfolio/', //Возвращает информацию для страницы работ
      services: '/pages/services/', //Возвращает информацию для страницы услуг
      faq: '/pages/faq/', //Возвращает информацию для страницы Вопросов/Ответов
      prices: '/pages/prices/', //Возвращает информацию для страницы цен
      reviews: '/pages/reviews/', //Возвращает информацию для страницы отзывов
      about: '/pages/about/', //Возвращает информацию для страницы О нас
      main: '/pages/main/', //Возвращает информацию для главной страницы
      contacts: '/pages/contacts/', //Возвращает информацию для страницы Контактов
      oferta: '/pages/oferta/', //Возвращает информацию для страницы Оферты
      policy: '/pages/policy/', //Возвращает информацию для политики конфиденциальности
      healthQuestionnaire: '/pages/health-questionnaire', //Возвращает информацию для страницы Анкеты здоровья
    },
    specialists: {
      list: '/specialists/', //Возвращает всех специалистов
      dropdown: '/specialists/dropdown/', //Список всех специалистов для дропдаунов
      item: (slug: string): string => `/specialists/${slug}`, // Получить конкретный специалиста по слагу
    },
    portfolio: {
      list: '/portfolio/', //Возвращает все примеры работ по фильтрам
      filter: '/portfolio/filter/', //Возвращает фильтр для работ по услугам
      item: (slug: string): string => `/portfolio/${slug}`, //Возвращает пример работы по слагу
    },
    services: {
      list: '/services/', //Возвращает все услуги
      prices: '/services/prices/', //Возвращает цены на услуги
      tech: '/services/technologies/', //Возвращает все технологии и образование
      item: (slug: string): string => `/services/${slug}`, //Возвращает список под услуг для выбранногй услуги по слагу родительской услуги
      subService: (service_slug: string, sub_service_slug: string) => `/services/${service_slug}/${sub_service_slug}`, //Возвращает под услугу по слагу услуги по под услуги
      dropdown: '/services/dropdown/', //Возвращает список подуслуг
    },
    reviews: {
      list: '/specialists/reviews/' //Возвращает пагинорованный список отзывов
    },
    faq: {
      list: '/faq/', //Возвращает список вопросов/ответов
    },
    site: {
      contacts: '/site/contacts/', //Возвращает контактную информацию
    },
    feedback: {
      callback: '/feedback/callback/', //Запрос на создание обратного звонка
      review: '/feedback/review/', //Запрос на создание отзыва
      healthQuestionnaire: '/feedback/feedback/health-questionnaire/', //Представление для отправки формы анкеты здоровья
    },
    seo: {
      url: (url: string = "") => `/seo/${url}` //Возвращает сео для конкретной страницы
    }
  };
  