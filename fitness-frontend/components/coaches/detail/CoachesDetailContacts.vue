<script lang="ts" setup>
import { SocialIcons } from "~/assets/icons/types/social-icons";
</script>
<template>
  <div class="coaches-detail-contacts">
    <ul class="coaches-detail-contacts__list">
      <li class="coaches-detail-contacts__list-item">
        <icon
          class="coaches-detail-contacts__list-item-icon"
          :name="SocialIcons.USER"
        /><span class="coaches-detail-contacts__list-item-name"
          >Анна Иванова</span
        >
      </li>
      <li class="coaches-detail-contacts__list-item">
        <icon
          class="coaches-detail-contacts__list-item-icon"
          :name="SocialIcons.WORK"
        /><span class="coaches-detail-contacts__list-item-position"
          >Инструктор тренажерного зала</span
        >
      </li>
      <li class="coaches-detail-contacts__list-item">
        <icon
          class="coaches-detail-contacts__list-item-icon"
          :name="SocialIcons.PHONE"
        /><span class="coaches-detail-contacts__list-item-phone"
          >8-800-555-35-35</span
        >
      </li>
      <li class="coaches-detail-contacts__list-item">
        <icon
          class="coaches-detail-contacts__list-item-icon"
          :name="SocialIcons.MAIL"
        /><span class="coaches-detail-contacts__list-item-mail"
          >bs-dev@bk.ru</span
        >
      </li>
      <li class="coaches-detail-contacts__list-item" style="gap: 20px;">
        <icon
          class="coaches-detail-contacts__list-item-icon"
          :name="SocialIcons.TELEGRAM"
        />
        <icon
          class="coaches-detail-contacts__list-item-icon"
          :name="SocialIcons.VK"
        />
        <icon
          class="coaches-detail-contacts__list-item-icon"
          :name="SocialIcons.WHATSAPP"
        />
      </li>
    </ul>
    <p class="coaches-detail-contacts__desc">
      ОБРАЗОВАНИЕ: российский государственный университет физической культуры,
      спорта, молодежи и туризма; Дополнительное образование: дипломы по
      нутрициологии и фитнесу международного класса; СПЕЦИАЛИЗАЦИЯ: -
      Диетология; - Разработка сплит-программ; - Жиросжигание; - Увеличение
      мышечной массы; - Работа на рельеф; - Тренировка сердечно-сосудистой
      системы; - Улучшение пропорций тела; - Реабилитация спины; - Составление
      программ питания; - Подготовка к соревнованиям; СПОРТИВНЫЕ ДОСТИЖЕНИЯ: -
      обладатель кубков чемпионата Европы по бодибилдингу и фитнесу - член
      международной федерации бодибилдинга и фитнеса - судья федерации
      бодибилдинга СПб - Опыт работы более 10 лет ТРЕНЕРСКИЙ СТАЖ: с 2011 года
    </p>
  </div>
</template>
<style scoped lang="scss">
.coaches-detail-contacts {
  &__list {
    display: flex;
    flex-direction: column;
    gap: 20px;

    &-item {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 17px;
      font-weight: 500;
      color: $white;
      &-icon {
        font-size: 22px;
      }
    }
  }
  &__desc {
    padding-block: 20px;
    line-height: 160%;
    font-size: 17px;
    font-weight: 500;
    color: $white;
  }
}
</style>
