'use strict';

angular.module('addshop').
		component('addshop',{     
			 templateUrl: 'api/templates/addshop.html',
		controller : function($scope, $element, $anchorScroll, 
			$location, $mdDialog, $filter, City, Category, SubCategory,Addshop,Map){ 
				$scope.goaddshop = function(shopdata){
					Addshop.create(JSON.stringify({
						city : shopdata.city,
						category : shopdata.category,
						subCategory : shopdata.subCategory,
						shopName : shopdata.shopName,
						tagline : shopdata.tagline,
						bannerImage : shopdata.bannerImage,
						email : shopdata.email,
						mobileNo : shopdata.mobileNo,
						alternateMobileNo : shopdata.alternateMobileNo,
						location : shopdata.location,
						ownerName : shopdata.ownerName,
						shopAddress : shopdata.shopAddress,
						shopPinCode : shopdata.shopPinCode,
						openingTime : shopdata.openingTime,
						closingTime : shopdata.closingTime,
						closingDay : JSON.stringify(shopdata.closingDay),

					}))					 
		 }

		 			 City.query({},function(data){
				$scope.cityList = data
		});		
				 Category.query({},function(data){
				$scope.categoryList = data  
		});     
				SubCategory.query({},function(data){
				$scope.subcategoryList = data

		});

	 
		$scope.days = ["sunday","monday" ,"tuesday" ,"thursday" ,"friday", "saturday"];
			
		$scope.states = [ 'Utter Pradesh','Delhi','Jammu & Kashmir','Uttarakhand','Bihar','Rajasthan','Madhya Pradesh','Andaman and Nicobar Islands','Andra Pradesh','Arunachal Pradesh','Assam','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Orissa','Punjab','Sikkim','Tamil Nadu','Tripura','West Bengal','Pondicherry','Lakshadeep','Daman and Diu','Dadar and Nagar Haveli','Chandigarh']       

		$scope.scrollTo = function(id,show) {
		$location.hash(id);
		$anchorScroll();   
	};
		 
  }

});
