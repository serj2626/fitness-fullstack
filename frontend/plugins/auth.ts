import type { ITokenResponse } from "~/types";
import { api } from "~/api";

export default defineNuxtPlugin(() => {
  console.log("auth", useNuxtApp());
  const { $api } = useNuxtApp();
  const auth = {
    // Сохраняем токены в куки
    async setTokens(access: string, refresh: string) {
      const accessExpires = new Date(Date.now() + 5 * 60 * 1000);
      const refreshExpires = new Date(Date.now() + 1 * 24 * 60 * 60 * 1000);

      useCookie("access_token", {
        httpOnly: true,
        secure: true,
        expires: accessExpires,
        sameSite: "strict",
      }).value = access;

      useCookie("refresh_token", {
        httpOnly: true,
        secure: true,
        expires: refreshExpires,
        sameSite: "strict",
      }).value = refresh;
    },

    // Получаем access токен
    getAccessToken(): string | null {
      return useCookie("access_token").value || null;
    },

    // Обновляем токены
    async refreshTokens() {
      const refreshToken = useCookie("refresh_token").value;
      if (!refreshToken) return null;

      try {
        const { access, refresh } = await $api<ITokenResponse>(
          api.users.refresh,
          {
            method: "POST",
            body: { refresh: refreshToken },
          }
        );
        this.setTokens(access, refresh);
        return access;
      } catch (error) {
        if (error instanceof Error) {
          console.error(error.message);
        } else {
          console.error("Неизвестная ошибка", error);
        }

        this.logout();
        return null;
      }
    },

    // Выход
    logout() {
      useCookie("access_token").value = null;
      useCookie("refresh_token").value = null;
      navigateTo("/login");
    },
  };

  // Инъекция в контекст Nuxt
  return {
    provide: { auth },
  };
});
