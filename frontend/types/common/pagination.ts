export interface IPagination {
  current: number;
  next: number | null;
  previous: number | null;
  count: number;
  total_pages: number;
}