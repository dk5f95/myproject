'use strict';

angular.module('city.services').
	factory('City',function($resource){
		var url = '/api/shop/cities'
		var cityQuery = {
			method : "GET",
			params : {},
			isArray: true,
			cache: true, 
		}
		var getCity = {
			url: url + ":id/",
			method: "GET",
			params:{"id":"@id"},
			isArray:true,
			cache:true
		}

		return $resource(url, {}, {
   		 query : cityQuery,
   		 get : getCity 
  		});
	});
