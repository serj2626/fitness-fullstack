<script lang="ts" setup>
import { coaches } from "~/assets/data/moke.data";
const modalsStore = useModalsStore();

const isClosing = ref(false);

function closeListReviews() {
  isClosing.value = true;
}

function handleAnimationEnd() {
  if (isClosing.value) {
    modalsStore.closeModal("orderAbonement");
  }
}
</script>
<template>
  <div
    class="base-form-order-abonement"
    :class="{ 'base-form-order-abonement_close': isClosing }"
    @animationend="handleAnimationEnd"
  >
    <div class="base-form-order-abonement__wraper">
      <p style="text-align: center; color: aliceblue; font-size: 26px">
        Забронировать абонемент.
      </p>
      <form class="base-form-order-abonement__wraper-form">
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
