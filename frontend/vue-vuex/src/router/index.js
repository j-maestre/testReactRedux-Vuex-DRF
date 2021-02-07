import { createWebHistory, createRouter } from "vue-router";
import Search from "@/views/Search.vue";
import Contact from "@/views/Contact.vue";
import Travels from "@/views/Travels.vue";
import Message from "@/views/Message.vue";
import Login from "@/views/Login.vue";
import Register from "@/views/Register.vue";

const routes = [
  {
    path: "/",
    name: "Search",
    component: Search,
  },
  {
    path: "/message",
    name: "Message",
    component: Message,
  },
  {
    path: "/travels",
    name: "Travels",
    component: Travels,
  },
  {
    path: "/contact",
    name: "Contact",
    component: Contact,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
