<script setup lang="ts">
const { firstName, lastName, width, height } = withDefaults(
  defineProps<{
    firstName: string;
    lastName: string;
    width?: string;
    height?: string;
  }>(),
  {
    width: "50px",
    height: "50px",
  }
);

const fullName = computed(() => {
  const f = firstName?.[0] ?? "М";
  const l = lastName?.[0] ?? "И";
  return `${f}${l}`;
});
</script>
<template>
  <div class="avatar-component">
    <div class="avatar-component__wrapper">
      {{ fullName }}
    </div>
  </div>
</template>
<style scoped lang="scss">
.avatar-component {
  width: v-bind(width);
  height: v-bind(height);
  border-radius: 50%;
  outline: 2px solid $accent;
  background-color: $bg;
  display: flex;
  justify-content: center;
  align-items: center;
}
.avatar-component__wrapper {
  font-size: 20px;
  color: $accent;
  font-weight: 600;
  text-transform: uppercase;
  line-height: 1;
}
</style>
