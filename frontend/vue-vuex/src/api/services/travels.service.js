import axios from "axios";

export function list() {
  return axios.get("http://localhost:8000/api/travels");
}

export function create(data) {
  return axios.post("http://localhost:8000/api/travels/create/");
}
