<script setup lang="ts">
import { ref } from "vue";

const user = ref({
  id: "user-fit-789",
  avatar: "https://randomuser.me/api/portraits/women/44.jpg",
  name: "Анна Смирнова",
  membership: "Премиум членство",
  isPremium: true,
  joinDate: "Участник с января 2022",
  bio: "Фитнес-энтузиаст | Люблю кроссфит и йогу",
  stats: {
    weight: 68,
    height: 172,
    workouts: 124,
    achievements: 8,
  },
  goals: {
    weight: 62,
    workoutsPerWeek: 5,
  },
  recentActivities: [
    { date: "Сегодня", activity: "Кроссфит", calories: 420 },
    { date: "Вчера", activity: "Йога", calories: 280 },
    { date: "2 дня назад", activity: "Бег", calories: 350 },
  ],
});

const isEditing = ref(false);
const editForm = ref({
  name: user.value.name,
  bio: user.value.bio,
});

const toggleEdit = () => {
  isEditing.value = !isEditing.value;
};

const saveChanges = () => {
  user.value.name = editForm.value.name;
  user.value.bio = editForm.value.bio;
  isEditing.value = false;
};

const cancelEditing = () => {
  editForm.value = {
    name: user.value.name,
    bio: user.value.bio,
  };
  isEditing.value = false;
};
</script>
<template>
  <div class="container">
    <div class="user-profile">

      <!-- Основная информация -->
      <div class="profile-content">
        <!-- Аватар и кнопка редактирования -->
        <div class="profile-header">
          <div class="avatar-container">
            <img :src="user.avatar" :alt="user.name" class="avatar" />
            <span v-if="user.isPremium" class="premium-badge">PREMIUM</span>
          </div>

          <button @click="toggleEdit" class="edit-button">
            <FiEdit v-if="!isEditing" />
            <template v-else>
              <FiCheck @click.stop="saveChanges" />
              <FiX @click.stop="cancelEditing" />
            </template>
          </button>
        </div>

        <!-- Имя и статус -->
        <div class="user-info">
          <h1 class="user-name">{{ user.name }}</h1>
          <p class="user-membership">{{ user.membership }}</p>
        </div>

        <!-- Статистика -->
        <div class="stats-grid">
          <div class="stat-card">
            <FiActivity class="stat-icon" />
            <div>
              <p class="stat-value">{{ user.stats.workouts }}</p>
              <p class="stat-label">Тренировки</p>
            </div>
          </div>

          <div class="stat-card">
            <FiAward class="stat-icon" />
            <div>
              <p class="stat-value">{{ user.stats.achievements }}</p>
              <p class="stat-label">Достижения</p>
            </div>
          </div>

          <div class="stat-card">
            <div>
              <p class="stat-value">{{ user.stats.weight }} кг</p>
              <p class="stat-label">Вес</p>
            </div>
          </div>

          <div class="stat-card">
            <div>
              <p class="stat-value">{{ user.stats.height }} см</p>
              <p class="stat-label">Рост</p>
            </div>
          </div>
        </div>

        <!-- Цели -->
        <div class="goals-section">
          <h2 class="section-title">Мои цели</h2>
          <div class="goals-grid">
            <div class="goal-card">
              <p class="goal-label">Целевой вес</p>
              <p class="goal-value">{{ user.goals.weight }} кг</p>
            </div>
            <div class="goal-card">
              <p class="goal-label">Тренировок в неделю</p>
              <p class="goal-value">{{ user.goals.workoutsPerWeek }}</p>
            </div>
          </div>
        </div>

        <!-- Последние активности -->
        <div class="activities-section">
          <h2 class="section-title">Последние тренировки</h2>
          <div class="activities-list">
            <div
              v-for="(activity, index) in user.recentActivities"
              :key="index"
              class="activity-item"
            >
              <div class="activity-date">{{ activity.date }}</div>
              <div class="activity-name">{{ activity.activity }}</div>
              <div class="activity-calories">{{ activity.calories }} ккал</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss">
.user-profile {
  margin: 100px auto;
  color: $white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.profile-content {
  padding: 0 24px 24px;
}

.profile-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 16px;
}

.avatar-container {
  position: relative;
  margin-top: 60px;
}

.avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  border: 4px solid $bg;
  object-fit: cover;
}

.premium-badge {
  position: absolute;
  bottom: 10px;
  right: -10px;
  background: $accent;
  color: $txt;
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: bold;
}

.edit-button {
  background: $accent;
  color: $txt;
  border: none;
  border-radius: 50%;
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  margin-top: 16px;
}

.user-info {
  margin-bottom: 24px;
}

.user-name {
  font-size: 24px;
  margin: 0;
  color: $white;
}

.user-membership {
  color: $accent;
  margin: 4px 0 0;
  font-weight: 500;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-bottom: 24px;
}

.stat-card {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 12px;
  display: flex;
  align-items: center;
}

.stat-icon {
  margin-right: 8px;
  color: $accent;
  font-size: 20px;
}

.stat-value {
  font-size: 18px;
  font-weight: bold;
  margin: 0;
}

.stat-label {
  font-size: 12px;
  opacity: 0.8;
  margin: 0;
}

.section-title {
  font-size: 20px;
  margin: 0 0 16px;
  color: $accent;
}

.goals-section {
  margin-bottom: 24px;
}

.goals-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.goal-card {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 16px;
}

.goal-label {
  font-size: 14px;
  opacity: 0.8;
  margin: 0 0 4px;
}

.goal-value {
  font-size: 18px;
  font-weight: bold;
  margin: 0;
  color: $accent;
}

.activities-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.activity-item {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 12px 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.activity-date {
  font-size: 14px;
  opacity: 0.8;
  min-width: 80px;
}

.activity-name {
  flex-grow: 1;
  padding: 0 16px;
  font-weight: 500;
}

.activity-calories {
  color: $accent;
  font-weight: bold;
}

@media (max-width: $tablet) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .goals-grid {
    grid-template-columns: 1fr;
  }

  .profile-banner {
    height: 150px;
  }

  .avatar {
    width: 100px;
    height: 100px;
  }
}

@media (max-width: $mobile) {
  .stats-grid {
    grid-template-columns: 1fr;
  }

  .profile-content {
    padding: 0 16px 16px;
  }
}
</style>
