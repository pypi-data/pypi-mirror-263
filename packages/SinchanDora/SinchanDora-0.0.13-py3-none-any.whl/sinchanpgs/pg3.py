def sayhello3():
    print('''<!DOCTYPE html>
<html>
  <head>
    <title>AJS Simple Calculator</title>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
    <script>
      var app = angular.module("myapp", []);
      app.controller("mycntrl", function ($scope) {
        $scope.num1 = 0;
        $scope.num2 = 0;
        $scope.result = 0;
        $scope.operator = "add";

        $scope.compute = function () {
          switch ($scope.operator) {
            case "add":
              $scope.result = $scope.num1 + $scope.num2;
              break;
            case "sub":
              $scope.result = $scope.num1 - $scope.num2;
              break;
            case "mul":
              $scope.result = $scope.num1 * $scope.num2;
              break;
            case "div":
              if ($scope.num2 == 0) {
                alert("Divide by zero error");
              } else {
                $scope.result = $scope.num1 / $scope.num2;
              }
              break;
          }
        };
      });
    </script>
  </head>
  <body ng-app="myapp">
    <div ng-controller="mycntrl">
      <h1>Angular JS Simple Calculator</h1>

      Enter First Number: <input type="number" ng-model="num1" /><br />
      Select Operator:
      <select ng-model="operator">
        <option value="add">+</option>
        <option value="sub">-</option>
        <option value="mul">*</option>
        <option value="div">/</option>
        </select>
        <br />
      Enter Second Number: <input type="number" ng-model="num2" /><br />
      <button ng-click="compute()">Compute</button><br />
      <b>{{num1 + " " + operator + " " + num2 + " = " + result}}</b>
    </div>
  </body>
</html>
''')