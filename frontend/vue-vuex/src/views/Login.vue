<template>
  <div class="page">
    <section class="mobile">
      <h1 class="font-secundary">¿Cuál es tu email y tu contraseña?</h1>
      <InputText class="input-type" placeholder="Email" v-model="email" />
      <Password
        class="input-type"
        placeholder="Password"
        v-model="password"
        :feedback="false"
      />
      <div class="check-type">
        <p>Recordarme email</p>
        <Checkbox v-model="checked" :binary="true" />
      </div>
      <div @click="onSubmit()" class="button-type">
        <a class="button-primary button">
          <p>Iniciar sesion</p>
        </a>
      </div>
      <hr class="separador" />
      <div class="message">
        <p>No tienes cuenta de <a class="link" href="/">FORGETIT?</a></p>
        <a href="/register" class="button-primary button">
          <p>Registrate</p>
        </a>
      </div>
      <div v-if="loading" class="loading">
        <img src="../assets/loading.svg" alt="loading..." />
      </div>
    </section>
    <section class="desktop">
      <h1 class="font-secundary">¿Cuál es tu email y tu contraseña?</h1>
      <InputText class="input-type" placeholder="Email" v-model="email" />
      <Password
        class="input-type"
        placeholder="Password"
        v-model="password"
        :feedback="false"
      />

      <div class="button-type">
        <a class="button-primary button">
          <p @click="onSubmit()">Iniciar sesion</p>
        </a>
      </div>
      <hr class="separador" />

      <div class="message">
        <p>No tienes cuenta de <a class="link" href="/">FORGETIT?</a></p>
        <a href="/register" class="button-primary button">
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

import { mapActions } from "vuex";

export default {
  components: { InputText, Password, Checkbox },
  data() {
    return {
      email: "",
      password: "",
      checked: true,
      loading: false,
      routerFrom: "",
    };
  },
  methods: {
    ...mapActions({
      login: "user/login",
    }),
    async onSubmit() {
      let response = await this.login({
        email: this.email,
        checked: this.checked,
        password: this.password,
      });

      // Si el login es success.
      response ? this.$router.push({ name: "Home" }) : "";
    },
  },
  beforeRouteEnter(to, from, next) {
    // console.log(from.name);
    // this.routerFrom = from.name;
    next();
  },
};
</script>

<style>
.desktop .input-type {
  padding: 10px !important;
  margin: 10px !important;
  display: flex;
  width: 50%;
  min-width: 500px;
  justify-content: flex-start;
}

.mobile .input-type {
  margin: 10px 30px;
  padding: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
<style scoped>
.page {
  width: 100%;
}

.page .desktop {
  height: calc(100vh - 100px);
  width: 100%;
  display: flex;
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

.page .desktop .button p {
  border-color: black;
  cursor: pointer;
  margin: 10px 0px;
}

.page .desktop .button p:hover {
  border-color: black;
}

.page .desktop .message {
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
  padding-bottom: 70px;
}

.page .mobile .input-type {
  margin: 10px 30px;
  padding: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.page .mobile .check-type {
  margin: 0px 30px;
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

.page .mobile .button p {
  border-color: black;
  cursor: pointer;
  margin: 10px 30px;
  text-align: center;
}

.page .mobile .button p:hover {
  border-color: black;
}

.page .mobile .message p {
  text-align: center;
  font-weight: bold;
}

@media (max-width: 746px) {
  .page .desktop {
    display: none;
  }

  .page .mobile {
    display: flex;
  }
}
</style>
