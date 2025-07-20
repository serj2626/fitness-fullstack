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
    "nuxt-swiper",
    "vue-yandex-maps/nuxt",
    "@nuxtjs/robots",
    "@nuxtjs/sitemap",
  ],
  sitemap: {
    sources: ["/api/__sitemap__/coaches", "/api/__sitemap__/posts"],
  },
  runtimeConfig: {
    public: {
      api_url: process.env.API_URL,
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
});
