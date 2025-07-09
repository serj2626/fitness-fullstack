<script lang="ts" setup>
import { ref, computed } from "vue";

const today = new Date();
const selectedDate = ref<Date | null>(null);
const isOpen = ref(false);

const currentYear = ref(today.getFullYear());
const currentMonth = ref(today.getMonth());

const weekdays = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"];
const monthNames = [
  "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
  "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
];

const toggleCalendar = () => {
  isOpen.value = !isOpen.value;
};

const selectDate = (day: number | null) => {
  if (!day) return;
  selectedDate.value = new Date(currentYear.value, currentMonth.value, day);
  isOpen.value = false;
};

const formattedDate = computed(() => {
  if (!selectedDate.value) return "";
  return selectedDate.value.toLocaleDateString("ru-RU", {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
  });
});

const getDaysInMonth = (year: number, month: number) => {
  return new Date(year, month + 1, 0).getDate();
};

const getStartDayOfWeek = (year: number, month: number) => {
  const day = new Date(year, month, 1).getDay();
  return day === 0 ? 6 : day - 1;
};

const days = computed(() => {
  const totalDays = getDaysInMonth(currentYear.value, currentMonth.value);
  const startDay = getStartDayOfWeek(currentYear.value, currentMonth.value);
  const emptyDays = Array(startDay).fill(null);
  return [...emptyDays, ...Array.from({ length: totalDays }, (_, i) => i + 1)];
});

const prevMonth = () => {
  if (currentMonth.value === 0) {
    currentMonth.value = 11;
    currentYear.value--;
  } else {
    currentMonth.value--;
  }
};

const nextMonth = () => {
  if (currentMonth.value === 11) {
    currentMonth.value = 0;
    currentYear.value++;
  } else {
    currentMonth.value++;
  }
};

const isSelected = (day: number | null) => {
  if (!selectedDate.value || !day) return false;
  return (
    selectedDate.value.getDate() === day &&
    selectedDate.value.getMonth() === currentMonth.value &&
    selectedDate.value.getFullYear() === currentYear.value
  );
};
</script>
<template>
  <div class="datepicker">
    <input
      type="text"
      :value="formattedDate"
      readonly
      class="datepicker__input"
      @click="toggleCalendar"
    />
    <div v-if="isOpen" class="datepicker__calendar">
      <div class="datepicker__header">
        <button @click="prevMonth" class="datepicker__nav">&lt;</button>
        <div class="datepicker__month">
          {{ monthNames[currentMonth] }} {{ currentYear }}
        </div>
        <button @click="nextMonth" class="datepicker__nav">&gt;</button>
      </div>

      <div class="datepicker__weekdays">
        <div v-for="day in weekdays" :key="day" class="datepicker__weekday">
          {{ day }}
        </div>
      </div>

      <div class="datepicker__days">
        <div
          v-for="(day, index) in days"
          :key="index"
          class="datepicker__day"
          :class="{ 'datepicker__day--empty': !day, 'datepicker__day--selected': isSelected(day) }"
          @click="selectDate(day)"
        >
          {{ day }}
        </div>
      </div>
    </div>
  </div>
</template>
<style lang="scss" scoped>
.datepicker {
  position: relative;
  width: 260px;
  font-family: "Inter", sans-serif;

  &__input {
    width: 100%;
    padding: 12px 16px;
    border: 1px solid #ccc;
    border-radius: 12px;
    font-size: 16px;
    cursor: pointer;
    background-color: white;
    transition: border 0.2s;

    &:hover {
      border-color: #888;
    }

    &:focus {
      outline: none;
      border-color: #31c178;
      box-shadow: 0 0 0 2px rgba(49, 193, 120, 0.2);
    }
  }

  &__calendar {
    position: absolute;
    top: 100%;
    left: 0;
    margin-top: 8px;
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 12px;
    padding: 16px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    z-index: 20;
  }

  &__header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
  }

  &__month {
    font-weight: 600;
    font-size: 16px;
  }

  &__nav {
    background: none;
    border: none;
    font-size: 18px;
    color: #777;
    cursor: pointer;

    &:hover {
      color: #000;
    }
  }

  &__weekdays {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    text-align: center;
    margin-bottom: 8px;
    font-weight: 500;
    color: #666;
  }

  &__days {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 6px;
  }

  &__day {
    width: 34px;
    height: 34px;
    line-height: 34px;
    text-align: center;
    cursor: pointer;
    border-radius: 8px;
    font-size: 14px;
    color: #333;

    &:hover {
      background-color: #f2f2f2;
    }

    &--empty {
      pointer-events: none;
      background: transparent;
    }

    &--selected {
      background-color: #31c178;
      color: white;
      font-weight: 600;
    }
  }
}
</style>
