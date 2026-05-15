export default defineNuxtPlugin(() => {
  const config = useRuntimeConfig();
  const apiFetch = $fetch.create({
    baseURL: config.public.api_url,
    onRequest({ request, options, response, error }) {
      // options.credentials = "include";
      // options.baseURL = import.meta.server ? config.ssrApiUrl : config.public.browserApiUrl
      if (config.public.debug) {
        console.log("making req", options.baseURL, request.toString());
      }
    },
    onResponse({ response }) {},
    onResponseError({ response }) {},
  });
  return {
    provide: {
      api: apiFetch,
    },
  };
});
