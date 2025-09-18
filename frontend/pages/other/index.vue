<script setup lang="ts">
const bg = ref(null);

function onMouseMove(e: MouseEvent) {
  const strength = 60;
  const x = (e.clientX / window.innerWidth - 0.5) * strength;
  const y = (e.clientY / window.innerHeight - 0.5) * strength;
  bg.value && (bg.value.style.transform = `translate(${x}px, ${y}px)`);
}
</script>
<template>
  <div class="parallax-container" @mousemove="onMouseMove">
    <div ref="bg" class="parallax-bg" />
    <div class="content"><slot /></div>
  </div>
</template>

<style scoped>
.parallax-container {
  position: relative;
  height: 100vh;
  overflow: hidden;
}
.parallax-bg {
  position: absolute;
  width: 120%;
  height: 120%;
  top: -10%;
  left: -10%;
  background: url("/first/zal.jpg") center/cover no-repeat;
  transition: transform 0.2s ease-out;
}
.content {
  position: relative;
  z-index: 1;
  text-align: center;
  padding-top: 40vh;
  color: white;
}
</style>
