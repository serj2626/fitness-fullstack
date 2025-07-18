import type { ITokenResponse, IUser } from "~/types";

import { api } from "~/api";

export const useAuthStore = defineStore("auth", () => {
  const user = ref<IUser | null>(null);
  const isLoading = ref(false);
  const error = ref<string | null>(null);

  const token = reactive<ITokenResponse>({
    access: "",
    refresh: "",
  });

  const isAuthenticated = computed(() => !!user.value);
  const isGetToken = computed(() => !!token.access);

  const login = async (email: string, password: string) => {
    const { $api } = useNuxtApp();
    isLoading.value = true;
    error.value = null;

    try {
      const res: ITokenResponse = await $api(api.users.login, {
        method: "POST",
        body: { email, password },
      });

      token.access = res.access;
      token.refresh = res.refresh;
      useCookie("access_token").value = res.access;
      useCookie("refresh_token").value = res.refresh;

      // await fetchUser();
      return true;
    } catch (err) {
      error.value = extractError(err);
      return false;
    } finally {
      isLoading.value = false;
    }
  };

  const refreshToken = async () => {
    try {
      const { $api } = useNuxtApp();
      const res: ITokenResponse = await $api(api.users.refresh, {
        method: "POST",
        body: { refresh: token.refresh },
      });
      token.access = res.access;
      token.refresh = res.refresh;
      useCookie("access_token").value = res.access;
      useCookie("refresh_token").value = res.refresh;
      return true;
    } catch (err) {
      error.value = extractError(err);
      return false;
    }
  };

  const fetchUser = async () => {
    try {
      const { $api } = useNuxtApp();
      user.value = await $api<IUser>(api.users.me, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${useCookie("access_token").value}`,
        },
      });
    } catch (err) {
      console.error("Ошибка загрузки пользователя", err);
      user.value = null;
    }
  };

  const logout = async () => {
    useCookie("access_token").value = null;
    useCookie("refresh_token").value = null;
    user.value = null;
  };

  function extractError(err: unknown): string {
    if (err instanceof Error && err?.message) return err.message;
    return "Неизвестная ошибка";
  }

  return {
    user,
    isAuthenticated,
    isLoading,
    error,
    login,
    // fetchUser,
    logout,
  };
});
