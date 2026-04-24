<script lang="ts" setup>
import { api } from "~/api";

const { error: errorNotify, success: successNotify } = useNotify();

const store = useContactsStore();
const { contactsList } = storeToRefs(store);

const { $api } = useNuxtApp();

const { formData } = useForm({
  name: { value: "", error: "", required: true },
  phone: { value: "", error: "", required: true },
  captcha: { value: "", error: "", required: true },
});

const agree = reactive({
  value: false,
  error: "",
});

const loading = ref(false);
const error = ref<string | null>(null);

async function submitForm() {
  loading.value = true;
  const payload = {
    name: formData.name.value,
    phone: formData.phone.value,
  };

  console.log("Данные к отправке:", payload);
  clearForm(formData);

  try {
    const res = await $api(api.contacts.feedback, {
      method: "POST",
      body: payload,
    });
    console.log(res);
    successNotify("Заявка отправлена");
  } catch (e) {
    errorNotify(
      e.statusCode == 429 ? "Превышен лимит запросов" : "Произошла ошибка",
    );
  } finally {
    loading.value = false;
  }
}
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
          <div style="display: flex; align-items: center; gap: 10px">
            <a
              v-for="phone in contactsList?.phone"
              :key="phone"
              :href="`tel:${phone}`"
              class="base-form-feedback__wraper-content-info-tel"
            >
              {{ phone || "8-999-999-99-99" }}
            </a>
          </div>

          <p class="base-form-feedback__wraper-content-info-address">
            {{ contactsList?.address || "СПБ, улица Будапештская дом 89" }}
          </p>
        </div>
        <form
          class="base-form-feedback__wraper-content-form"
          @submit.prevent="submitForm"
        >
          <div class="base-form-feedback__wraper-content-form-input">
            <BaseInput
              v-model:input-value="formData.name.value"
              v-model:error="formData.name.error"
              type="text"
              placeholder="Ваше имя"
              class="base-form-feedback__wraper-content-form-input-name"
            />
            <BaseInput
              v-model:input-value="formData.phone.value"
              v-model:error="formData.phone.error"
              type="tel"
              placeholder="+7 ( ___ ) ___ - __ - __"
              class="base-form-feedback__wraper-content-form-input-phone"
            />
          </div>
          <BaseInputCheckbox
            v-model="agree.value"
            :error="agree.error"
            class="base-form-feedback__wraper-content-form-check"
          />
          <BaseButton
            :disabled="loading"
            label="Отправить заявку"
            size="lg"
            style="width: 100%"
          />
        </form>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
.base-form-feedback {
  padding-block: 100px;
  background-color: $bg;
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
      @include mediaCustom(800px) {
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
        &-address {
          color: $white;
        }
      }
      &-form {
        display: flex;
        flex-direction: column;
        &-input {
          display: flex;
          gap: 10px;
          margin-bottom: 50px;
          &-phone,
          &-name {
            width: 100%;
          }
        }
        // &-check {
        //   display: flex;
        //   align-items: center;
        //   gap: 10px;
        //   margin-bottom: 20px;
        //   // &-input{
        //   //   padding: 10px;
        //   // }
        //   &-text {
        //     color: $white;
        //     &-link {
        //       color: #ffc551c4;
        //       cursor: pointer;
        //     }
        //   }
        // }
        &-check {
          margin-block: 20px;
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
