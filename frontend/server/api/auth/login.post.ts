import type { ITokenResponse } from "~/types";
import { api } from "~/api";

export default defineEventHandler(async (event) => {
  const body = await readBody(event);

  // Запрос к Django
  const response: ITokenResponse = await $fetch(
    api.users.login,
    {
      method: "POST",
      body,
    }
  );

  // Установка токенов на сервере
  setCookie(event, "access_token", response.access, {
    httpOnly: true,
    secure: true,
    sameSite: "strict",
    maxAge: 60 * 5,
  });

  setCookie(event, "refresh_token", response.refresh, {
    httpOnly: true,
    secure: true,
    sameSite: "strict",
    maxAge: 60 * 60 * 24 * 7,
  });

  return { success: true };
});
