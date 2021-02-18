import axios from "axios";

export const config = {
  baseURL: "http://localhost:8000/api",
  token: localStorage.getItem("token"),
};

export const auth_http = axios.create({
  baseURL: config.baseURL,
  headers: config.token
    ? {
        common: {
          Authorization: "Token " + config.token,
        },
      }
    : {},
});

export const http = axios.create({
  baseURL: config.baseURL,
});
