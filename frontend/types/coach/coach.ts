
export interface ICoach {
    id:         string;
    first_name: string;
    avatar:     string | null;
    last_name:  string;
    experience: number;
    email:      string;
    phone:      string;
    categories: ICoachCategory[];
    services:   ICoachService[];
}

export interface ICoachCategory {
    id:   number;
    name: string;
    slug: string;
}

export interface ICoachService {
    id:    number;
    title: string;
    price: number | null;
    time:  number;
}