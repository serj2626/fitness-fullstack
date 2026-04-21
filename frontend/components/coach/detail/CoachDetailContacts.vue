<script setup lang="ts">
import {
  getSocialIcon,
  type TSocialIcon,
} from "~/assets/icons/types/social-icons";
import type { ICoachCategory, ICoachSocial } from "~/types";

const props = defineProps<{
  name: string;
  categories: ICoachCategory[] | [];
  email: string;
  phone: string;
  socials?: ICoachSocial[];
  experience: number;
}>();

function getCategories(cats: ICoachCategory[]) {
  return cats.map((c) => c.name).join(", ");
}
</script>

<template>
  <div class="coach-contacts">
    <!-- Основной список контактов -->
    <ul class="contact-list">
      <li class="contact-item">
        <Icon name="ri:user-3-line" class="contact-icon" />
        <div class="contact-details">
          <span class="contact-value">{{ name }}</span>
        </div>
      </li>

      <li class="contact-item">
        <Icon name="ri:briefcase-line" class="contact-icon" />
        <div class="contact-details">
          <span class="contact-value">{{
            getCategories(categories) || "—"
          }}</span>
        </div>
      </li>

      <li class="contact-item">
        <Icon name="ri:phone-line" class="contact-icon" />
        <div class="contact-details">
          <a :href="`tel:${phone}`" class="contact-value">{{ phone }}</a>
        </div>
      </li>

      <li class="contact-item">
        <Icon name="ri:mail-line" class="contact-icon" />
        <div class="contact-details">
          <a :href="`mailto:${email}`" class="contact-value">{{ email }}</a>
        </div>
      </li>

      <li class="contact-item">
        <Icon name="ri:calendar-check-line" class="contact-icon" />
        <div class="contact-details">
          <span class="contact-value">{{ experience }} лет</span>
        </div>
      </li>
    </ul>

    <!-- Социальные сети -->
    <div v-if="socials?.length" class="social-section">
      <div class="social-divider"></div>
      <ul class="social-list">
        <li v-for="social in socials" :key="social.id" class="social-item">
          <a :href="social.link" target="_blank" rel="noopener noreferrer">
            <Icon
              class="social-icon"
              :name="getSocialIcon(social.title as TSocialIcon)"
              size="20"
            />
            <span class="social-title">{{ social.title }}</span>
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped lang="scss">
.contact-icon {
  color: $accent;
  font-size: 20px;
}
.contact-value {
  color: $white;
  font-size: 14px;
  font-weight: 500;
}
.contact-list {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 15px;
}
.contact-details {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.social-section{
  margin-top: 20px;
}
.social-divider {
  width: 100%;
  height: 1px;
  background: rgba($white, 0.1);
  margin-bottom: 15px;
}
.social-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.social-item {
  display: flex;
  align-items: center;
  gap: 15px;
}
.social-icon {
  color: $white;
  font-size: 20px;
}
.social-title {
  color: $white;
  font-size: 14px;
  font-weight: 500;
}
</style>
