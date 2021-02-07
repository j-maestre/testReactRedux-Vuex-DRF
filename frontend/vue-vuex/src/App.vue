<template>
  <div id="app">
    <Header></Header>
    <router-view />
    <Toast />
    <Toast position="top-left" group="tl" />
    <Toast position="bottom-left" group="bl" />
    <Toast position="bottom-right" group="br" />
  </div>
</template>

<script>
import Header from "./components/Header";
import Toast from "primevue/toast";
import { computed } from "vue";
import store from "./store/index";

export default {
  name: "App",
  setup() {
    const store_msg = computed(() => store.state.msg);

    return {
      store_msg,
    };
  },
  components: {
    Header,
    Toast,
  },
  watch: {
    store_msg: function(value) {
      // Si es true, mensaje success
      let type = value.type ? "success" : "error";

      // Pintamos el toaster
      this.$toast.add({
        severity: type,
        summary: value.title ? value.title : "",
        detail: value.details ? value.details : "",
        life: 3000,
      });
    },
  },
};
</script>
