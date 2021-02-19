import { http, auth_http } from "../config";

export function login(credentials) {
  return http.post("users/login", { user: credentials });
}

export function register(credentials) {
  return http.post("users", { user: credentials });
}

export function getProfile() {
  return auth_http.get("user");
}
