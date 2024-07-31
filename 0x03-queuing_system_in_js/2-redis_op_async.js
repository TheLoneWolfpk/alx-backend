import redis from "redis";
import { promisify } from "util";

const client = redis.createClient();
const useAsync = promisify(client.get).bind(client);

client.on("error", (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
})
client.on("connect", () => {
  console.log("Redis client connected to the server");
})

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    redis.print(`Reply: ${reply}`);
  });
}

async function displaySchoolValue(schoolName) {
  const reply = await useAsync(schoolName);
  console.log(reply);
}


(async () => {
await displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
await displaySchoolValue("HolbertonSanFrancisco");
})();
