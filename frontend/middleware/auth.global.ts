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

export default defineNuxtRouteMiddleware(async (to) => {
  console.log("auth middleware", to);
});
