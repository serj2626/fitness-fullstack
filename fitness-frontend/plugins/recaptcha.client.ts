export default defineNuxtPlugin(() => {
  if (import.meta.client) {
    if (!document.getElementById("recaptcha-script")) {
      const script = document.createElement("script");
      script.src = "https://www.google.com/recaptcha/api.js";
      script.async = true;
      script.defer = true;
      script.id = "recaptcha-script";
      document.head.appendChild(script);
    }
  }
});
