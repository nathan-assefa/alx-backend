// Import the node_redis library using ES6 import syntax
import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client instance
const client = redis.createClient();

// Handle the "ready" event when the client successfully connects to Redis
client.on('ready', () => {
  console.log('Redis client connected to the server');
});

// Handle any errors that occur during the connection
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Promisify the Redis client methods
// the client.get method expects to be called on a Redis client instance, so we use .bind(client)
const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
  // Set the value for the key schoolName in Redis
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  try {
    // Retrieve the value for the specified key from Redis using async/await
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (error) {
    console.error(error);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
