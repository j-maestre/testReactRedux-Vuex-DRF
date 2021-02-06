import { createApp } from "vue";
import App from "./App.vue";
import store from "./store";
const vue = createApp(App);
vue.use(store);

// Style
import "./assets/style.css";

// Librarias
import router from "./router";
import PrimeVue from "primevue/config";
import "primevue/resources/themes/saga-orange/theme.css";
import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css";
vue.use(router);
vue.use(PrimeVue);

// Componentes
import Password from "primevue/password";
import Dialog from "primevue/dialog";
vue.component("Password", Password);
vue.component("Dialog", Dialog);

vue.mount("#app");
