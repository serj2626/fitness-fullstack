export interface IAbonementResponse {
  id: number;
  services: string[];
  title: string;
  description: string;
  price: number;
  number_of_months: number;
  is_popular: boolean;
  sale: boolean;
  freeze_days: number;
  slug: string;
}