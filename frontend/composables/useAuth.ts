export const useAuth = () => {
  const { $api } = useNuxtApp();
  const token = useCookie("auth_token");
  const user = useState("user");

  const login = async (credentials) => {
    const { data } = await $api.post("/auth/login", credentials);
    token.value = data.token;
    await fetchUser();
  };

  const fetchUser = async () => {
    if (token.value) {
      user.value = await $api.get("/auth/user");
    }
  };

  const logout = () => {
    token.value = null;
    user.value = null;
  };

  return { token, user, login, logout, fetchUser };
};
