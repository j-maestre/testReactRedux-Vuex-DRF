import { createWebHistory, createRouter } from "vue-router";
import Home from "@/views/Home.vue";
import Contact from "@/views/Contact.vue";
import Travels from "@/views/Travels.vue";
import Message from "@/views/Message.vue";
import Login from "@/views/Login.vue";
import Register from "@/views/Register.vue";

// VueRouteMiddleware (Utilizado mas para organizacion)
import { auth, noAuth } from "@/router/middleware/auth";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/profile",
    name: "Profile",
    component: Home,
    beforeEnter: [auth],
  },
  {
    path: "/message",
    name: "Message",
    component: Message,
    beforeEnter: [auth],
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
    beforeEnter: [noAuth],
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
    beforeEnter: [noAuth],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
