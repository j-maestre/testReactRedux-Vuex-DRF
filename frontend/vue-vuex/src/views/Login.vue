<template>
  <v-app>
    <v-content>
      <Password v-model="value" />
    </v-content>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      value: "",
    };
  },
};
</script>

<style>
#nav {
}
</style>
