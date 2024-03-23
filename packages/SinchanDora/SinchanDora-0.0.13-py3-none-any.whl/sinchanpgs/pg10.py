def sayhello10():
    print('''<!DOCTYPE html>
<html>
  <title>Item Management Application</title>
  <head>
    <script
      type="text/javascript"
      src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"
    ></script>
    <script>
      var app = angular.module("myapp", []);
      app.controller("mycntrl", function ($scope) {
        $scope.itemList = ["Pen", "Pencil", "Eraser", "Book"];
        $scope.addItem = function () {
          if (!$scope.newItem) {
            alert("Please enter an item to add");
            return;
          }

          if ($scope.itemList.indexOf($scope.newItem) !== -1) {
            alert("This item is already there in the shopping list");
            return;
          }

          $scope.itemList.push($scope.newItem);
          $scope.newItem = "";
        };
        $scope.removeItem = function (item) {
          var index = $scope.itemList.indexOf(item);
          if (index !== -1) {
            $scope.itemList.splice(index, 1);
          } else {
            alert("Please select an item to remove");
          }
        };
      });
    </script>
  </head>
  <body ng-app="myapp">
    <h1>Item Management Application</h1>
    <div ng-controller="mycntrl">
      Enter an item to add: <input type="text" ng-model="newItem" />
      <button ng-click="addItem()">ADD</button> <br /><br />
      <b>List of Items</b>
      <table border="1">
        <tr>
          <th>SLNO</th>
          <th>Item</th>
          <th>Remove</th>
        </tr>
        <tr ng-repeat="item in itemList">
          <td>{{$index+1}}</td>
          <td>{{item}}</td>
          <td><button ng-click="removeItem(item)">Remove</button></td>
        </tr>
      </table>
      <br />
      Total Number of Items=<b>{{itemList.length}}</b>
    </div>
  </body>
</html>
''')