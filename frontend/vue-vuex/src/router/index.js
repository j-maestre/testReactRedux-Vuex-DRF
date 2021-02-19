import { createWebHistory, createRouter } from "vue-router";
import Home from "@/views/Home.vue";
import Contact from "@/views/Contact.vue";
import Travels from "@/views/Travels.vue";
import Message from "@/views/Message.vue";
import Login from "@/views/Login.vue";
import Register from "@/views/Register.vue";
// Profile
import Profile from "@/views/Profile.vue";
import EditProfile from "@/views/Profile/EditProfile.vue";
import InfoProfile from "@/views/Profile/InfoProfile.vue";

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
    component: Profile,
    children: [
      { path: "/profile", component: InfoProfile },
      { path: "/profile/edit", component: EditProfile },
      { path: "/profile/travels", component: Home },
      { path: "/profile/shippings", component: Home },
      { path: "/profile/settings", component: Home },
    ],
    beforeEnter: [auth],
  },
  {
    path: "/profile/edit",
    name: "EditProfile",
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
