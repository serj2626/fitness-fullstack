export interface ICoach {
  id: string;
  content: string;
  position: string;
  first_name: string;
  last_name: string;
  email: string;
  phone: string;
  keywords: null;
  experience: number;
  avatar: string;
}

export interface ICoachesListResponse {
  current: number;
  next: number | null;
  previous: number | null;
  count: number;
  results: ICoach[];
}

// ДЛЯ ФУТЕРА

interface IFooterResponse {
  site_name: string;
  copyright: string;
  links: {
    title: "string";
    link: "string";
  }[];
  icons: {
    title: "vk";
    link: "string";
  }[];
}

interface IServiceAbonemnet {
  title: string;
}

export interface IMainAbonementAPIResponse {
  id: number;
  title: string;
  services: IServiceAbonemnet[];
  description: string;
  price: number;
  number_of_months: number;
  is_popular: boolean;
  slug: string;
}

export interface IMainAbonementResponse {
  id: number;
  title: string;
  services: string[];
  description: string;
  price: number;
  number_of_months: number;
  is_popular: boolean;
  slug: string;
}

export interface IServicesResponse {
  id: string;
  alt: string;
  type: string;
  slug: string;
  avatar: string;
  img_url: string;
}

// СТРАНИЦА КОНТАКТОВ

type ContactType = "phone" | "mail" | "address" | "latitude" | "longitude";

export interface IContactData<T extends ContactType = ContactType> {
  type: T;
  second_type: string;
  value: string;
}

export interface IContactsResponse {
  [key: string]: IContactData;
}

// СТРАНИЦА ТРЕНЕРА ДЕТАЛЬНАЯ

interface TrainerImage {
  id: string;
  image: string; // URL изображения
}

interface TrainingRate {
  id: number;
  title: string; // Название тарифа
  count_minutes: number; // Продолжительность в минутах
  price: number; // Цена (лучше использовать number вместо bigint)
  description: string; // Описание тарифа
}

interface TrainerReview {
  name: string; // Имя автора отзыва
  email: string; // Email автора
  rating: number; // Оценка (1-5)
  text: string; // Текст отзыва
  verified: boolean; // Подтвержденный отзыв
  time_age: string; // Время создания (лучше использовать Date или string в ISO формате)
}

export interface ITrainerSocial {
  type: string;
  link: string;
}
export interface ITrainerResponse {
  id: string;
  images: TrainerImage[];
  position: string;
  rates: TrainingRate[];
  average_rating: string;
  reviews: TrainerReview[];
  socials: ITrainerSocial[];
  photo: string;
  content: string;
  first_name: string;
  last_name: string;
  email: string;
  phone: string;
  keywords: string;
  experience: number;
  avatar: string;
  education: string;
}

// СТРАНИЦА ВОПРОСЫ-ОТВЕТЫ

export interface IQuestion {
  id: number;
  question: string;
  answer: string;
}
export interface IFAQResponse {
  current: number;
  next: null | number;
  previous: null | number;
  count: number;
  results: IQuestion[];
}

// СТРАНИЦЫ С ЮРИДИЧЕСКИМИ ДОКУМЕНТАМИ
export interface ILegalResponse {
  title: string;
  content: string;
}

// СТРАНИЦЫ С ПОСТАМИ

export interface IPost {
  id: number;
  content: string;
  title: string;
  created_at: string;
  updated_at: string;
  slug: string;
  category: string;
  image: string;
  is_published: true;
}

export interface IPostsResponse {
  current: number;
  next: null | number;
  previous: null | number;
  count: number;
  results: IPost[];
}

// ТОКЕНЫ
export interface ITokenResponse {
  access: string;
  refresh: string;
}

interface IUser {
  id: string;
  email: string;
  phone: string;
}
