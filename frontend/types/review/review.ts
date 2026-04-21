import type { IPagination } from "../common/pagination";

export type TOrderingReview =
  | "rating"
  | "-rating"
  | "created_at"
  | "-created_at";
export interface IReview {
  id: string;
  coach: string | null;
  rating: number;
  text: string;
  time_ago: string;
  user: string;
}

export interface ICreateReview {
  user: string;
  coach: string;
  rating: number;
  text: string;
}

export interface IReviewResponse extends IPagination {
  results: IReview[];
}
