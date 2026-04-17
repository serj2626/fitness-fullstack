import type { IPagination } from "../common/pagination";

export interface IPost {
  id: number;
  title: string;
  slug: string;
  type: string;
  image: null;
  created_at: Date;
}


export interface IPostsResponse extends IPagination {
  results: IPost[];
}
