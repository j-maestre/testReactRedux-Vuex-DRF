<template>
  <div class="page">
    <section class="header-mobile">
      <h1 class="font-secundary">¿Cuál es tu email y tu contraseña?</h1>
      <InputText
        class="input-type"
        placeholder="Email"
        v-model="credentials.username"
      />
      <Password
        class="input-type"
        placeholder="Password"
        v-model="credentials.password"
        :feedback="false"
      />
      <div class="check-type">
        <p>Recordarme email</p>
        <Checkbox v-model="credentials.checked" :binary="true" />
      </div>
      <div @click="onSubmit()" class="button-type">
        <a class="button-primary login-button">
          <p>Iniciar sesion</p>
        </a>
      </div>
      <hr class="separador" />
      <div class="login-message">
        <p>No tienes cuenta de <a class="link" href="/">FORGETIT?</a></p>
        <a href="/register" class="button-primary login-button">
          <p>Registrate</p>
        </a>
      </div>
      <div v-if="loading" class="loading">
        <img src="../assets/loading.svg" alt="loading..." />
      </div>
    </section>
    <section class="header-desktop">
      <h1 class="font-secundary">¿Cuál es tu email y tu contraseña?</h1>
      <InputText
        class="input-type"
        placeholder="Email"
        v-model="credentials.username"
      />
      <Password
        class="input-type"
        placeholder="Password"
        v-model="credentials.password"
        :feedback="false"
      />

      <div @click="onSubmit()" class="button-type">
        <a class="button-primary login-button">
          <p>Iniciar sesion</p>
        </a>
      </div>
      <hr class="separador" />

      <div class="login-message">
        <p>No tienes cuenta de <a class="link" href="/">FORGETIT?</a></p>
        <a href="/register" class="button-primary login-button">
          <p>Registrate</p>
        </a>
      </div>
      <div v-if="loading" class="loading">
        <img src="../assets/loading.svg" alt="loading..." />
      </div>
    </section>
  </div>
</template>

<script>
import InputText from "primevue/inputtext";
import Password from "primevue/password";
import Checkbox from "primevue/checkbox";

// import { mapActions } from 'vuex';
import { reactive } from "vue";
import store from "../store/index";
import { computed } from "vue";

export default {
  components: { InputText, Password, Checkbox },
  setup() {
    const credentials = reactive({ username: "", password: "", checked: "" });
    const loading = computed(() => store.state.user.loading);

    function onSubmit() {
      store.dispatch("login", credentials);
    }

    return {
      credentials,
      onSubmit,
      loading,
    };
  },
};
</script>

<style>
.page {
  height: calc(100vh - 100px);
  width: 100%;
}

.page .header-desktop {
  height: calc(100vh - 100px);
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.page .header-desktop .button-type {
  display: flex;
  width: 50%;
  min-width: 500px;
  justify-content: flex-start;
}

.page .header-desktop .input-type {
  padding: 10px !important;
  margin: 10px !important;
  display: flex;
  width: 50%;
  min-width: 500px;
  justify-content: flex-start;
}

.page .header-desktop .separador {
  height: 2px;
  background-color: black;
  border: none;
  width: 50%;
  min-width: 500px;
  margin: 20px 0px;
}

.page .header-desktop .login-button p {
  border-color: black;
  cursor: pointer;
  margin: 10px 0px;
}

.page .header-desktop .login-button p:hover {
  border-color: black;
}

.page .header-desktop .login-message {
  display: flex;
  width: 50%;
  min-width: 500px;
  justify-content: space-evenly;
  align-items: center;
  font-weight: bold;
}

.page .header-desktop .loading {
  position: absolute;
  top: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.39);
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
}

.page .header-mobile {
  display: none;
  flex-direction: column;
}

.page .header-mobile .input-type {
  margin: 10px 30px;
  padding: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.page .header-mobile .check-type {
  margin: 0px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.page .header-mobile .separador {
  height: 2px;
  background-color: black;
  border: none;
  width: 50%;
  margin: 30px auto 20px auto;
}

.page .header-mobile .login-button p {
  border-color: black;
  cursor: pointer;
  margin: 10px 30px;
  text-align: center;
}

.page .header-mobile .login-button p:hover {
  border-color: black;
}

.page .header-mobile .login-message p {
  text-align: center;
  font-weight: bold;
}

@media (max-width: 746px) {
  .page .header-desktop {
    display: none;
  }

  .page .header-mobile {
    display: flex;
  }
}
</style>
