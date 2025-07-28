import type { ITokenResponse, IUser } from "~/types";

import { api } from "~/api";

export const useAuthStore = defineStore("auth", () => {
  const user = ref<IUser | null>(null);
  const isLoading = ref<boolean>(false);
  const error = ref<string | null>(null);

  const accessToken = useCookie("access_fitness_token");
  const refreshToken = useCookie("refresh_fitness_token");

  const isAuthenticated = computed(() => !!user.value);
  const currentToken = computed(() => accessToken.value);

  const login = async (email: string, password: string) => {
    isLoading.value = true;
    error.value = null;

    try {
      const { $api } = useNuxtApp();
      const tokens = await $api<ITokenResponse>(api.users.login, {
        method: "POST",
        body: { email, password },
      });

      setTokens(tokens);
      await fetchUser();

      return true;
    } catch (err) {
      error.value = extractError(err);
      return false;
    } finally {
      isLoading.value = false;
    }
  };

  const fetchUser = async () => {
    try {
      const { $api } = useNuxtApp();
      user.value = await $api<IUser>(api.users.me, {
        headers: {
          Authorization: `Bearer ${accessToken.value}`,
        },
      });
    } catch (err) {
      console.error("Ошибка загрузки пользователя", err);
      user.value = null;
      throw err;
    }
  };

  const logout = () => {
    accessToken.value = null;
    refreshToken.value = null;
    user.value = null;
  };

  const setTokens = (tokens: ITokenResponse) => {
    accessToken.value = tokens.access;
    refreshToken.value = tokens.refresh;
  };

  return {
    user,
    isAuthenticated,
    currentToken,
    isLoading,
    error,
    login,
    fetchUser,
    logout,
  };
});
