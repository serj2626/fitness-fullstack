import type { IUser } from "~/types";

export const useAuthStore = defineStore("auth", () => {
  const user = ref<IUser | null>(null);
  const isLoading = ref(false);
  const error = ref<string | null>(null);

  const isAuthenticated = computed(() => !!user.value);

  const login = async (credentials: { email: string; password: string }) => {
    isLoading.value = true;
    error.value = null;

    try {
      await $fetch("/api/auth/login", {
        method: "POST",
        body: credentials,
      });

      await fetchUser();
      return true;
    } catch (err: any) {
      error.value = extractError(err);
      return false;
    } finally {
      isLoading.value = false;
    }
  };

  const fetchUser = async () => {
    try {
      const { $api } = useNuxtApp();
      user.value = await $api<IUser>("/users/me/");
    } catch (err) {
      console.error("Ошибка загрузки пользователя", err);
      user.value = null;
    }
  };

  const logout = async () => {
    useCookie("access_token").value = null;
    useCookie("refresh_token").value = null;
    user.value = null;
    // await navigateTo("/login");
  };

  function extractError(err: any): string {
    if (err?.data?.detail) return err.data.detail;
    if (err?.message) return err.message;
    return "Неизвестная ошибка";
  }

  return {
    user,
    isAuthenticated,
    isLoading,
    error,
    login,
    fetchUser,
    logout,
  };
});
