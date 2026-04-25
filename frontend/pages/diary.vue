<template>
  <div class="training-diary">
    <div class="container">
      <h1 class="page-title">Дневник тренировок</h1>

      <!-- Форма добавления новой тренировки -->
      <div class="card">
        <h2 class="card-title">Добавить тренировку</h2>
        <form @submit.prevent="addWorkout" class="diary-form">
          <!-- Дата -->
          <div class="form-group">
            <label class="form-label">Дата тренировки</label>
            <input
              v-model="newWorkout.date"
              type="date"
              class="form-input"
              required
            />
          </div>

          <!-- Выбор упражнения -->
          <div class="form-group">
            <label class="form-label">Упражнение</label>
            <select v-model="newWorkout.exerciseId" class="form-input" required>
              <option value="" disabled>Выберите упражнение</option>
              <option
                v-for="exercise in exercises"
                :key="exercise.id"
                :value="exercise.id"
              >
                {{ exercise.name }}
              </option>
            </select>
          </div>

          <!-- Произвольное количество подходов -->
          <div class="form-group">
            <label class="form-label">Подходы</label>
            <div
              v-for="(set, index) in newWorkout.sets"
              :key="index"
              class="set-row"
            >
              <div class="set-number">Подход {{ index + 1 }}</div>
              <div class="set-fields">
                <input
                  v-model.number="set.weight"
                  type="number"
                  step="0.5"
                  placeholder="Вес (кг)"
                  class="form-input-small"
                  required
                />
                <input
                  v-model.number="set.reps"
                  type="number"
                  placeholder="Повторения"
                  class="form-input-small"
                  required
                />
                <button
                  type="button"
                  class="btn-icon"
                  @click="removeSet(index)"
                  :disabled="newWorkout.sets.length === 1"
                >
                  🗑️
                </button>
              </div>
            </div>
            <button type="button" class="btn-add-set" @click="addSet">
              + Добавить подход
            </button>
          </div>

          <!-- Кнопка отправки -->
          <BaseButton type="submit" size="md" class="submit-btn">
            Сохранить тренировку
          </BaseButton>
        </form>
      </div>

      <!-- История тренировок -->
      <div class="card history-card">
        <h2 class="card-title">История тренировок</h2>

        <div v-if="loading" class="loading-state">Загрузка...</div>
        <div v-else-if="workouts.length === 0" class="empty-state">
          Пока нет добавленных тренировок. Добавьте первую!
        </div>

        <!-- Список тренировок, сгруппированных по датам -->
        <div v-for="workout in workouts" :key="workout.id" class="workout-item">
          <div class="workout-header">
            <div class="workout-date">{{ formatDate(workout.date) }}</div>
            <div class="workout-exercise">{{ workout.exerciseName }}</div>
            <button
              v-if="!workout.synced"
              class="btn-sync"
              @click="syncWorkout(workout)"
            >
              ⚙️ Синхронизировать
            </button>
          </div>
          <div class="workout-sets">
            <div
              v-for="set in workout.sets"
              :key="set.id || set.index"
              class="set-detail"
            >
              <span>Подход {{ set.setNumber }}:</span>
              <span>{{ set.weight }} кг × {{ set.reps }} раз</span>
            </div>
          </div>
          <button class="btn-delete-workout" @click="deleteWorkout(workout.id)">
            Удалить
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";
// Предполагается, что BaseButton уже импортирован глобально или импортируем
// import BaseButton from '~/components/BaseButton.vue';

// Типы
interface Exercise {
  id: number;
  name: string;
  muscleGroup?: string;
}

interface WorkoutSet {
  weight: number;
  reps: number;
  // для отображения после сохранения
  setNumber?: number;
  id?: number;
}

interface Workout {
  id: number;
  date: string; // YYYY-MM-DD
  exerciseId: number;
  exerciseName: string;
  sets: WorkoutSet[];
  synced?: boolean;
}

// Состояния
const loading = ref(false);
const workouts = ref<Workout[]>([]);
const nextId = ref(1);

// Список упражнений (можно загрузить с API)
const exercises = ref<Exercise[]>([
  { id: 1, name: "Жим лёжа", muscleGroup: "Грудь" },
  { id: 2, name: "Приседания со штангой", muscleGroup: "Ноги" },
  { id: 3, name: "Становая тяга", muscleGroup: "Спина" },
  { id: 4, name: "Тяга верхнего блока", muscleGroup: "Спина" },
  { id: 5, name: "Разгибания на трицепс", muscleGroup: "Трицепс" },
  { id: 6, name: "Сгибания на бицепс", muscleGroup: "Бицепс" },
  { id: 7, name: "Жим ногами", muscleGroup: "Ноги" },
  { id: 8, name: "Отжимания", muscleGroup: "Грудь" },
]);

// Новая тренировка (форма)
const newWorkout = reactive({
  date: new Date().toISOString().slice(0, 10),
  exerciseId: "",
  sets: [] as WorkoutSet[],
});

// Добавить пустой подход
function addSet() {
  newWorkout.sets.push({ weight: 0, reps: 0 });
}

// Удалить подход
function removeSet(index: number) {
  if (newWorkout.sets.length > 1) {
    newWorkout.sets.splice(index, 1);
  }
}

// Сохранить тренировку локально (без бэкенда – только для демо)
function addWorkout() {
  if (!newWorkout.exerciseId) return;
  if (newWorkout.sets.length === 0) {
    alert("Добавьте хотя бы один подход");
    return;
  }
  // Проверка заполненности
  const allFilled = newWorkout.sets.every(
    (set) => set.weight > 0 && set.reps > 0,
  );
  if (!allFilled) {
    alert("Заполните вес и повторения для всех подходов");
    return;
  }

  const exercise = exercises.value.find(
    (ex) => ex.id === Number(newWorkout.exerciseId),
  );
  if (!exercise) return;

  const newId = nextId.value++;
  const workout: Workout = {
    id: newId,
    date: newWorkout.date,
    exerciseId: Number(newWorkout.exerciseId),
    exerciseName: exercise.name,
    sets: newWorkout.sets.map((set, idx) => ({
      ...set,
      setNumber: idx + 1,
      id: Date.now() + idx,
    })),
    synced: true, // в демо считаем синхронизированным
  };
  workouts.value.unshift(workout);
  // Сброс формы (сохраняем выбранную дату, сбрасываем упражнение и подходы)
  newWorkout.exerciseId = "";
  newWorkout.sets = [];
  // Добавим один пустой подход по умолчанию
  addSet();

  // Здесь можно отправить на бэкенд, но пока просто сохраняем в localStorage
  saveToLocalStorage();
}

// Загрузка тренировок из localStorage (демо)
function loadFromLocalStorage() {
  const saved = localStorage.getItem("workoutDiary");
  if (saved) {
    try {
      const data = JSON.parse(saved);
      workouts.value = data;
      if (workouts.value.length) {
        // устанавливаем следующий id больше максимального
        const maxId = Math.max(...workouts.value.map((w) => w.id), 0);
        nextId.value = maxId + 1;
      }
    } catch (e) {
      console.error(e);
    }
  }
}

function saveToLocalStorage() {
  localStorage.setItem("workoutDiary", JSON.stringify(workouts.value));
}

// Асинхронная синхронизация (имитация отправки на сервер)
async function syncWorkout(workout: Workout) {
  if (workout.synced) return;
  // Имитация запроса
  await new Promise((resolve) => setTimeout(resolve, 500));
  workout.synced = true;
  saveToLocalStorage();
  alert("Тренировка синхронизирована с сервером");
}

// Удаление тренировки
function deleteWorkout(id: number) {
  if (confirm("Удалить эту тренировку?")) {
    workouts.value = workouts.value.filter((w) => w.id !== id);
    saveToLocalStorage();
  }
}

// Форматирование даты
function formatDate(dateStr: string) {
  const options: Intl.DateTimeFormatOptions = {
    year: "numeric",
    month: "long",
    day: "numeric",
  };
  return new Date(dateStr).toLocaleDateString("ru-RU", options);
}

// Инициализация: загружаем данные и добавляем первый пустой подход
onMounted(() => {
  loadFromLocalStorage();
  if (newWorkout.sets.length === 0) addSet();
});
</script>

<style scoped lang="scss">
.training-diary {
  .page-title {
    font-size: 2rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 2rem;
    text-align: center;
  }

  .card {
    background: white;
    border-radius: 20px;
    box-shadow:
      0 4px 6px -1px rgba(0, 0, 0, 0.1),
      0 2px 4px -1px rgba(0, 0, 0, 0.06);
    padding: 1.5rem;
    margin-bottom: 2rem;
  }

  .card-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: #1e293b;
    margin-bottom: 1.5rem;
    border-left: 4px solid #facc15;
    padding-left: 1rem;
  }

  .diary-form {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }

  .form-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .form-label {
    font-weight: 600;
    color: #334155;
  }

  .form-input {
    padding: 0.75rem;
    border: 1px solid #cbd5e1;
    border-radius: 12px;
    font-size: 1rem;
    transition: all 0.2s;

    &:focus {
      outline: none;
      border-color: #facc15;
      box-shadow: 0 0 0 3px rgba(250, 204, 21, 0.2);
    }
  }

  .form-input-small {
    padding: 0.5rem;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    font-size: 0.9rem;
    width: 100%;
    width: 110px;

    &:focus {
      outline: none;
      border-color: #facc15;
    }
  }

  .set-row {
    background: #f1f5f9;
    border-radius: 12px;
    padding: 0.75rem;
    margin-bottom: 0.75rem;
  }

  .set-number {
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: #475569;
  }

  .set-fields {
    display: flex;
    gap: 1rem;
    align-items: center;
    flex-wrap: wrap;
  }

  .btn-icon {
    background: none;
    border: none;
    font-size: 1.2rem;
    cursor: pointer;
    color: #ef4444;
    &:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }
  }

  .btn-add-set {
    background: none;
    border: 1px dashed #facc15;
    color: #ca8a04;
    padding: 0.5rem;
    border-radius: 30px;
    cursor: pointer;
    font-size: 0.9rem;
    margin-top: 0.5rem;
    transition: 0.2s;

    &:hover {
      background: #fef9e3;
    }
  }

  .submit-btn {
    margin-top: 0.5rem;
  }

  .history-card {
    .workout-item {
      border-bottom: 1px solid #e2e8f0;
      padding: 1rem 0;
      &:last-child {
        border-bottom: none;
      }
    }

    .workout-header {
      display: flex;
      flex-wrap: wrap;
      align-items: baseline;
      gap: 1rem;
      margin-bottom: 0.5rem;

      .workout-date {
        font-weight: 700;
        color: #0f172a;
        background: #f1f5f9;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
      }
      .workout-exercise {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1e293b;
      }
      .btn-sync {
        margin-left: auto;
        background: #facc15;
        border: none;
        border-radius: 20px;
        padding: 0.25rem 0.75rem;
        font-size: 0.75rem;
        cursor: pointer;
      }
    }

    .workout-sets {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      margin: 0.5rem 0 0.75rem 0;

      .set-detail {
        background: #f8fafc;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
        color: #334155;
      }
    }

    .btn-delete-workout {
      background: none;
      border: none;
      color: #ef4444;
      cursor: pointer;
      font-size: 0.8rem;
      padding: 0;
      margin-top: 0.5rem;
      &:hover {
        text-decoration: underline;
      }
    }
  }

  .loading-state,
  .empty-state {
    text-align: center;
    padding: 2rem;
    color: #64748b;
  }
}
</style>
