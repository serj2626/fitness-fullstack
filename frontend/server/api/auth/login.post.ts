import type { ITokenResponse } from "~/types";
import { api } from "~/api";
import { setServerTokens } from "~/server/composables/useSetTokens";

export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig();
  const body = await readBody(event);

  // Запрос к Django
  const response: ITokenResponse = await $fetch(
    `${config.public.api_url}${api.users.login}`,
    {
      method: "POST",
      body,
    }
  );

  // Установка токенов на сервере
  setServerTokens(event, response.access, response.refresh);
  return { success: true };
});
