<script setup lang="ts">
interface ICaptchaProps {
  theme?: "dark" | "light" | "auto";
  size?: "normal" | "compact";
  marginBottom?: string;
  position?: "start" | "center" | "end";
}

const {
  theme = "light",
  size = "normal",
  marginBottom = "0",
  position = "start",
} = defineProps<ICaptchaProps>();

const siteKey = useRuntimeConfig().public.cloudFlarePublicKey;

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
    sitekey: siteKey,
    theme: theme,
    size: size,
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
  justify-content: v-bind("position");
  margin-bottom: v-bind("marginBottom");
}
</style>
