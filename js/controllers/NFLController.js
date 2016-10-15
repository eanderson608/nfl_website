app.controller('NFLController', function($scope, $http) {
	$http.get("http://ec2-54-244-135-126.us-west-2.compute.amazonaws.com/gettabledata.php")
		.then(function(response) {
			$scope.records = response.data.records;
		});
});