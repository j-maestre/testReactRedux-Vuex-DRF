<template>
  <div class="header">
    <!-- Version movil -->
    <section class="header-mobile">
      <router-link active-class="active" to="/travels">
        <i class="fas fa-car"></i>
      </router-link>
      <router-link active-class="active" to="/">
        <i class="fas fa-search"></i>
      </router-link>
      <router-link active-class="active" to="/message">
        <i class="fas fa-sms"></i>
      </router-link>
    </section>

    <!-- Version escritorio -->
    <section class="header-desktop">
      <div class="header-logo">
        <img src="../assets/logo.png" alt="" />
      </div>
      <nav class="header-menu">
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
        <router-link active-class="active" class="header-button" to="/login">
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
.header-mobile {
  display: none;
  position: fixed;
  bottom: 0;
  width: 100vw;
  height: 60px;
  justify-content: space-around;
  align-items: flex-end;
  border-top: 2px solid black;
}

.header-mobile i {
  color: black;
  font-size: 25px;
}

.header-mobile a {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
  text-decoration: none;
}

.header-mobile a.active {
  background-color: black;
  height: 115%;
  width: 120%;
}
.header-mobile a.active i {
  color: #faff8a;
  font-size: 35px;
}

.header-desktop {
  background-color: black;
  width: 100%;
  height: 100px;
  display: flex;
  justify-content: space-between;
}

.header-desktop .header-logo {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 150px;
}

.header-desktop .header-logo img {
  width: 150px;
}

.header-desktop .header-menu {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.header-desktop .header-menu a {
  padding: 20px;
  display: flex;
  height: 100%;
  justify-content: center;
  align-items: center;
  text-decoration: none;
  color: white;
}

.header-desktop .header-menu a p {
  margin-left: 7px;
}

.header-desktop .header-menu a i {
  font-size: 20px;
}

.header-desktop .header-menu a:hover,
.header-desktop .header-menu a.active {
  color: #faff8a;
}

.header-desktop .header-button p {
  border: 2px solid white;
  padding: 10px;
  font-weight: bold;
}

.header-desktop .header-button p:hover,
.header-desktop a.header-button.active p {
  color: black;
  background-color: #faff8a;
  border-color: #faff8a;
}

@media (max-width: 886px) {
  .header-desktop .header-logo {
    margin-left: 14px;
  }

  .header-desktop .header-logo {
    margin-left: 14px;
  }
}

@media (max-width: 746px) {
  .header-desktop {
    display: none;
  }

  .header-mobile {
    display: flex;
  }
}
</style>
