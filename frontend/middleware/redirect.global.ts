export default defineNuxtRouteMiddleware((to, from) => {
  console.log("redirect middleware", to.path, from.path);
  console.log("client", import.meta.client);
  console.log("ser  ", import.meta.server);
  if (!to.path.endsWith("/") && to.path !== "/") {
    return navigateTo(to.path + "/", { redirectCode: 301 });
  }
});
