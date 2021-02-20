<template>
  <div id="app">
    <TitleMobile />
    <Header />
    <div class="mobile">
      <br />
      <br />
      <br />
    </div>
    <!-- {{ state }} -->
    <router-view />
    <Toast />
  </div>
</template>

<script>
import Header from "@/components/Header";
import TitleMobile from "@/components/TitleMobile";
import Toast from "primevue/toast";
import { onMounted, computed } from "vue";
import { useStore } from "vuex";

export default {
  name: "App",
  setup() {
    const store = useStore();
    const state_msg = computed(() => store.state.msg);
    const state = computed(() => store.state);

    onMounted(async () => {
      // Comprobamos que el token es valido y obtenemos los datos del usuario logeado.
      console.log("Is logged?:", await store.dispatch("user/checkout"));
    });

    return {
      store,
      state_msg,
      state,
    };
  },
  watch: {
    state_msg(value) {
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
  components: {
    Header,
    Toast,
    TitleMobile,
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
