import { api } from "~/api"
import type { IContactsFooterInfo, IContactsList, IContactsSocials } from "~/types"

// stores/contacts.ts
export const useContactsStore = defineStore('contacts', () => {
  const footerInfo = ref<IContactsFooterInfo | null>(null)
  const socials = ref<IContactsSocials | null>(null)
  const contactsList = ref<IContactsList | null>(null)
  const loaded = ref(false)

  async function loadAll(force = false) {
    if (loaded.value && !force) return
    const { $api } = useNuxtApp()
    const [footer, soc, contacts] = await Promise.all([
      $api<IContactsFooterInfo>(api.contacts.footer),
      $api<IContactsSocials>(api.contacts.socials),
      $api<IContactsList>(api.contacts.list),
    ])
    footerInfo.value = footer
    socials.value = soc
    contactsList.value = contacts
    loaded.value = true
  }

  return { footerInfo, socials, contactsList, loaded, loadAll }
})