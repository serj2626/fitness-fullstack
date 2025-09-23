import type { IPagination } from "../common/pagination";
import type { IReview } from "../review/review";

export interface ICoach {
  id: string;
  content?: string;
  position: string;
  first_name: string;
  last_name: string;
  email?: string;
  phone?: string;
  keywords?: null;
  experience: number;
  avatar: string;
  education?: string;
  socials?: { type: string; link: string }[];
}

export interface ICoachesListResponse extends IPagination {
  results: ICoach[];
}

export interface ICoachImage {
  id: string;
  image: string;
}

export interface ICoachRate {
  id: number;
  title: string;
  count_minutes: number;
  price: number;
  description?: string;
}

export interface ICoachSocial {
  type: string;
  link: string;
}

export interface CoachResponse {
  id: string;
  images: ICoachImage[];
  position: string;
  rates: ICoachRate[];
  average_rating: string;
  reviews: IReview[];
  socials: ICoachSocial[];
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
