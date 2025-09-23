import type { IPagination } from "../common/pagination";

export interface IQuestion {
  id: number;
  question: string;
  answer: string;
}
export interface IFAQResponse extends IPagination {
  results: IQuestion[];
}
