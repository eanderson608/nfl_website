app.controller('NFLController', function($scope, $http) {
	$http.get("http://ec2-54-214-112-22.us-west-2.compute.amazonaws.com/testdata.php")
		.then(function(response) {
			$scope.tables = response.data;
		}, function(error) {
			$scope.status = error.status;
			console.error(error);
		});
});