export interface ICoach {
  id: string;
  first_name: string;
  avatar: string;
  last_name: string;
  experience: number;
  email: string;
  phone: string;
  categories: ICategory[];
  services: IService[];
}

export interface ICategory {
  id: number;
  name: string;
  slug: string;
}

export interface IService {
  id: number;
  title: string;
  price: number | null;
  time: number;
}
