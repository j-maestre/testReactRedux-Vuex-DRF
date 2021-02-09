import axios from "axios";

export function login() {
  return axios.get("https://api.coindesk.com/v1/bpi/currentprice.json");
}

export function register(credentials) {
  const user = { user: credentials };
  return axios
    .post("http://127.0.0.1:8000/api/users/", user)
    .then((response) => response);
}
