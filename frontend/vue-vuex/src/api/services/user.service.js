import axios from "axios";

export function login(user) {
  console.log("LOGIN OLE LOS CANELONES")
  console.log("USER BUENO")
  console.log(user)
  return axios.post("http://localhost:8000/api/users/login",user).then((response) => response);
  // "https://api.coindesk.com/v1/bpi/currentprice.json"
}

export function register(credentials) {
  const user = { user: credentials };
  console.log("Vamos al register ole los canelones")
  return axios
    .post("http://localhost:8000/api/users/", user)
    .then((response) => response);
}
