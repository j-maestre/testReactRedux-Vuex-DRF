import { createApp } from "vue";
import App from "@/App.vue";
import store from "@/store";
const vue = createApp(App);
vue.use(store);

// Style
import "primevue/resources/themes/saga-orange/theme.css";
import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css";
import "@/assets/style.css";

// Librarias
import router from "@/router";
import PrimeVue from "primevue/config";
import ToastService from "primevue/toastservice";
vue.use(router);
vue.use(PrimeVue);
vue.use(ToastService);
vue.mount("#app");
