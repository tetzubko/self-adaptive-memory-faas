module.exports.timestamp = (event, context, callback) => {
    mySlowFunction(8);
  const response = {
    statusCode: 200,
    headers: {
      "Content-Type": "text/plain"
    },
    body: "sucess"
  };

  callback(null, response)
};

function mySlowFunction(baseNumber) {
	console.time('mySlowFunction');
	let result = 0;
	for (var i = Math.pow(baseNumber, 7); i >= 0; i--) {
		result += Math.atan(i) * Math.tan(i);
	}
	console.timeEnd('mySlowFunction');
}