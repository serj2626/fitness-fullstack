<script lang="ts" setup>
import { ref, onMounted, nextTick } from 'vue';

const runtimeConfig = useRuntimeConfig();
const siteKey = runtimeConfig.public.recaptchaPublicKey;

const recaptchaEl = ref<HTMLElement | null>(null);
const widgetId = ref<number | null>(null);

onMounted(async () => {
  await nextTick();

  const checkReady = setInterval(() => {
    if (window.grecaptcha && recaptchaEl.value) {
      widgetId.value = window.grecaptcha.render(recaptchaEl.value, {
        sitekey: siteKey,
      });
      clearInterval(checkReady);
    }
  }, 100);
});
</script>

<template>
  <div class="g-recaptcha" ref="recaptchaEl"></div>
</template>