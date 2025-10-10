<script setup>
const props = defineProps({
  theme: { type: String, default: "light" }, // 'dark' | 'light' | 'auto'
  size: { type: String, default: "normal" }, // 'normal' | 'compact'
  marginBottom: { type: String, default: "0" },
});

const sitekey = useRuntimeConfig().public.cloudFlarePublicKey;

const emit = defineEmits(["verified", "expired", "error"]);

const captchaEl = ref(null);
let widgetId = null;

function onVerify(token) {
  emit("verified", token);
}

onMounted(() => {
  if (typeof window.turnstile === "undefined") {
    const script = document.createElement("script");
    script.src = "https://challenges.cloudflare.com/turnstile/v0/api.js";
    script.async = true;
    script.defer = true;
    script.onload = () => {
      renderCaptcha();
    };
    document.head.appendChild(script);
  } else {
    renderCaptcha();
  }
});

function renderCaptcha() {
  widgetId = window.turnstile.render(captchaEl.value, {
    sitekey: sitekey,
    theme: props.theme,
    size: props.size,
    callback: (token) => emit("verified", token),
    "error-callback": () => emit("error"),
    "expired-callback": () => emit("expired"),
  });
}

onBeforeUnmount(() => {
  if (widgetId && window.turnstile) {
    window.turnstile.remove(widgetId);
  }
});
</script>
<template>
  <div>
    <div
      ref="captchaEl"
      class="cf-turnstile"
      :data-sitekey="siteKey"
      :data-theme="theme"
      :data-size="size"
      :data-callback="onVerify"
    />
  </div>
</template>

<style scoped>
.cf-turnstile {
  display: flex;
  justify-content: start;
  margin-bottom: v-bind("marginBottom");
}
</style>
