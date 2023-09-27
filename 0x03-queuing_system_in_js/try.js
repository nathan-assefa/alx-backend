const { promisify } = require('util')

function getUserData(userId, callback) {
  setTimeout(() => {
    if (userId === 1) {
      callback(null, { id: 1, username: 'john_doe' });
    } else {
      callback(new Error('User not found'));
    }
  }, 1000);
}

const getAsync = async () => {
	const prom = promisify(getUserData)
	try {
		res = await prom(1)
		console.log(res)
	} catch(error) {
		console.log(error)
	}
}

getAsync()
