import type { IPagination } from "../common/pagination";

export interface IPost {
  id: number;
  image: string;
  slug: string;
  content: string;
  created_at: Date;
  title: string;
  type: string;
}

export interface IPostsResponse extends IPagination {
  results: IPost[];
}
