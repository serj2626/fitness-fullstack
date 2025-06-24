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
