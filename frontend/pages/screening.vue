<script lang="ts" setup>
// Тип вопроса
interface QuestionnaireItem {
  id: string;
  text: string;
  defaultAnswer?: boolean;
}

// Список вопросов (можно вынести в отдельный файл или получить с API)
const questions: QuestionnaireItem[] = [
  { id: "weight_loss", text: "Цель — похудение", defaultAnswer: false },
  {
    id: "muscle_gain",
    text: "Хочу нарастить мышечную массу",
    defaultAnswer: false,
  },
  { id: "cardio", text: "Предпочитаю кардиотренировки", defaultAnswer: false },
  { id: "trainer_help", text: "Нужна помощь тренера", defaultAnswer: false },
  {
    id: "injuries",
    text: "Были травмы или ограничения по здоровью",
    defaultAnswer: false,
  },
  {
    id: "home_training",
    text: "Планирую заниматься дома",
    defaultAnswer: false,
  },
  {
    id: "has_membership",
    text: "Уже есть абонемент в клуб",
    defaultAnswer: false,
  },
  {
    id: "group_lessons",
    text: "Интересуют групповые занятия",
    defaultAnswer: false,
  },
  {
    id: "morning_workouts",
    text: "Предпочитаю утренние тренировки",
    defaultAnswer: false,
  },
];

// Состояния
const answers = reactive<Record<string, boolean>>({});
const isSaving = ref(false);
const showSuccessMessage = ref(false);

// Инициализация ответов (по умолчанию или загруженные с сервера)
function initAnswers() {
  for (const q of questions) {
    answers[q.id] = q.defaultAnswer ?? false;
  }
}

// Загрузка сохранённых данных (имитация API)
async function loadSavedAnswers() {
  try {
    // Здесь запрос к API, например: const { data } = await $fetch('/api/user/questionnaire')
    // Пока имитируем задержку и ничего не загружаем
    await new Promise((resolve) => setTimeout(resolve, 300));
    // Если бы были данные, перезаписали бы answers
    // Object.assign(answers, data)
  } catch (error) {
    console.error("Ошибка загрузки анкеты:", error);
  }
}

// Сохранение (отправка на сервер)
async function saveQuestionnaire() {
  if (isSaving.value) return;
  isSaving.value = true;

  try {
    // Подготовка данных для отправки
    const payload = Object.entries(answers).map(([key, value]) => ({
      questionId: key,
      answer: value,
    }));

    // Отправка на API
    // await $fetch('/api/user/questionnaire', { method: 'POST', body: payload })
    console.log("Сохранённые ответы:", payload);

    // Показываем сообщение об успехе
    showSuccessMessage.value = true;
    setTimeout(() => {
      showSuccessMessage.value = false;
    }, 3000);
  } catch (error) {
    console.error("Ошибка сохранения:", error);
    alert("Не удалось сохранить анкету. Попробуйте позже.");
  } finally {
    isSaving.value = false;
  }
}

// Загрузка данных при монтировании
onMounted(async () => {
  initAnswers();
  await loadSavedAnswers();
});
</script>
<template>
  <div class="questionnaire-page">
    <div class="questionnaire-container">
      <h1 class="questionnaire-title">Анкета пользователя</h1>
      <p class="questionnaire-subtitle">
        Расскажите о своих предпочтениях и целях, чтобы мы могли подобрать
        лучшие тренировки
      </p>

      <form class="questionnaire-form" @submit.prevent="saveQuestionnaire">
        <div
          v-for="question in questions"
          :key="question.id"
          class="question-item"
        >
          <label class="question-label">{{ question.text }}</label>
          <BaseToggle v-model="answers[question.id]" :disabled="isSaving">
            <span class="toggle-text">{{ answers[question.id] ? "Да" : "Нет" }}</span>
          </BaseToggle>
        </div>

        <div class="form-actions">
          <BaseButton
            type="submit"
            size="lg"
            :loading="isSaving"
            :disabled="isSaving"
            label=" Сохранить ответы"
          />
        </div>

        <Transition name="fade">
          <div v-if="showSuccessMessage" class="success-message">
            ✅ Анкета успешно сохранена
          </div>
        </Transition>
      </form>
    </div>
  </div>
</template>

<style scoped lang="scss">
.questionnaire-page {
  padding: 150px 200px 100px;
}

.questionnaire-container {
  max-width: 800px;
  margin: 0 auto;
  background: white;
  border-radius: 24px;
  box-shadow:
    0 10px 25px -5px rgba(0, 0, 0, 0.05),
    0 8px 10px -6px rgba(0, 0, 0, 0.02);
  padding: 2rem;
}

.questionnaire-title {
  font-size: 1.875rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.5rem;
  text-align: center;
}

.questionnaire-subtitle {
  text-align: center;
  color: #475569;
  margin-bottom: 2rem;
  font-size: 0.95rem;
}

.questionnaire-form {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.question-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 0;
  border-bottom: 1px solid #e2e8f0;

  &:last-of-type {
    border-bottom: none;
  }
}

.question-label {
  font-size: 1rem;
  font-weight: 500;
  color: #0f172a;
  flex: 1;
  padding-right: 1rem;
}

.form-actions {
  margin-top: 1.5rem;
  display: flex;
  justify-content: center;
}

.success-message {
  margin-top: 1rem;
  text-align: center;
  padding: 0.75rem;
  background-color: #dcfce7;
  color: #15803d;
  border-radius: 12px;
  font-weight: 500;
}

// Анимация появления сообщения
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

// Адаптив для мобильных устройств
@media (max-width: 640px) {
  .questionnaire-container {
    padding: 1.5rem;
  }

  .question-item {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.75rem;
  }

  .question-label {
    padding-right: 0;
  }
}
</style>
