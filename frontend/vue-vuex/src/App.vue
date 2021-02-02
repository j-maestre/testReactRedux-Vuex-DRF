<template>
  <div id="app">
    <div class="router">
      <router-link to="/">Home</router-link>
      <router-link to="/about">Search</router-link>
      <router-link to="/travels">Travels</router-link>
      <router-link to="/login">Login</router-link>
    </div>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
  components: {},
};
</script>

<style>
#nav {
}
</style>
