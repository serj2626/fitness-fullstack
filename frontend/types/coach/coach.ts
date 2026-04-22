import type { IPagination } from "../common/pagination";

export interface ICoachesListResponse extends IPagination {
  results: ICoach[];
}

export interface ICoach {
  id: string;
  first_name: string;
  avatar: string | null;
  last_name: string;
  experience?: number | null;
  email?: string;
  phone?: string;
  categories: ICoachCategory[];
  services?: ICoachService[];
  socials?: ICoachSocial[];
}

export interface ICoachCategory {
  id: number;
  name: string;
  slug: string;
}

export interface ICoachService {
  id: number;
  title: string;
  price: number | null;
  time: number;
}

export interface ICoachSocial {
  id: number;
  title: string;
  social: string;
  link: string;
}
