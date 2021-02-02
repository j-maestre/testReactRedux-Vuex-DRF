import { createApp } from "vue";
import App from "./App.vue";
const vue = createApp(App);

// Style
import "./assets/style.css";

// Librarias
import router from "./router";
import PrimeVue from "primevue/config";
import "primevue/resources/themes/arya-blue/theme.css";
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
