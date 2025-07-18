// export default defineNuxtRouteMiddleware(async (to, from) => {
//   const access = useCookie("access_token").value;

//   if (!access) {
//     try {
//       // Попробовать обновить токен
//       await $fetch("/api/auth/refresh", { method: "POST" });
//     } catch (error) {
//       // Если и refresh не сработал — разлогинить
//       return navigateTo("/login");
//     }
//   }
// });

const authStore = useAuthStore();
const { warning } = useNotify();

export default defineNuxtRouteMiddleware(async (to, from) => {
  console.log("auth middleware", to, from);
  if (to.name === "profile" && !authStore.isAuthenticated)
    warning("Вы не авторизованы! Пожалуйста, войдите в свой аккаунт");
  return navigateTo({ path: "/" });
});
