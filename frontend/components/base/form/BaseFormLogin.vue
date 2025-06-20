<script lang="ts" setup>
const email = ref("");
const password = ref("");

const handleLogin = () => {
  console.log("Пытаемся войти с", email.value, password.value);
  // Здесь можно добавить реальную авторизацию через API
};
</script>
<template>
  <ModalBase>
    <div class="login-form">
      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="email">Email</label>
          <BaseInput
            v-model="email"
            type="email"
            placeholder="Введите ваш email"
          />
        </div>

        <div class="form-group">
          <label for="password">Пароль</label>
          <BaseInput
            v-model="password"
            type="password"
            placeholder="Введите пароль"
          />
        </div>
        <BaseButton size="md" label="Войти" class="btn-login" />
      </form>

      <div class="register-link">
        <span>Нет аккаунта?</span>
        <NuxtLink to="/register">Зарегистрироваться</NuxtLink>
      </div>
    </div>
  </ModalBase>
</template>
<style scoped lang="scss">
.login-form {
  background: #f5f5f5;
  text-align: center;


  form {
    padding: 60px 20px 20px;
    display: flex;
    flex-direction: column;
    gap: 20px;

    .form-group {
      display: flex;
      flex-direction: column;
      text-align: left;

      label {
        margin-bottom: 8px;
        font-size: 14px;
        color: #555;
      }

      // input {
      //   padding: 12px 16px;
      //   border: 1px solid #ccc;
      //   border-radius: 12px;
      //   font-size: 16px;
      //   transition: border-color 0.3s;

      //   &:focus {
      //     outline: none;
      //     border-color: #ff5a5f;
      //   }
      // }
    }

    // .btn-login {
    //   padding: 14px;
    //   background: linear-gradient(135deg, #ff5a5f, #f0575b);
    //   border: none;
    //   border-radius: 12px;
    //   color: #fff;
    //   font-size: 16px;
    //   cursor: pointer;
    //   transition: background 0.3s;

    //   &:hover {
    //     background: linear-gradient(135deg, #f0575b, #ff5a5f);
    //   }
    // }
  }

  .register-link {
    margin-top: 20px;
    font-size: 14px;
    color: #777;

    span {
      margin-right: 6px;
    }

    a {
      color: #ff5a5f;
      text-decoration: none;
      font-weight: bold;
      transition: color 0.3s;

      &:hover {
        color: #f0575b;
        text-decoration: underline;
      }
    }
  }
}
</style>
