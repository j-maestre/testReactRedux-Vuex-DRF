<template>
  <div id="app">
    <TitleMobile />
    <Header />
    <router-view />
    <Toast />
  </div>
</template>

<script>
import Header from "./components/Header";
import TitleMobile from "./components/TitleMobile";
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
    TitleMobile,
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

<style>
.mobile {
  display: none;
}

.desktop {
  display: flex;
}

@media (max-width: 746px) {
  .desktop {
    display: none !important;
  }

  .mobile {
    display: flex !important;
  }
}
</style>
