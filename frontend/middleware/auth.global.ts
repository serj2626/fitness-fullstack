export default defineNuxtRouteMiddleware(async () => {
  const authStore = useAuthStore();

  const access = useCookie("access_fitness_token").value;
  const refresh = useCookie("refresh_fitness_token").value;

  if (!access && !refresh) return;

  if (authStore.user) return;

  try {
    await authStore.fetchUser();
  } catch {
    const refreshed = await useRefreshToken();

    if (refreshed) {
      try {
        await authStore.fetchUser();
      } catch {
        authStore.logout();
      }
    } else {
      authStore.logout();
    }
  }
});
