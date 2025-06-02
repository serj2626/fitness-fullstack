<script lang="ts" setup>

</script>
<template>
  <section id="base-form-feedback" class="base-form-feedback">
    <div class="base-form-feedback__wraper container">
      <h4 class="base-form-feedback__wraper-title">Оставьте заявку</h4>
      <p class="base-form-feedback__wraper-text">
        И получите выгодное предложение <BaseDot />
      </p>
      <div class="base-form-feedback__wraper-content">
        <div class="base-form-feedback__wraper-content-info">
          <a class="base-form-feedback__wraper-content-info-tel"
            >8-999-999-99-99
          </a>
          <p class="base-form-feedback__wraper-content-info-adress">
            СПБ, улица Будапештская дом 89
          </p>
        </div>
        <form class="base-form-feedback__wraper-content-form">
          <div class="base-form-feedback__wraper-content-form-input">
            <BaseInput
              type="text"
              placeholder="Ваше имя"
              class="base-form-feedback__wraper-content-form-input-phone"
            />
            <BaseInput
              type="tel"
              placeholder="+7 ( ___ ) ___ - __ - __"
              class="base-form-feedback__wraper-content-form-input-phone"
            />
          </div>
          <label class="base-form-feedback__wraper-content-form-check">
            <input
              type="checkbox"
              class="base-form-feedback__wraper-content-form-check-input"
            />
            <p class="base-form-feedback__wraper-content-form-check-text">
              Согласен на
              <NuxtLink
                class="base-form-feedback__wraper-content-form-check-text-link"
                >обработку своих персональных данных</NuxtLink
              >
            </p>
          </label>
          <button class="base-form-feedback__wraper-content-form-btn">
            Отправить заявку
          </button>
        </form>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
.base-form-feedback {
  padding-block: 100px;

  &__wraper {
    &-title {
      font-weight: 600;
      font-size: 36px;
      color: $accent;
      text-align: center;
      text-transform: uppercase;
      margin-bottom: 30px;
      letter-spacing: 2px;
      opacity: 0.8;
    }
    &-text {
      text-align: center;
      font-weight: 700;
      font-size: 30px;
      color: $white;
      margin-top: 20px;
      text-transform: uppercase;
      letter-spacing: 2px;
    }
    &-content {
      margin-top: 120px;
      display: grid;
      grid-template-columns: 1fr;
      gap: 50px;
      @include mediaCustom(1100px) {
        grid-template-columns: repeat(2, 1fr);
      }

      &-info {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;

        @include mediaTablet {
          align-items: start;
        }
        &-tel {
          color: $accent;
          opacity: 0.8;
        }
        &-adress {
          color: $white;
        }
      }
      &-form {
        display: flex;
        flex-direction: column;
        &-input {
          display: flex;
          gap: 20px;
          margin-bottom: 50px;
          justify-content: space-between;
        }
        &-check {
          display: flex;
          align-items: center;
          gap: 10px;
          margin-bottom: 20px;
          // &-input{
          //   padding: 10px;
          // }
          &-text {
            color: $white;
            &-link {
              color: #ffc551c4;
              cursor: pointer;
            }
          }
        }

        &-btn {
          display: inline-block;
          border-radius: 10px;
          padding: 15px 20px;
          background-color: #ffc551;
          color: $txt;
        }
      }
    }
  }
}
</style>
