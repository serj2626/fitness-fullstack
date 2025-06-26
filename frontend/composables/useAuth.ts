import type { ITokenResponse } from "~/types";
import { api } from "~/api";

export const useAuth = () => {
  const { $auth , $api } = useNuxtApp();
  const user = useState("user", () => null);

  // Логин
  const login = async (credentials: { email: string; password: string }) => {
    try {
      const { access, refresh } = await $api<ITokenResponse>(
       api.users.login,
        {
          method: "POST",
          body: credentials,
        }
      );

      $auth.setTokens(access, refresh);
      await fetchUser(); // Загружаем данные пользователя
      return true;
    } catch (error) {
      return false;
    }
  };

  // Загрузка данных пользователя
  const fetchUser = async () => {
    try {
      user.value = await $api(api.users.info, {
        headers: {
          Authorization: `Bearer ${$auth.getAccessToken()}`,
        },
      });
    } catch (error) {
      console.log("error composable auth", error);
      // Если токен просрочен, пробуем обновить
      const newAccess = await $auth.refreshTokens();
      if (newAccess) {
        await fetchUser();
      }
    }
  };

  // Проверка авторизации (для middleware)
  const checkAuth = async () => {
    if (!$auth.getAccessToken()) {
      const newAccess = await $auth.refreshTokens();
      return !!newAccess;
    }
    return true;
  };

  return { user, login, fetchUser, checkAuth };
};
