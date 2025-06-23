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
