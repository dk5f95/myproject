'use strict';

angular.module('cityaplapp').
	config(
		function($resourceProvider,$routeProvider){
   $resourceProvider.defaults.stripTrailingSlashes=false;

   $routeProvider.
 when("/",{
      template:"<addshop></addshop>"
			
		})


})
 
