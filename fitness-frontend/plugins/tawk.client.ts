export default defineNuxtPlugin(() => {
  if (import.meta.client) {
    window.Tawk_API = window.Tawk_API || {};
    window.Tawk_API.visitor = {
      language: "ru",
    };
    const key = useRuntimeConfig().public.tawkKey;
    const script = document.createElement("script");
    script.src = `https://embed.tawk.to/${key}`;
    script.async = true;
    script.charset = "UTF-8";
    script.setAttribute("crossorigin", "*");
    document.body.appendChild(script);
  }
});
