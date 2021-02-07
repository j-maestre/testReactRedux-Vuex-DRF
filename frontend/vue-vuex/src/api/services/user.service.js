import axios from "axios";

export function login() {
  return axios.get("https://api.coindesk.com/v1/bpi/currentprice.json");
}

export function register() {
  return axios.get("https://api.coindesk.com/v1/bpi/currentprice.json");
}
