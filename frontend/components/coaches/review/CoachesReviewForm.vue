<script lang="ts" setup>
const modalsStore = useModalsStore();

const isClosing = ref(false);

function closeListReviews() {
  isClosing.value = true;
}

function handleAnimationEnd() {
  if (isClosing.value) {
    modalsStore.closeModal("reviewCoachForm");
  }
}
</script>
<template>
  <div
    class="coaches-review-form"
    :class="{ 'coaches-review-form_close': isClosing }"
    @animationend="handleAnimationEnd"
  >
    <div class="coaches-review-form__wraper">
      <p style="text-align: center; color: aliceblue; font-size: 26px">
        Оставьте свой комментарий
      </p>
      <form class="coaches-review-form__wraper-form">
        <RatingComponent class="coaches-review-form__wraper-form-stars" />
        <BaseInput
          class="coaches-review-form__wraper-form-name"
          placeholder="Ваше имя"
        />
        <BaseInput
          class="coaches-review-form__wraper-form-mail"
          placeholder="Ваша почта"
        />
        <div class="coaches-review-form__wraper-form-textarea">
          <BaseInputTextArea placeholder="Введите ваш отзыв." />
        </div>
        <BaseRecaptcha />
        <BaseButton
          class="coaches-review-form__wraper-form-submit"
          label="Отправить"
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
.coaches-review-form {
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
      &-textarea {
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
