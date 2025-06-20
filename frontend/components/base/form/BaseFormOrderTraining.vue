<script lang="ts" setup>
import { coaches } from "~/assets/data/moke.data";
const modalsStore = useModalsStore();

const isClosing = ref(false);

function closeListReviews() {
  isClosing.value = true;
}

function handleAnimationEnd() {
  if (isClosing.value) {
    modalsStore.closeModal("orderTraining");
  }
}
const busyDates = ['2025-05-04', '2025-05-07']
const attributes = [
  {
    key: 'busy',
    highlight: {
      backgroundColor: '#ff4d4d',
      borderColor: '#ff0000',
    },
    dates: busyDates,
  },
]
const selectedDate = ref<Date | null>(null)
</script>
<template>
  <div
    class="base-form-order-abonement"
    :class="{ 'base-form-order-abonement_close': isClosing }"
    @animationend="handleAnimationEnd"
  >
    <div class="base-form-order-abonement__wraper">
      <p style="text-align: center; color: aliceblue; font-size: 26px">
        Записаться на персональную тренировку.
      </p>
      <form class="base-form-order-abonement__wraper-form">
        <VDatePicker
          v-model="selectedDate"
          :attributes="attributes"
          :min-date="new Date()"
        />
        <BaseInput
          class="base-form-order-abonement__wraper-form-name"
          placeholder="* Ваше имя"
        />
        <BaseInput
          type="tel"
          class="base-form-order-abonement__wraper-form-mail"
          placeholder="* Ваш телефон"
        />
        <BaseInput
          type="email"
          class="base-form-order-abonement__wraper-form-mail"
          placeholder="* Ваша почта"
        />
        <div class="base-form-order-abonement__wraper-form-select">
          <BaseInputSelect :options="coaches" placeholder="Выберите тренера" />
        </div>
        <BaseRecaptcha />
        <BaseButton
          class="base-form-order-abonement__wraper-form-submit"
          label="Записаться"
          size="lg"
          @click="closeListReviews"
        />
      </form>
      <BaseButtonClose
        right="10px"
        top="10px"
        color="white"
        :size="30"
        @click="closeListReviews"
      />
    </div>
  </div>
</template>

<style scoped lang="scss">
.base-form-order-abonement {
  position: fixed;
  top: 0;
  right: 0;
  width: 100vw;
  height: 100vh;
  background-color: $bg;
  overflow-y: auto;
  box-shadow: -5px 0px 10px rgba(0, 0, 0, 0.1);
  animation: open_reviews 0.5s ease-in-out;

  @include mediaTablet {
    max-width: 700px;
  }
  &_close {
    animation: close_reviews 0.5s ease-in-out;
  }

  &__wraper {
    position: relative;
    height: 100%;
    padding: 70px 20px 20px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    overflow-y: auto;
    @include mediaTablet {
      padding-inline: 30px;
    }
    &-form {
      padding-block: 30px 10px;
      height: 100%;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      &-select {
        flex-grow: 1;
        width: 100%;

        &:deep(.base-input-text-area__input) {
          height: 350px !important;
        }
      }
      &-name {
        width: 100%;
        margin-bottom: 10px;
      }
      &-mail {
        width: 100%;
        margin-bottom: 20px;
      }
      &-stars {
        margin-bottom: 20px;
        margin-inline: auto;
        @include mediaTablet {
          margin-inline: 0;
        }
      }
      &-submit {
        margin-top: 30px;
        width: 100%;
        margin-left: auto;
        transition: all color 0.3s;

        &:hover {
          color: $txt;
        }
      }
    }
  }
}

@keyframes open_reviews {
  from {
    transform: translateX(100%);
  }
  to {
    transform: translateX(0);
  }
}
@keyframes close_reviews {
  from {
    transform: translateX(0);
  }
  to {
    transform: translateX(100%);
  }
}
</style>

<!-- 
<script setup lang="ts">
import { ref } from 'vue'

const name = ref('')
const phone = ref('')
const selectedDate = ref<Date | null>(null)
const success = ref(false)
const error = ref('')

// Пример занятых дат
const busyDates = ['2025-05-04', '2025-05-07']

const attributes = [
  {
    key: 'busy',
    highlight: {
      backgroundColor: '#ff4d4d',
      borderColor: '#ff0000',
    },
    dates: busyDates,
  },
]

async function submitBooking() {
  if (!name.value || !phone.value || !selectedDate.value) {
    error.value = 'Заполните все поля!'
    return
  }

  try {
    await $fetch('/api/bookings', {
      method: 'POST',
      body: {
        name: name.value,
        phone: phone.value,
        date: selectedDate.value,
      },
    })
    success.value = true
    error.value = ''
  } catch (err) {
    error.value = 'Ошибка при отправке.'
  }
}
</script>

<template>
  <section class="booking">
    <h2>Записаться на тренировку</h2>

    <VDatePicker
      v-model="selectedDate"
      :attributes="attributes"
      :min-date="new Date()"
    />

    <div class="form-fields">
      <input v-model="name" type="text" placeholder="Имя" />
      <input v-model="phone" type="tel" placeholder="Телефон" />
      <button @click="submitBooking">Отправить</button>
    </div>

    <p v-if="error" class="error">{{ error }}</p>
    <p v-if="success" class="success">Заявка отправлена!</p>
  </section>
</template>

<style scoped>
.booking {
  max-width: 500px;
  margin: 40px auto;
  text-align: center;
}
.form-fields {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
input {
  padding: 10px;
  font-size: 16px;
  border-radius: 6px;
  border: 1px solid #ccc;
}
button {
  padding: 10px;
  background-color: #07bcc6;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}
.error {
  color: red;
  margin-top: 10px;
}
.success {
  color: green;
  margin-top: 10px;
}
</style> -->
