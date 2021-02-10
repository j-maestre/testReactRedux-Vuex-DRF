import axios from "axios";

export function login() {
  return axios.get("https://api.coindesk.com/v1/bpi/currentprice.json");
}

export function register() {
  // const user = { user: credentials };
  let http = axios.create({
    baseURL: "http://localhost:8000/api",
  });

  return http.get("/travels");
}
