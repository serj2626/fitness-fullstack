type ContactType = "phone" | "mail" | "IAddress" | "latitude" | "longitude";

export interface IContactData<T extends ContactType = ContactType> {
  type: T;
  second_type: string;
  value: string;
}
export interface IContactsResponse {
  [key: string]: IContactData;
}

export interface IContact {
  type: string;
  type_display: string;
  value: string;
}

export interface INavigation {
  title: string;
  link: string;
}

export interface IFooterInfo {
  site_name: string;
  subtitle: string;
  copyright: string;
  developer_name: string;
  developer_link: string;
  navigations: INavigation[];
  contacts: IContact[];
}

export interface IFooterInfoTransformResponse {
  site_name: string;
  subtitle: string;
  copyright: string;
  developer_name: string;
  developer_link: string;
  navigations: INavigation[];
  phone: IContact;
  mail: IContact;
  tg: IContact;
  whatsapp: IContact;
  address: IContact;
  mode: IContact;
  latitude: IContact;
  longitude: IContact;
}
