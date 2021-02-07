<template>
  <div class="page">
    <section class="mobile">
      <h1 class="font-secundary">Registrate en FORGETIT y gana dinero!!</h1>
      <InputText
        class="input-type"
        placeholder="Username"
        v-model="credentials.username"
      />
      <InputText
        class="input-type"
        placeholder="Email"
        v-model="credentials.email"
      />
      <Password
        class="input-type"
        placeholder="Password"
        v-model="credentials.password"
      ></Password>
      <div @click="onSubmit()" class="button-type">
        <a class="button-primary login-button">
          <p>Registrate</p>
        </a>
      </div>
      <hr class="separador" />
      <div class="login-message">
        <p>Ya tienes cuenta de <a class="link" href="/">FORGETIT?</a></p>
        <a href="/login" class="button-primary login-button">
          <p>Inicia Sesión</p>
        </a>
      </div>
      <div v-if="loading" class="loading">
        <img src="../assets/loading.svg" alt="loading..." />
      </div>
    </section>
    <section class="desktop">
      <h1 class="font-secundary">Registrate en FORGETIT y gana dinero!!</h1>
      <InputText
        class="input-type"
        placeholder="Username"
        v-model="credentials.username"
      />
      <InputText
        class="input-type"
        placeholder="Email"
        v-model="credentials.email"
      />
      <Password
        class="input-type"
        placeholder="Password"
        v-model="value3"
      ></Password>

      <div class="button-type">
        <a class="button-primary login-button">
          <p @click="onSubmit()">Registrate</p>
        </a>
      </div>
      <hr class="separador" />

      <div class="login-message">
        <p>Ya tienes cuenta de <a class="link" href="/">FORGETIT?</a></p>
        <a href="/login" class="button-primary login-button">
          <p>Inicia Sesión</p>
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

// import { mapActions } from 'vuex';
import { reactive } from "vue";
import store from "../store/index";
import { computed } from "vue";

export default {
  components: { InputText, Password },
  setup() {
    const credentials = reactive({
      username: "",
      email: "",
      password: "",
      checked: "",
    });
    const loading = computed(() => store.state.user.loading);

    function onSubmit() {
      store.dispatch("register", credentials);
    }

    return {
      credentials,
      onSubmit,
      loading,
    };
  },
};
</script>

<style scoped>
.page {
  height: calc(100vh - 100px);
  width: 100%;
}

.page .desktop {
  height: calc(100vh - 100px);
  width: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.page .desktop .button-type {
  display: flex;
  width: 50%;
  min-width: 500px;
  justify-content: flex-start;
}

.page .desktop .input-type {
  padding: 10px !important;
  margin: 10px !important;
  display: flex;
  width: 50%;
  min-width: 500px;
  justify-content: flex-start;
}

.page .desktop .separador {
  height: 2px;
  background-color: black;
  border: none;
  width: 50%;
  min-width: 500px;
  margin: 20px 0px;
}

.page .desktop .login-button p {
  border-color: black;
  cursor: pointer;
  margin: 10px 0px;
}

.page .desktop .login-button p:hover {
  border-color: black;
}

.page .desktop .login-message {
  display: flex;
  width: 50%;
  min-width: 500px;
  justify-content: space-evenly;
  align-items: center;
  font-weight: bold;
}

.page .desktop .loading {
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

.page .mobile {
  display: none;
  flex-direction: column;
}

.page .mobile .input-type {
  margin: 10px 30px;
  padding: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.page .mobile .separador {
  height: 2px;
  background-color: black;
  border: none;
  width: 50%;
  margin: 30px auto 20px auto;
}

.page .mobile .login-button p {
  border-color: black;
  cursor: pointer;
  margin: 10px 30px;
  text-align: center;
}

.page .mobile .login-button p:hover {
  border-color: black;
}

.page .mobile .login-message p {
  text-align: center;
  font-weight: bold;
}
</style>
