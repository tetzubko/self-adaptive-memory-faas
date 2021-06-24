exports.handler = async (event) => {
    mySlowFunction(8);
    const response = {
        statusCode: 200,
        body: JSON.stringify('test'),
    };
    return response;
};


function mySlowFunction(baseNumber) {
	console.time('mySlowFunction');
	let result = 0;
	for (var i = Math.pow(baseNumber, 7); i >= 0; i--) {
		result += Math.atan(i) * Math.tan(i);
	}
	console.timeEnd('mySlowFunction');
}


// Adapted from: https://gist.github.com/sqren/5083d73f184acae0c5b7