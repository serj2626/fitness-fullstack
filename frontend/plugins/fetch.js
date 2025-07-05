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

// export default defineNuxtPlugin((nuxtApp) => {
//   const config = useRuntimeConfig();

//   const apiFetch = $fetch.create({
//     baseURL: config.public.api_url,

//     async onRequest({ request, options }) {
//       let token: string | undefined;

//       if (process.server) {
//         // На сервере: токен из HttpOnly куки
//         const event = nuxtApp.ssrContext?.event;
//         if (event) {
//           const cookie = useCookie('access_token', { event });
//           token = cookie.value;
//         }
//       } else if (process.client) {
//         // На клиенте: токен из обычной (не HttpOnly) куки или Pinia (по желанию)
//         const cookie = useCookie('access_token');
//         token = cookie.value;
//       }

//       if (token) {
//         options.headers = {
//           ...options.headers,
//           Authorization: `Bearer ${token}`,
//         };
//       }

//       if (config.public.debug) {
//         console.log('[api] →', request.toString(), options);
//       }
//     },

//     onResponse({ request, response }) {
//       if (config.public.debug) {
//         console.log('[api] ←', request.toString(), response);
//       }
//     },

//     onResponseError({ request, response }) {
//       console.error('[api] ✖', request.toString(), response.status, response._data);
//     },
//   });

//   return {
//     provide: {
//       api: apiFetch,
//     },
//   };
// });
