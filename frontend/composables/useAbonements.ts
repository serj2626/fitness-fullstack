import type { IMainAbonementAPIResponse } from "~/types";
import { api } from "~/api";

export const useAbonements = () => {
  const { $api } = useNuxtApp();
  return useAsyncData(
    "main-page-abonements-list-info",
    () => $api<IMainAbonementAPIResponse[]>(api.abonements.list),
    {
      // transform: (data) => {
      //   return data.map((abonement) => {
      //     return {
      //       ...abonement,
      //       services: abonement.services.map((service) => service.title),
      //     };
      //   });
      // },
      getCachedData: (key) => {
        const cached = useNuxtData(key).data.value;
        return cached || undefined;
      },
    }
  );
};
