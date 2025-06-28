import type { ITokenResponse } from "~/types";
import { api } from "~/api";

export default defineEventHandler(async (event) => {
  const refresh = getCookie(event, "refresh_token");

  if (!refresh) {
    throw createError({ statusCode: 401, statusMessage: "No refresh token" });
  }

  try {
    // Запрос к Django для получения новых токенов
    const { access, refresh: newRefresh } = await $fetch<ITokenResponse>(
      api.users.refresh,
      {
        method: "POST",
        body: { refresh },
      }
    );

    // Обновляем куки
    setCookie(event, "access_token", access, {
      httpOnly: true,
      secure: true,
      sameSite: "strict",
      maxAge: 60 * 5,
    });

    setCookie(event, "refresh_token", newRefresh, {
      httpOnly: true,
      secure: true,
      sameSite: "strict",
      maxAge: 60 * 60 * 24 * 7,
    });

    return { success: true };
  } catch (error) {
    throw createError({
      statusCode: 401,
      statusMessage: "Invalid refresh token",
    });
  }
});
