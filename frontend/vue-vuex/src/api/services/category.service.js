import { http } from "../config";

export function getCategories() {
  return http.get("categories/");
}
