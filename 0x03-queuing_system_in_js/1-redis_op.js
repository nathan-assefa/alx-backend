// Import the node_redis library using ES6 import syntax
import redis from 'redis';

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


function setNewSchool(schoolName, value) {
  // Set the value for the key schoolName in Redis
  client.set(schoolName, value, redis.print)
};


function displaySchoolValue(schoolName) {
  // Retrieve the value for the specified key from Redis
  client.get(schoolName, (error, value) => {
    if (error) {
      console.error(error);
    } else {
      console.log(value);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
