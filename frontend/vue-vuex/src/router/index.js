import { createWebHistory, createRouter } from "vue-router";
import Home from "@/views/Home.vue";
import About from "@/views/About.vue";
import Travels from "@/views/Travels.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/travels",
    name: "Travels",
    component: Travels
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;