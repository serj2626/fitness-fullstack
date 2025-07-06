<template>
  <div class="base-loader" role="status">
    <span class="loader" />
    <span class="visually-hidden">Загрузка...</span>
  </div>
</template>

<style scoped lang="scss">
.base-loader {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem;
}

.loader {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(255, 255, 255, 0.3);
  border-top-color: $accent; // замените на вашу SCSS переменную, или хардкодьте цвет
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
</style>
