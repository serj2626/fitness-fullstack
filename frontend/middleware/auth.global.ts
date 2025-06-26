// export default defineNuxtRouteMiddleware(async (to) => {
//   const { $auth } = useNuxtApp();
//   const { checkAuth } = useAuth();

//   if (to.meta.requiresAuth && !await checkAuth()) {
//     return navigateTo('/login');
//   }
// });

export default defineNuxtRouteMiddleware(async (to) => {
  console.log("auth middleware", to);
});
