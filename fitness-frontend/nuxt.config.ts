// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2024-11-01",
  devtools: { enabled: true },
  css: ["~/assets/scss/global.scss"],
  modules: [
    "@nuxt/icon",
    "@nuxt/image",
    "@nuxt/eslint",
    "nuxt-aos",
    "@pinia/nuxt",
    "@sidebase/nuxt-auth",
    "nuxt-swiper",
    "vue-yandex-maps/nuxt",
  ],
  auth: {
    enableGlobalAppMiddleware: true,
    strategies: {
      "django-jwt": {
        scheme: "refresh",
        token: {
          property: "access",
          maxAge: 1800,
        },
        refreshToken: {
          property: "refresh",
          maxAge: 86400,
        },
        user: {
          property: false,
          autoFetch: true,
        },
        endpoints: {
          login: { url: "token/", method: "post" },
          refresh: { url: "token/refresh/", method: "post" },
          user: { url: "user/", method: "get" },
          logout: false, // если логаут не реализован
        },
      },
    },
  },

  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE,
      recaptchaPublicKey: process.env.GOOGLE_CAPTCHA_PUBLIC_KEY,
      tawkKey: process.env.TAWK_ID,
    },
    recaptchaSecretKey: process.env.GOOGLE_CAPTCHA_SECRET_KEY,
  },
  plugins: ["~/plugins/tawk.client.ts"],
  yandexMaps: {
    apikey: process.env.YANDEX_MAP_API_KEY,
    initializeOn: "onComponentMount",
    strictMode: true,
    lang: "ru_RU",
  },
  icon: {
    customCollections: [
      {
        prefix: "icon",
        dir: "./assets/icons",
      },
    ],
  },
  app: {
    head: {
      title: "Фитнес-клуб DV Fitness",
      htmlAttrs: {
        lang: "ru",
      },
      link: [
        {
          rel: "icon",
          type: "image/png",
          href: "/fav/logo.png",
          sizes: "96x96",
        },
        { rel: "icon", type: "image/svg+xml", href: "/logo.png" },
        { rel: "shortcut icon", href: "/logo.pngo" },
        // { rel: 'apple-touch-icon', sizes: '180x180', href: '/public/fav/apple-touch-icon.png' },
        // { rel: 'manifest', href: '/public/fav/site.webmanifest' },
      ],
      meta: [
        { name: "msapplication-TileColor", content: "#da532c" },
        { name: "theme-color", content: "#ffffff" },
        { charset: "UTF-8" },
        { "http-equiv": "X-UA-Compatible", content: "IE=edge" },
        { name: "format-detection", content: "telephone=no" },
        {
          name: "viewport",
          content: "width=device-width, initial-scale=1.0, maximum-scale=5",
        },
        { name: "apple-mobile-web-app-title", content: "pavelpola" },
      ],
      script: [
        {
          src: "https://www.google.com/recaptcha/api.js",
          async: true,
          defer: true,
        },
      ],
    },
    pageTransition: { name: "page", mode: "out-in" },
  },
  vite: {
    // server: {
    //   hmr: {
    //     protocol: 'ws',
    //     host: process.env.DOMAIN
    //   },
    // },
    vue: {
      script: {
        defineModel: true,
        propsDestructure: true,
      },
    },
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: `
              @use '@/assets/scss/_vars.scss' as *;
              @use '@/assets/scss/_mixins.scss' as *;
              @use '@/assets/scss/_animations.scss' as *;
            `,
        },
      },
    },
  },

  // runtimeConfig: {
  //   // The private keys which are only available within server-side
  //   // apiSecret: "/nuxt", // reassign default nuxt api url
  //   // ssrApiUrl: process.env.SSR_API_URL,
  //   // Keys within public, will be also exposed to the client-side
  //   public: {
  //     // isDebug: process.env.DEBUG,
  //     // apiBase: "/nuxt",
  //     // apiUrl: process.env.API_URL,
  //     // mediaUrl: process.env.MEDIA_URL,
  //     yandexCaptchaPublicKey: process.env.YANDEX_CAPTCHA_PUBLIC_KEY,
  //   },
  // },
});
