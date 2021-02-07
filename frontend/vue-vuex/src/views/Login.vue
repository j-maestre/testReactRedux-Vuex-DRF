<template>
  <div class="page">
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
  </div>
</template>

<script>
import InputText from "primevue/inputtext";
import Password from "primevue/password";

// import { mapActions } from 'vuex';
import { reactive } from "vue";
import store from "../store/index";
import { computed } from "vue";

export default {
  components: { InputText, Password },
  setup() {
    const credentials = reactive({ username: "", password: "" });
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
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.button-type {
  display: flex;
  width: 50%;
  min-width: 500px;
  justify-content: flex-start;
}

.input-type {
  padding: 10px !important;
  margin: 10px !important;
  display: flex;
  width: 50%;
  min-width: 500px;
  justify-content: flex-start;
}

.separador {
  height: 2px;
  background-color: black;
  border: none;
  width: 50%;
  min-width: 500px;
  margin: 20px 0px;
}

.login-button p {
  border-color: black;
  cursor: pointer;
  margin: 10px 0px;
}

.login-button p:hover {
  border-color: black;
}

.login-message {
  display: flex;
  width: 50%;
  min-width: 500px;
  justify-content: space-evenly;
  align-items: center;
  font-weight: bold;
}

.loading {
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
</style>
