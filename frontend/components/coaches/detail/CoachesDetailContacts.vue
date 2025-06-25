<script setup lang="ts">
import { SocialIcons } from "~/assets/icons/types/social-icons";
const props = defineProps<{
  name: string;
  position: string;
  email: string;
  phone: string;
  socials: { type: string; link: string }[];
  keywords: string;
  experience: number;
  education: string;
}>();

function getIcon(title: string) {
  return `ri:${title}-fill`;
}

const getListKeywords = computed(() => {
  return props.keywords.split(',');
});
const getExperience = computed(() => {
  if (props.experience > 0) {
    return `Более ${props.experience} лет`;
  }
  return "Не указан";
});
</script>
<template>
  <div class="coach-detail-contacts">
    <div class="coach-detail-contacts__cards">
      <div class="coach-detail-contacts__cards-item">
        <Icon
          :name="SocialIcons.USER"
          class="coach-detail-contacts__cards-item-icon"
        />
        <div>
          <div class="coach-detail-contacts__cards-item-label">Имя</div>
          <div class="coach-detail-contacts__cards-item-value">{{ name }}</div>
          {{ getListKeywords.length }}
        </div>
      </div>

      <div class="coach-detail-contacts__cards-item">
        <Icon
          :name="SocialIcons.WORK"
          class="coach-detail-contacts__cards-item-icon"
        />
        <div>
          <div class="coach-detail-contacts__cards-item-label">
            Специализация
          </div>
          <div class="coach-detail-contacts__cards-item-value">
            {{ position }}
          </div>
        </div>
      </div>

      <div class="coach-detail-contacts__cards-item clickable">
        <Icon
          :name="SocialIcons.PHONE"
          class="coach-detail-contacts__cards-item-icon"
        />
        <div>
          <div class="coach-detail-contacts__cards-item-label">Телефон</div>
          <a
            href="tel:+78005553535"
            class="coach-detail-contacts__cards-item-value"
            >{{ phone }}</a
          >
        </div>
      </div>

      <div class="coach-detail-contacts__cards-item clickable">
        <Icon
          :name="SocialIcons.MAIL"
          class="coach-detail-contacts__cards-item-icon"
        />
        <div>
          <div class="coach-detail-contacts__cards-item-label">Email</div>
          <a
            href="mailto:bs-dev@bk.ru"
            class="coach-detail-contacts__cards-item-value"
            >{{ email }}</a
          >
        </div>
      </div>
    </div>

    <div class="coach-detail-contacts__social-links">
      <Icon
        v-for="icon in socials"
        :key="icon.type"
        class="coach-detail-contacts__social-links-icon"
        size="30"
        :name="getIcon(icon.type)"
      />
    </div>

    <div class="coach-detail-contacts__description">
      <h3 class="coach-detail-contacts__description-title">О тренере</h3>
      <!-- <div style="color: aliceblue;">
        {{ keywords.split(',') }}
      </div> -->
      <ul
        v-if="getListKeywords.length > 0"
        class="coach-detail-contacts__description-keywords"
      >
        <li
          v-for="word in getListKeywords"
          :key="word"
          class="coach-detail-contacts__description-keywords-item"
        >
          {{ word }}
        </li>
      </ul>
      <div class="coach-detail-contacts__description-content">
        <p>
          <strong>Образование: </strong>
          {{ education.length > 0 ? education : "Не указано" }}
        </p>
        <p>
          <strong>Сертификаты: </strong> Дипломы по нутрициологии и фитнесу
          международного класса
        </p>
        <p>
          <strong>Опыт работы: </strong>
          {{ getExperience }}
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.coach-detail-contacts {
  padding: 20px;
  background: rgba($white, 0.05);
  border-radius: 12px;

  &__cards {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
    &-item {
      display: flex;
      gap: 15px;
      align-items: center;
      padding: 15px;
      background: rgba($white, 0.03);
      border-radius: 8px;
      transition: all 0.3s ease;

      &.clickable:hover {
        background: rgba($accent, 0.1);
        transform: translateY(-2px);
      }

      &-icon {
        font-size: 24px;
        color: $accent;
        flex-shrink: 0;
      }

      &-label {
        font-size: 14px;
        color: rgba($white, 0.7);
        margin-bottom: 4px;
      }

      &-value {
        font-size: 16px;
        font-weight: 500;
        color: $white;
      }

      a.value:hover {
        color: $accent;
      }
    }
  }
  &__social-links {
    display: flex;
    gap: 15px;
    margin-bottom: 30px;

    &-icon {
      display: flex;
      align-items: center;
      justify-content: center;
      background: $white;
      border-radius: 50%;
      transition: all 0.3s ease;

      &:hover {
        background: $accent;
        color: $txt;
        transform: translateY(-2px);
      }
    }
  }
  &__description {
    &-title {
      font-size: 18px;
      font-weight: 600;
      color: $accent;
      margin-bottom: 15px;
      padding-bottom: 8px;
      border-bottom: 1px solid rgba($white, 0.1);
    }
    &-keywords {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
      margin-block: 10px 20px;
      &-item {
        border: 1px solid $accent;
        padding: 8px 12px;
        border-radius: 8px;
        color: $accent;
        font-size: 12px;
        transition: all 0.3s ease;
        user-select: none;

        &:hover {
          background-color: rgba($accent, 0.8);
          color: $txt;
        }
      }
    }

    &-content {
      display: grid;
      gap: 12px;
      p {
        line-height: 1.5;
        color: rgba($white, 0.9);
      }

      strong {
        color: $white;
        font-weight: 700;
      }
    }
  }
}
</style>
