import { http } from "../config";

export function list() {
  return http.get("http://localhost:8000/api/travels");
}

export function create(data) {
  return http.post("http://localhost:8000/api/travels/create/", data);
}
