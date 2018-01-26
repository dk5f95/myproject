 'use strict';

 angular.module('addshop.services').

factory ('Addshop',function($resource){

    var url = '/api/shop/create'

 
          return $resource(url,{},{
            create:{
               
                method : "POST",
                params : {},
               

            }
            })
       });



