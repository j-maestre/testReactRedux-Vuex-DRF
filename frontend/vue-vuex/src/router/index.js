import { createWebHistory, createRouter } from "vue-router";

// MiddleWares
import { auth, noAuth } from "@/router/middleware/auth";

// Carga de modulos
const lazyLoad = (view) => import(`@/views/${view}.vue`);

// Rutas
const routes = [
  {
    path: "/",
    name: "Home",
    component: lazyLoad("Home"),
  },
  {
    path: "/profile",
    name: "Profile",
    component: lazyLoad("Profile"),
    children: [
      { path: "/profile", component: lazyLoad("Profile/InfoProfile") },
      { path: "/profile/edit", component: lazyLoad("Profile/EditProfile") },
      { path: "/profile/travels", component: lazyLoad("Home") },
      { path: "/profile/shippings", component: lazyLoad("Home") },
      { path: "/profile/settings", component: lazyLoad("Home") },
    ],
    beforeEnter: [auth],
  },
  {
    path: "/message",
    name: "Message",
    component:  lazyLoad("Message"),
    beforeEnter: [auth],
  },
  {
    path: "/travels",
    name: "Travels",
    component: lazyLoad("Travels"),
  },
  {
    path: "/contact",
    name: "Contact",
    component: lazyLoad("Contact"),
  },
  {
    path: "/login",
    name: "Login",
    component: lazyLoad("Login"),
    beforeEnter: [noAuth],
  },
  {
    path: "/register",
    name: "Register",
    component: lazyLoad("Register"),
    beforeEnter: [noAuth],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
