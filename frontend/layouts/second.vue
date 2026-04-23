<template>
  <div class="second-layout">
    <HeaderComponent />
    <main>
      <slot />
    </main>
    <ModalComponent />
  </div>
</template>
<style lang="scss">
.second-layout {
  min-height: 100vh;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  main {
    flex-grow: 1;
  }
}
</style>
