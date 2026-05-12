<script setup lang="ts">
import { api } from "~/api";
import type { IVacancy } from "~/types";
const { $api } = useNuxtApp();
const route = useRoute();
const router = useRouter();

const id = route.params.id;

const { data: vacancy, pending } = await useAsyncData<IVacancy>(
  `vacancy-${id}`,
  () => $api(api.contacts.vacancyDetail(id as string)),
  {
    watch: [() => id],
  },
);

function closeModal() {
  router.back();
}
</script>
<template>
  <div class="modal-overlay" @click.self="closeModal">
    <div class="modal-container">
      <div class="modal-header">
        <h2>{{ vacancy?.title }}</h2>
        <button class="modal-close" @click="closeModal">✕</button>
      </div>
      <div class="modal-body">
        <BaseLoader v-if="pending" />
        <div v-else>
          <div class="vacancy-detail">
            <div class="vacancy-detail__description">
              {{ vacancy?.description }}
            </div>
            <div class="vacancy-detail__content">
              <BaseWysiwyg v-if="vacancy?.content" :html="vacancy?.content" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  backdrop-filter: blur(5px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  color: $white;
  font-weight: 600;
}
.modal-container {
  background: $bg_block;
  border-radius: 24px;
  width: 90%;
  max-width: 800px;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 35px -12px rgba(0, 0, 0, 0.5);
}
.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 24px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}
.modal-close {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: rgba(255, 255, 255, 0.7);
  transition: color 0.2s ease;
}
.vacancy-detail__content {
  padding: 24px 5px;
}
.modal-close:hover {
  color: $accent;
}
.modal-body {
  padding: 24px;
}
</style>
