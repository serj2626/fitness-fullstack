import type { ITokenResponse } from "~/types";
import { api } from "~/api";

export const useVerifyToken = async (token: string) => {
  const { $api } = useNuxtApp();
  try {
    const { success } = await $api<{ success: boolean }>(api.users.verify, {
      method: "POST",
      body: { token },
    });
    return success;
  } catch (error) {
    console.error("Token verification failed:", error);
    return false;
  }
};

export const useRefreshToken = async () => {
  const { $api } = useNuxtApp();
  const refreshToken = useCookie("refresh_token").value;

  try {
    const res = await $api<ITokenResponse>(api.users.refresh, {
      method: "POST",
      body: { refresh: refreshToken },
    });
    const accessCookie = useCookie("access_fitness_token", { maxAge: 5 * 60 }); // 5 минут
    const refreshCookie = useCookie("refresh_fitness_token", {
      maxAge: 60 * 60 * 24,
    }); // 1 день

    accessCookie.value = res.access;
    refreshCookie.value = res.refresh;

    return true;
  } catch (error) {
    console.error("Token refresh failed:", error);
    return false;
  }
};
