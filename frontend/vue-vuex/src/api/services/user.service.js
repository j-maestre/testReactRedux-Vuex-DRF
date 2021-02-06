import axios from "axios";

export function userLogin() {
  return axios.get("https://api.coindesk.com/v1/bpi/currentprice.json");
}
