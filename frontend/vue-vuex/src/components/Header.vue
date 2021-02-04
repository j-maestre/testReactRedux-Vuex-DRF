<template>
  <div class="header">
    <section class="header-mobile">
      <router-link to="/">Home</router-link>
      <router-link to="/about">Search</router-link>
      <router-link to="/travels">Travels</router-link>
      <router-link to="/login">Login</router-link>
    </section>
    <section class="header-desktop">
      <div class="header-logo">
        <img src="../assets/logo.png" alt="" />
      </div>
      <nav class="header-menu">
        <router-link to="/">Home</router-link>
        <router-link to="/about">Search</router-link>
        <router-link to="/travels">Travels</router-link>
        <router-link to="/login">Login</router-link>
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
}

.header-desktop {
  background-color: black;
  width: 100%;
  height: 100px;
  display: flex;
}

.header-logo {
  height: 100%;
  display: flex;
  justify-content: center;
}

.header-logo img {
  width: 150px;
}
</style>
