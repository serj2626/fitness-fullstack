import type { IPagination } from "../common/pagination";

export interface IPost {
  id: number;
  content: string;
  title: string;
  created_at: string;
  updated_at: string;
  slug: string;
  category: string;
  image: string | null;
  is_published: true;
}

export interface IPostsResponse extends IPagination {
  results: IPost[];
}
