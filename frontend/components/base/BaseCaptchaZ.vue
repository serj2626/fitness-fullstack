<script setup lang="ts">
import { onMounted, ref } from "vue";

const props = defineProps({
  hl: { type: String, default: "ru" },
  test: { type: Boolean, default: false },
  webview: { type: Boolean, default: false },
  invisible: { type: Boolean, default: false },
  shieldPosition: { type: String, default: "top-left" },
  hideShield: { type: Boolean, default: true },
  error: { type: String, default: "" },
});

const { $config } = useNuxtApp();
const emit = defineEmits(["success", "error", "expired"]);

const captchaEl = ref<HTMLElement | null>(null);
const widgetId = ref<number | null>(null);
const siteKey = $config.public.recaptchaPublicKey;

function renderCaptcha() {
  if (!window.grecaptcha || !captchaEl.value) return;

  widgetId.value = window.grecaptcha.render(captchaEl.value, {
    sitekey: siteKey,
    callback: (token: string) => {
      emit("success", token);
    },
    "expired-callback": () => {
      emit("expired");
    },
    "error-callback": () => {
      emit("error", "Recaptcha error");
    },
  });
}

function loadRecaptchaScript() {
  return new Promise<void>((resolve, reject) => {
    if (window.grecaptcha) {
      resolve();
      return;
    }

    const script = document.createElement("script");
    script.src = "https://www.google.com/recaptcha/api.js?render=explicit";
    script.async = true;
    script.defer = true;
    script.onload = () => resolve();
    script.onerror = () => reject("reCAPTCHA script failed to load");
    document.head.appendChild(script);
  });
}

function resetCaptcha() {
  if (widgetId.value !== null && window.grecaptcha) {
    window.grecaptcha.reset(widgetId.value);
  }
}

defineExpose({
  reset: resetCaptcha
})

onMounted(async () => {
  try {
    await loadRecaptchaScript();
    renderCaptcha();
  } catch (e) {
    emit("error", e);
  }
});
</script>

<template>
  <div class="captcha-component">
    <div ref="captchaEl"></div>
    <div v-if="error" class="text-danger">{{ error }}</div>
  </div>
</template>
<style scoped lang="scss">
.text-danger {
  color: red;
  font-size: 14px;
  font-weight: 600;
}
</style>
