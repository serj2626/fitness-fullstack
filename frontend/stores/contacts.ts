import { api } from "~/api";
import type {
  IContactsFooterInfo,
  IContactsList,
  IContactsSocials,
} from "~/types";

type ContactsType = 
  | "city" 
  | "address" 
  | "email" 
  | "phone" 
  | "other_phone" 
  | "mode" 
  | "map" 
  | "longitude";

// Для SOCIALS_TYPE
type SocialsType = 
  | "vk" 
  | "tg" 
  | "max" 
  | "insta" 
  | "youtube";

function parseContacts(data: IContactsList[]) {
  const res: Record<string,  string[]> = {};
  data.forEach((item: IContactsList) => {
    if (res[item.type]) {
      res[item.type].push(item.value);
    }
    res[item.type] = [item.value];
  });

  return res;
}

// stores/contacts.ts
export const useContactsStore = defineStore("contacts", () => {
  const footerInfo = ref<IContactsFooterInfo | null>(null);
  const socials = ref<IContactsSocials | null>(null);
  const contactsList = ref<Record<string, string[]> | null>(null);
  const loaded = ref(false);

  async function loadAll(force = false) {
    if (loaded.value && !force) return;
    const { $api } = useNuxtApp();
    const [footer, soc, contacts] = await Promise.all([
      $api<IContactsFooterInfo>(api.contacts.footer),
      $api<IContactsSocials>(api.contacts.socials),
      $api<IContactsList[]>(api.contacts.list),
    ]);
    footerInfo.value = footer;
    socials.value = soc;
    contactsList.value = parseContacts(contacts);
    loaded.value = true;
  }

  return { footerInfo, socials, contactsList, loaded, loadAll };
});
