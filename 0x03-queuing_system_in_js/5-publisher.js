const redis = require('redis');
const client = redis.createClient();

// On connect, log a message
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// On error, log an error message
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

// Function to publish a message after a specified time
function publishMessage(message, time) {
  setTimeout(() => {
    console.log('About to send MESSAGE');
    client.publish('holberton school channel', message);
  }, time);
}

// Call the publishMessage function with different messages and times
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
