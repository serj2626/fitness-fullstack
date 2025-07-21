const authStore = useAuthStore();
const { warning } = useNotify();

export default defineNuxtRouteMiddleware(async (to, from) => {
  console.log("auth middleware", to, from);
  if (to.name === "profile" && !authStore.isAuthenticated) {
    warning("Вы не авторизованы! Пожалуйста, войдите в свой аккаунт");
    console.log("authStore", authStore);
    return navigateTo({ path: "/" });
  } else if (to.name === "login" && authStore.isAuthenticated) {
    return navigateTo({ path: "/profile" });
  }
});
