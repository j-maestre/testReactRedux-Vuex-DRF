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
        <router-link active-class="active" class="button-primary" to="/login">
          <p>Iniciar Sesion</p>
        </router-link>
      </nav>
    </section>
  </div>
</template>

<script>
export default {
  name: "Header",
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

@media (max-width: 886px) {
  .desktop .logo {
    margin-left: 14px;
  }

  .desktop .logo {
    margin-left: 14px;
  }
}
</style>
