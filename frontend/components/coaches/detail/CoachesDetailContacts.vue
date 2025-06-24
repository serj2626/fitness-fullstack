<script setup lang="ts">
import { SocialIcons } from "~/assets/icons/types/social-icons";
defineProps<{
  name: string;
  position: string;
  email: string;
  phone: string;
}>();
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

    <!-- Соцсети -->
    <div class="social-links">
      <a href="#" class="social-link">
        <Icon :name="SocialIcons.TELEGRAM" />
      </a>
      <a href="#" class="social-link">
        <Icon :name="SocialIcons.VK" />
      </a>
      <a href="#" class="social-link">
        <Icon :name="SocialIcons.WHATSAPP" />
      </a>
    </div>

    <!-- Описание -->
    <div class="coach-description">
      <h3 class="section-title">О тренере</h3>
      <div class="description-content">
        <p>
          <strong>Образование:</strong> Российский государственный университет
          физической культуры, спорта, молодежи и туризма
        </p>
        <p>
          <strong>Сертификаты:</strong> Дипломы по нутрициологии и фитнесу
          международного класса
        </p>
        <p><strong>Опыт работы:</strong> Более 10 лет</p>
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
}

.social-links {
  display: flex;
  gap: 15px;
  margin-bottom: 30px;

  .social-link {
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba($white, 0.08);
    border-radius: 50%;
    transition: all 0.3s ease;

    &:hover {
      background: $accent;
      color: $txt;
      transform: translateY(-2px);
    }
  }
}

.coach-description {
  .section-title {
    font-size: 18px;
    font-weight: 600;
    color: $accent;
    margin-bottom: 15px;
    padding-bottom: 8px;
    border-bottom: 1px solid rgba($white, 0.1);
  }

  .description-content {
    display: grid;
    gap: 12px;

    p {
      line-height: 1.5;
      color: rgba($white, 0.9);
    }

    strong {
      color: $white;
      font-weight: 500;
    }
  }
}
</style>
