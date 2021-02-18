export function auth(to, from, next) {
  !localStorage.getItem("token") ? next({ name: "Login" }) : next();
}

export function noAuth(to, from, next) {
  localStorage.getItem("token") ? next({ name: "Home" }) : next();
}
