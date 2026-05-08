// stores/auth.ts
import type { IUser } from "~/types";
import { api } from "~/api";

export const useAuthStore = defineStore("auth", () => {
  const user = ref<IUser | null>(null);
  const isLoading = ref(false);
  const error = ref<string | null>(null);

  const isAuthenticated = computed(() => !!user.value);

  const register = async (payload: {
    email: string;
    password: string;
    first_name?: string;
    last_name?: string;
    phone?: string;
  }) => {
    isLoading.value = true;
    error.value = null;

    try {
      const { $api } = useNuxtApp();
      // 🔥 $api сам отправит credentials: 'include' и CSRF
      user.value = await $api(api.users.register, {
        method: "POST",
        body: payload,
      });
      return true;
    } catch (err: any) {
      error.value = err.message || "Ошибка регистрации";
      return false;
    } finally {
      isLoading.value = false;
    }
  };

  // 🔐 ЛОГИН
  const login = async (email: string, password: string) => {
    isLoading.value = true;
    error.value = null;

    try {
      const { $api } = useNuxtApp();
      user.value = await $api(api.users.login, {
        method: "POST",
        body: { email, password },
      });
      return true;
    } catch (err: any) {
      error.value = err.message || "Неверные данные";
      return false;
    } finally {
      isLoading.value = false;
    }
  };

  const fetchUser = async () => {
    try {
      const { $api } = useNuxtApp();
      user.value = await $api(api.users.me, {
        method: "GET",
        // 🔥 credentials: 'include' уже в $api, не нужно дублировать
      });
      return true;
    } catch (err) {
      console.error("Ошибка загрузки пользователя", err);
      user.value = null;
      return false;
    }
  };

  const logout = async () => {
    try {
      const { $api } = useNuxtApp();
      await $api(api.users.logout, { method: "POST" });
    } catch (err) {
      console.error("Ошибка при логауте", err);
    } finally {
      user.value = null; // 🔥 очищаем стор, сессию удалил бэк
    }
  };

  // 🔥 Инициализация: проверяем сессию при загрузке приложения
  const init = async () => {
    await fetchUser();
  };

  return {
    user,
    isAuthenticated,
    isLoading,
    error,
    register,
    login,
    logout,
    fetchUser,
    init, // 🔥 вызови в app.vue или плагине
  };
});
