import fetch from "node-fetch";
import aspida from "@aspida/node-fetch";
import api from "./api/$api";

const client = api(aspida(fetch, { baseURL: "http://localhost:10080" }));
(async () => {
  const response = await client.users.get();
  console.log(response);
})();
