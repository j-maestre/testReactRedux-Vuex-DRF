<template>
  <div id="app">
    <Header></Header>
    <font-awesome-icon icon="user-secret" />

    <router-view />
  </div>
</template>

<script>
import Header from "./components/Header";

export default {
  name: "App",
  components: {
    Header,
  },
};
</script>

<style></style>
