import { api } from "~/api";
import type {
  IContactsFooterInfo,
  IContactsList,
  IContactsSocials,
} from "~/types";

type ContactsType =
  | "address"
  | "email"
  | "phone"
  | "mode"
  | "map"
  | "longitude";

// Для SOCIALS_TYPE
type SocialsType = "vk" | "tg" | "max" | "insta" | "youtube";

function parseContacts(data: IContactsList[]): Partial<Record<ContactsType, string | string[]>> {
  const res: Record<string, string | string[]> = {};
  data.forEach((item: IContactsList) => {
    // Предполагаем, что у item есть поля type и value
    const key = item.type === "other_phone" ? "phone" : item.type;
    const value = item.value; // или само item, если это строка
    if (key === "phone") {
      if (!res[key]) {
        res[key] = [value];
      } else {
        (res[key] as string[]).push(value);
      }
    } else {
      if (!res[key]) {
        res[key] = value;
      }
    }
  });
  return res;
}
// stores/contacts.ts
export const useContactsStore = defineStore("contacts", () => {
  const footerInfo = ref<IContactsFooterInfo | null>(null);
  const socials = ref<IContactsSocials | null>(null);
  const contactsList = ref<Record<string, string[] | string> | null>(null);
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
