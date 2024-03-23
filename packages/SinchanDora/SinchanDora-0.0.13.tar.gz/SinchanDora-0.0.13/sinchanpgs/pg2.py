def sayhello2():
    print('''<!DOCTYPE html>
<html>
<head>
  <title>Shopping Items Application</title>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
  <script>
    var app = angular.module("myApp", []);
    app.controller("myCntrl", function($scope) {
      $scope.shoppingItems = ['Apple', 'Mango', 'Banana', 'Grapes'];

      $scope.addItem = function() {
        if (!$scope.newItem) {
          alert("Please enter an item to add");
          return;
        }
        
        if ($scope.shoppingItems.indexOf($scope.newItem) !== -1) {
          alert("This item is already there in the shopping list");
          return;
        }

        $scope.shoppingItems.push($scope.newItem);
        $scope.newItem = "";
      };

      $scope.removeItem = function() {
        var index = $scope.shoppingItems.indexOf($scope.selectItem);
        if (index !== -1) {
          $scope.shoppingItems.splice(index, 1);
          $scope.selectItem = "";
        } else {
          alert("Please select an item to remove");
        }
      };
    });
  </script>
</head>
<body ng-app="myApp">
  <div ng-controller="myCntrl">
    <h2>Shopping Application</h2>
    <h4>List of Shopping Items</h4>
    <table border="1">
      <tr>
        <th>SLNO</th>
        <th>Item</th>
      </tr>
      <tr ng-repeat="item in shoppingItems">
        <td>{{$index+1}}</td>
        <td>{{item}}</td>
      </tr>
    </table>
    <br/>
    <div>
      Enter an Item to Add:
      <input type="text" ng-model="newItem">
      <button ng-click="addItem()">Add Item</button>
    </div>
    <div>
      Select an Item to Remove:
      <select ng-model="selectItem" ng-options="item for item in shoppingItems"></select>
      <button ng-click="removeItem()">Remove Item</button>
    </div>
  </div>
</body>
</html>
''')