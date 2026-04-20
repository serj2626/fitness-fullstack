import type { IPagination } from "../common/pagination";
export interface IReview {
  id: string;
  coach: string | null;
  rating: number;
  text: string;
  time_ago: string;
  user: string;
}

export interface IReviewResponse {
  data: IReview[];
  pagination: IPagination;
}
