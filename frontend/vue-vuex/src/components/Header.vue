<template>
  <div class="header">
    <!-- Version movil -->
    <section class="mobile">
      <router-link active-class="active" to="/travels">
        <i class="fas fa-car"></i>
      </router-link>
      <router-link active-class="active" to="/">
        <i class="fas fa-home"></i>
      </router-link>
      <router-link active-class="active" to="/message">
        <i class="fas fa-sms"></i>
      </router-link>
    </section>

    <!-- Version escritorio -->
    <section class="desktop">
      <div class="logo">
        <h2>FORGETIT</h2>
      </div>
      <nav class="menu">
        <router-link active-class="active" to="/">
          <i class="fas fa-search"></i>
          <p>Buscar</p>
        </router-link>
        <router-link active-class="active" to="/travels">
          <i class="far fa-plus-square"></i>
          <p>Nuevo viaje</p>
        </router-link>
        <router-link active-class="active" to="/contact">
          <i class="far fa-address-book"></i>
          <p>Contact</p>
        </router-link>
        <router-link
          v-if="!currentUser.username"
          active-class="active"
          class="button-primary"
          to="/login"
        >
          <p>Iniciar Sesion</p>
        </router-link>
        <div v-if="currentUser.username" class="user-logged">
          <img src="https://thispersondoesnotexist.com/image" alt="profile" />
          <strong>@{{ currentUser.username }}</strong>
          <ul>
            <router-link class="li" active-class="active" to="/profile">
              <i class="fas fa-user"></i>
              <p>Perfil</p>
            </router-link>
            <router-link class="li" active-class="active" to="/travels">
              <i class="fas fa-user"></i>
              <p>Mis viajes</p>
            </router-link>
            <router-link class="li" active-class="active" to="/shipping">
              <i class="fas fa-user"></i>
              <p>Mis envios</p>
            </router-link>
            <router-link class="li" active-class="active" to="/settings">
              <i class="fas fa-user"></i>
              <p>Ajustes</p>
            </router-link>
            <li @click="logout()" class="li" active-class="active" to="/logout">
              <i class="fas fa-user"></i>
              <p>Cerrar sesion</p>
            </li>
          </ul>
        </div>
      </nav>
    </section>
  </div>
</template>

<script>
import { computed } from "vue";
import { useStore } from "vuex";

export default {
  name: "Header",
  setup() {
    const store = useStore();
    const currentUser = computed(() => store.state.user.user);

    const logout = () => store.dispatch("user/logout");

    return {
      logout,
      currentUser,
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.mobile {
  display: none;
  position: fixed;
  bottom: 0;
  width: 100vw;
  height: 60px;
  justify-content: space-around;
  align-items: flex-end;
  border-top: 2px solid black;
  z-index: 1;
  background: white;
}

.mobile i {
  color: black;
  font-size: 25px;
}

.mobile a {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
  text-decoration: none;
}

.mobile a.active {
  background-color: black;
  height: 115%;
  width: 120%;
}
.mobile a.active i {
  color: #faff8a;
  font-size: 35px;
}

.desktop {
  background-color: black;
  width: 100%;
  height: 100px;
  display: flex;
  justify-content: space-between;
}

.desktop .logo {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: "Roboto Condensed", sans-serif;
  margin-left: 150px;
  color: white;
  font-size: 30px;
}

.desktop .menu {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.desktop .menu a {
  padding: 20px;
  display: flex;
  height: 100%;
  justify-content: center;
  align-items: center;
  text-decoration: none;
  color: white;
}

.desktop .menu a p {
  margin-left: 7px;
}

.desktop .menu a i {
  font-size: 20px;
}

.desktop .menu a:hover,
.desktop .menu a.active {
  color: #faff8a;
}

.desktop .menu .user-logged {
  color: white;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  width: 170px;
  padding: 10px 30px 10px 0px;
  margin: 10px 20px;
  cursor: pointer;
  position: relative;
}

.desktop .menu .user-logged strong {
  margin-left: 10px;
}

.desktop .menu .user-logged:hover strong {
  color: #faff8a;
}

.desktop .menu .user-logged img {
  width: 60px;
  height: 60px;
  object-fit: cover;
  border-radius: 100%;
}

.desktop .menu .user-logged ul {
  position: absolute;
  top: 64px;
  right: -30px;
  background: black;
  list-style: none;
  width: 215px;
  padding: 0px;
  display: flex;
  justify-content: center;
  flex-direction: column;
  padding: 0px 25px 7px 25px;
  display: none;
}

.desktop .menu .user-logged:hover ul,
.desktop .menu .user-logged ul:hover {
  display: flex;
}

.desktop .menu .user-logged ul .li {
  margin: 17px 0px;
  padding: 0px;
  display: flex;
  justify-content: flex-start;
}

.desktop .menu .user-logged ul .li p {
  margin: 0;
  margin-left: 10px;
}

.desktop .menu .user-logged ul .li:hover {
  color: #faff8a;
}

@media (max-width: 886px) {
  .desktop .logo {
    margin-left: 14px;
  }

  .desktop .logo {
    margin-left: 14px;
  }
}
</style>
