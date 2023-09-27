const redis = require('redis');
const client = redis.createClient();

// Create Hash
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

// Display Hash
client.hgetall('HolbertonSchools', (error, hashObject) => {
  if (error) {
    console.error(error);
  } else {
    console.log(hashObject);
  }

  // Close the Redis connection
  client.quit();
});
