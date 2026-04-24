<script setup lang="ts">
import {
  getSocialIcon,
  type TSocialIcon,
} from "~/assets/icons/types/social-icons";
import type {  ICoachSocial } from "~/types";

defineProps<{
  name: string;
  categories: string[];
  email: string;
  phone: string;
  socials?: ICoachSocial[];
  experience: number;
}>();


</script>

<template>
  <div class="coach-contacts">
    <!-- Основной список контактов -->
    <ul class="contact-list">
      <li class="contact-item">
        <div class="contact-icon-wrapper">
          <Icon name="ri:user-3-line" class="contact-icon" />
        </div>
        <div class="contact-details">
          <span class="contact-label">Имя</span>
          <span class="contact-value">{{ name }}</span>
        </div>
      </li>

      <li class="contact-item">
        <div class="contact-icon-wrapper">
          <Icon name="ri:briefcase-line" class="contact-icon" />
        </div>
        <div class="contact-details">
          <span class="contact-label">Категории</span>
          <span class="contact-value">{{
            getCategories(categories) || "—"
          }}</span>
        </div>
      </li>

      <li class="contact-item">
        <div class="contact-icon-wrapper">
          <Icon name="ri:phone-line" class="contact-icon" />
        </div>
        <div class="contact-details">
          <span class="contact-label">Телефон</span>
          <a :href="`tel:${phone}`" class="contact-value contact-link">{{
            phone
          }}</a>
        </div>
      </li>

      <li class="contact-item">
        <div class="contact-icon-wrapper">
          <Icon name="ri:mail-line" class="contact-icon" />
        </div>
        <div class="contact-details">
          <span class="contact-label">Email</span>
          <a :href="`mailto:${email}`" class="contact-value contact-link">{{
            email
          }}</a>
        </div>
      </li>

      <li class="contact-item">
        <div class="contact-icon-wrapper">
          <Icon name="ri:calendar-check-line" class="contact-icon" />
        </div>
        <div class="contact-details">
          <span class="contact-label">Опыт</span>
          <span class="contact-value">{{ getExperience(experience) }}</span>
        </div>
      </li>
    </ul>

    <!-- Социальные сети -->
    <div v-if="socials?.length" class="social-section">
      <div class="social-divider"></div>
      <ul class="social-list">
        <li v-for="social in socials" :key="social.id" class="social-item">
          <a
            :href="social.link"
            target="_blank"
            rel="noopener noreferrer"
            class="social-link"
          >
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
.coach-contacts {
  background: rgba(255, 255, 255, 0.03);
  border-radius: 20px;
  padding: 24px;
  backdrop-filter: blur(2px);
  transition: all 0.2s ease;
}

.contact-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 16px;
  transition: transform 0.2s ease;

  &:hover {
    transform: translateX(4px);
  }
}

.contact-icon-wrapper {
  width: 40px;
  height: 40px;
  background: rgba($accent, 0.12);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s ease;

  .contact-item:hover & {
    background: rgba($accent, 0.25);
  }
}

.contact-icon {
  color: $accent;
  font-size: 20px;
  transition: transform 0.2s ease;

  .contact-item:hover & {
    transform: scale(1.05);
  }
}

.contact-details {
  display: flex;
  flex-direction: column;
  gap: 4px;
  flex: 1;
}

.contact-label {
  font-size: 12px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: rgba($white, 0.5);
}

.contact-value {
  font-size: 15px;
  font-weight: 500;
  color: $white;
  line-height: 1.4;
  word-break: break-word;
}

.contact-link {
  text-decoration: none;
  transition: color 0.2s ease;
  border-bottom: 1px dashed rgba($accent, 0.3);

  &:hover {
    color: $accent;
    border-bottom-color: $accent;
  }
}

.social-section {
  margin-top: 28px;
}

.social-divider {
  width: 100%;
  height: 1px;
  background: linear-gradient(
    90deg,
    rgba($white, 0.05) 0%,
    rgba($accent, 0.3) 50%,
    rgba($white, 0.05) 100%
  );
  margin-bottom: 20px;
}

.social-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.social-item {
  transition: transform 0.2s ease;

  &:hover {
    transform: translateX(4px);
  }
}

.social-link {
  display: flex;
  align-items: center;
  gap: 14px;
  text-decoration: none;
  padding: 8px 12px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.02);
  transition: background 0.2s ease, color 0.2s ease;

  &:hover {
    background: rgba($accent, 0.1);
  }
}

.social-icon {
  color: rgba($white, 0.7);
  font-size: 20px;
  transition: color 0.2s ease, transform 0.2s ease;

  .social-link:hover & {
    color: $accent;
    transform: scale(1.05);
  }
}

.social-title {
  font-size: 14px;
  font-weight: 500;
  color: rgba($white, 0.8);
  transition: color 0.2s ease;

  .social-link:hover & {
    color: $accent;
  }
}

/* Адаптивность для мобильных устройств */
@media (max-width: 768px) {
  .coach-contacts {
    padding: 16px;
  }

  .contact-item {
    gap: 12px;
  }

  .contact-icon-wrapper {
    width: 36px;
    height: 36px;
  }

  .contact-value {
    font-size: 14px;
  }

  .social-link {
    padding: 6px 10px;
  }
}
</style>