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

// Subscribe to the 'holberton school channel'
client.subscribe('holberton school channel');

// Listen for messages on the subscribed channel
client.on('message', (channel, message) => {
  console.log(`Message received on channel '${channel}': ${message}`);
  
  // If the message is 'KILL_SERVER', unsubscribe and quit
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
