export interface IContactsList {
  id: number;
  title: string;
  type: string;
  value: string;
}

export interface IContactsFooterInfo {
  id: number;
  text: string;
  developer_name: string;
  developer_link: string;
  copyright: string;
}

export interface IContactsSocials {
  id: number;
  title: string;
  type: string;
  value: string;
}


export interface IVacancy {
  id: number;
  title: string;
  slug: string;
  content: string;
  description: string;
  time: string;
  created_at: Date;
  salary?: string;
  location?: string;
}
