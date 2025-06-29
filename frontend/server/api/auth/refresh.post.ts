import type { ITokenResponse } from "~/types";
import { api } from "~/api";
import { setServerTokens } from "~/server/utils/useSetTokens";

export default defineEventHandler(async (event) => {
  const refresh = getCookie(event, "refresh_token");
  const config = useRuntimeConfig();

  if (!refresh) {
    throw createError({ statusCode: 401, statusMessage: "Не авторизован" });
  }

  try {
    // Запрос к Django для получения новых токенов
    const { access, refresh: newRefresh } = await $fetch<ITokenResponse>(
      `${config.public.api_url}${api.users.refresh}`,
      {
        method: "POST",
        body: { refresh },
      }
    );

    // Обновляем куки
    setServerTokens(event, access, newRefresh);

    return { success: true };
  } catch (error) {
    if (error instanceof Error) {
      throw createError({
        statusCode: 401,
        statusMessage: error.message,
      });
    } else {
      throw createError({
        statusCode: 401,
        statusMessage: "Неизвестная ошибка",
      });
    }
  }
});
