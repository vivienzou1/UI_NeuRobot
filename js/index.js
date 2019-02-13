(function() {
  var app = angular.module('chatApp', []);

  app.controller('MessageCtrl', function($scope) {
    $scope.messages = [{
      Name: 'Vivien Z',
      Message: "How should I subscribe to the Uniqlo newsletter? "
    }, {
      Name: 'Vitual Assistant',
      Message: "Our email newsletter signup can be found in the footer of any page on the site. Click on the footer to open it."
    }, {
      Name: 'Vivien Z',
      Message: "...Hard to find still.."
    }];
  });

})();