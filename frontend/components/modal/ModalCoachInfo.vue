<script setup lang="ts">
const modalsStore = useModalsStore();
</script>
<template>
  <div class="modal" :class="{ active: isModalOpen }">
    <div
      class="modal-overlay"
      @click="modalsStore.closeModal('coachInfo')"
    ></div>
    <div class="modal-content">
        <BaseButtonClose
          top="10px"
          right="10px"
          :size="26"
          @click="modalsStore.closeModal('coachInfo')"
        />
      <div class="modal-body">
        <div class="modal-image">
          <img :src="selectedTrainer.photo" :alt="selectedTrainer.name" />
        </div>
        <div class="modal-info">
          <h2>{{ selectedTrainer.name }}</h2>
          <p class="specialization">{{ selectedTrainer.specialization }}</p>

          <div class="details">
            <div class="detail-item">
              <span class="detail-label">Опыт:</span>
              <span class="detail-value"
                >{{ selectedTrainer.experience }} лет</span
              >
            </div>
            <div class="detail-item">
              <span class="detail-label">Направления:</span>
              <span class="detail-value">{{
                selectedTrainer.directions.join(", ")
              }}</span>
            </div>
            <div class="detail-item">
              <span class="detail-label">Сертификаты:</span>
              <span class="detail-value">{{
                selectedTrainer.certificates.join(", ")
              }}</span>
            </div>
          </div>

          <p class="full-bio">{{ selectedTrainer.full_bio }}</p>

          <div class="modal-actions">
            <button class="btn-primary">Записаться на тренировку</button>
            <div class="social-links">
              <a
                v-if="selectedTrainer.social_instagram"
                :href="selectedTrainer.social_instagram"
                target="_blank"
              >
                <i class="icon-instagram"></i>
              </a>
              <a
                v-if="selectedTrainer.social_telegram"
                :href="selectedTrainer.social_telegram"
                target="_blank"
              >
                <i class="icon-telegram"></i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss"></style>
