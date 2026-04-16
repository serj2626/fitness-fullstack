export interface IAbonement {
  id: number;
  name: string;
  slug: string;
  content: string;
  count_months: number;
  days_freezing: number;
  price: number;
  services: string[];
}
