import axios from "axios";

export function login(user) {
  console.log("LOGIN OLE LOS CANELONES")
  console.log("USER BUENO")
  console.log(user)
  return axios.post("http://localhost:8000/api/users/login",user).then((response) => response);
  // "https://api.coindesk.com/v1/bpi/currentprice.json"
}



export function register() {
  const user = { user: credentials };
  let http = axios.create({
    baseURL: "http://localhost:8000/api",
  });

  // return http.get("/travels");

  return http.post("users", user)
  .then((response) => response);

}
