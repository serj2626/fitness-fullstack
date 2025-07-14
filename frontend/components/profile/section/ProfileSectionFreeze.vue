<script setup lang="ts"></script>
<template>
  <section class="user-main__section" v-if="activeTab === 'freeze'">
    <div class="user-main__section-header">
      <h2 class="user-main__section-title">Заморозка абонемента</h2>
    </div>

    <form class="freeze-form" @submit.prevent="submitFreeze">
      <div class="freeze-form__group">
        <label class="freeze-form__label">Причина заморозки</label>
        <select
          class="freeze-form__select"
          v-model="freezeData.reason"
          required
        >
          <option value="">Выберите причину</option>
          <option value="vacation">Отпуск</option>
          <option value="illness">Болезнь</option>
          <option value="business">Командировка</option>
          <option value="other">Другая причина</option>
        </select>
      </div>

      <div class="freeze-form__group">
        <label class="freeze-form__label">Дата начала</label>
        <input
          type="date"
          class="freeze-form__input"
          v-model="freezeData.startDate"
          required
        />
      </div>

      <div class="freeze-form__group">
        <label class="freeze-form__label">Дата окончания</label>
        <input
          type="date"
          class="freeze-form__input"
          v-model="freezeData.endDate"
          required
        />
      </div>

      <div class="freeze-form__group" v-if="freezeData.reason === 'other'">
        <label class="freeze-form__label">Укажите причину</label>
        <textarea
          class="freeze-form__input"
          rows="3"
          v-model="freezeData.customReason"
        ></textarea>
      </div>

      <button type="submit" class="freeze-form__submit">
        Отправить запрос
      </button>

      <div class="freeze-form__info">
        <p>Вы можете заморозить абонемент на срок от 7 до 30 дней.</p>
        <p>
          Осталось дней для заморозки в этом месяце:
          {{ freezeDaysLeft }} из 14
        </p>
      </div>
    </form>
  </section>
</template>
<style scoped lang="scss"></style>
