<script setup lang="ts">
import { breadcrumbsSchedulePage } from "~/assets/data/breadcrumbs.data";

interface IWorkout {
  id: number;
  name: string;
  type: string;
  trainer: string;
  time: string;
  day: string;
  capacity: string;
  isPopular: boolean;
  description: string;
}

const activeDay = ref(0);
const selectedWorkout = ref<IWorkout | null>(null);

const days = [
  { label: "Пн", value: "monday" },
  { label: "Вт", value: "tuesday" },
  { label: "Ср", value: "wednesday" },
  { label: "Чт", value: "thursday" },
  { label: "Пт", value: "friday" },
  { label: "Сб", value: "saturday" },
  { label: "Вс", value: "sunday" },
];

const times = [
  "07:00",
  "08:00",
  "09:00",
  "10:00",
  "11:00",
  "12:00",
  "13:00",
  "14:00",
  "15:00",
  "16:00",
  "17:00",
  "18:00",
  "19:00",
  "20:00",
  "21:00",
];

const workouts = ref<IWorkout[]>([
  {
    id: 1,
    name: "Йога",
    type: "yoga",
    trainer: "Анна Петрова",
    time: "09:00 - 10:00",
    day: "monday",
    capacity: "8/12",
    isPopular: true,
    description: "Утренняя йога для пробуждения тела и разума",
  },
  // Другие тренировки...
]);

const filteredWorkouts = (day: string) => {
  return workouts.value.filter((w) => w.day === day);
};

const getWorkoutColor = (type: string) => {
  const colors: Record<string, string> = {
    yoga: "#4CAF50",
    crossfit: "#F44336",
    pilates: "#9C27B0",
    swimming: "#2196F3",
    cycling: "#FF9800",
  };
  return colors[type] || "#2196F3";
};

const openModal = (workout: IWorkout) => {
  selectedWorkout.value = workout;
};
</script>
<template>
  <section class="schedule-page">
    <PagesTopSection title="Расписание тренировок" />

    <div class="schedule-page__content container">
      <BaseBreadCrumbs :breadcrumbs="breadcrumbsSchedulePage" />
      <div class="schedule-page__days">
        <button
          v-for="(day, index) in days"
          :key="day.value"
          :class="{ active: activeDay === index }"
          @click="activeDay = index"
        >
          {{ day.label }}
        </button>
      </div>

      <div class="schedule-page__container">
        <div class="schedule-sidebar">
          <div class="time-slots">
            <div v-for="time in times" :key="time" class="time-slot">
              {{ time }}
            </div>
          </div>
        </div>

        <div class="schedule-main">
          <div
            v-for="(day, dayIndex) in days"
            :key="day.value"
            class="schedule-day"
            :class="{ active: activeDay === dayIndex }"
          >
            <div
              v-for="workout in filteredWorkouts(day.value)"
              :key="workout.id"
              class="workout-card"
              :style="{ backgroundColor: getWorkoutColor(workout.type) }"
              @click="openModal(workout)"
            >
              <div class="workout-info">
                <h3>{{ workout.name }}</h3>
                <p class="trainer">{{ workout.trainer }}</p>
                <p class="time">{{ workout.time }}</p>
              </div>
              <div class="workout-meta">
                <span class="capacity">
                  <Icon name="heroicons:user-group" /> {{ workout.capacity }}
                </span>
                <span v-if="workout.isPopular" class="popular-badge">
                  <Icon name="heroicons:star" /> Популярно
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- <Teleport to="body">
      <WorkoutModal
        v-if="selectedWorkout"
        :workout="selectedWorkout"
        @close="selectedWorkout = null"
      />
    </Teleport> -->
  </section>
</template>
<style lang="scss">
.schedule-page {
  margin-bottom: 50px;
  &__days {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-block: 30px;

    button {
      padding: 12px 20px;
      background: $bg_block;
      border: none;
      border-radius: 30px;
      color: $header_link;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.3s ease;

      &.active {
        background: $accent;
        color: $txt;
      }

      &:hover {
        transform: translateY(-2px);
      }
    }
  }
  &__container {
    display: flex;
    max-width: 1200px;
    margin: 0 auto;
    background: rgba($white, 0.05);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  }
}

.schedule-sidebar {
  width: 80px;
  background: rgba($accent, 0.1);
  border-right: 1px solid rgba($white, 0.1);
}

.time-slots {
  display: flex;
  flex-direction: column;
}

.time-slot {
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: $header_link;
  font-size: 0.9rem;
  border-bottom: 1px solid rgba($white, 0.05);
}

.schedule-main {
  flex: 1;
  position: relative;
  min-height: 800px;
}

.schedule-day {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  padding: 20px;
  display: none;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 15px;
  align-content: start;

  &.active {
    display: grid;
  }
}

.workout-card {
  padding: 20px;
  border-radius: 8px;
  color: $txt;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);

  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);

    &::after {
      opacity: 0.1;
    }
  }

  &::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: $white;
    opacity: 0;
    transition: opacity 0.3s ease;
  }
}

.workout-info {
  position: relative;
  z-index: 2;

  h3 {
    font-size: 1.2rem;
    margin-bottom: 8px;
  }

  .trainer {
    font-size: 0.9rem;
    opacity: 0.9;
    margin-bottom: 5px;
  }

  .time {
    font-weight: 600;
    font-size: 0.95rem;
  }
}

.workout-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 15px;
  position: relative;
  z-index: 2;

  .capacity {
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 0.85rem;
  }

  .popular-badge {
    background: rgba($white, 0.9);
    padding: 3px 8px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 3px;
  }
}

@media (max-width: $tablet) {
  .schedule-container {
    flex-direction: column;
  }

  .schedule-sidebar {
    width: 100%;
    border-right: none;
    border-bottom: 1px solid rgba($white, 0.1);
  }

  .time-slots {
    flex-direction: row;
    overflow-x: auto;
    padding: 10px 0;

    .time-slot {
      width: 60px;
      height: auto;
      padding: 10px;
      flex-shrink: 0;
    }
  }

  .schedule-day {
    grid-template-columns: 1fr;
    padding: 15px;
  }
}
</style>
