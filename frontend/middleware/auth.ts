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

// export default defineNuxtRouteMiddleware(async (to) => {
//   const authStore = useAuthStore();
//   const { warning } = useNotify();

//   // Для SSR: сразу проверяем куки на сервере
//   const accessToken = useCookie("access_fitness_token");
//   const isAuthenticated = !!accessToken.value;

//   // Синхронизируем состояние хранилища
//   if (import.meta.client && !authStore.isAuthenticated && isAuthenticated) {
//     await authStore.fetchUser();
//   }

//   // Правила маршрутизации
//   if (to.meta.requiresAuth && !isAuthenticated) {
//     if (import.meta.client) {
//       warning("Требуется авторизация");
//     }
//     return navigateTo({ path: "/" });
//   }

//   if (to.meta.guestOnly && isAuthenticated) {
//     return navigateTo("/profile");
//   }
// });
