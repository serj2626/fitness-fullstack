export default defineNuxtPlugin(({ $config }) => {
    const api = $fetch.create({
      onRequest({ request, options }) {
        request.baseURL = import.meta.server
          ? $config.ssrApiUrl
          : $config.public.apiBase;
  
        if (options.headers) {
          options.headers = {
            ...options.headers,
            Accept: "application/json"
          }
        }
      },
      onRequestError({ request, options, error }) {
        if ($config.public.isDebug) {
          console.log("onRequestError: ", error);
        }
      },
      onResponse({ request, options, response }) {},
      onResponseError({ request, options, response }) {
        if ($config.public.isDebug) {
          console.log("onResponseError: ", response);
        }
      },
    })
    return {
      provide: {
        fetchApi: api
      }
    }
  })
  