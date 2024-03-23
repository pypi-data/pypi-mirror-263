def sayhello8():
    print('''<!DOCTYPE html>
<html>
  <head>
    <title>Angular JS Login Form</title>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
    <script>
      var app = angular.module("myapp", []);
      app.controller("mycntrl", function ($scope) {
        $scope.loginFailed = false;
        $scope.loginAttempts = 0;

        $scope.login = function () {
          if ($scope.userName === "harish" && $scope.password === "12345678") {
            alert("Login Successful!");
            $scope.loginFailed = false;
          } else {
            alert("Incorrect username or password!");
            $scope.loginFailed = true;
            $scope.loginAttempts++;
          }
        };
      });
    </script>
    <style>
      .error-message {
        color: red;
      }
    </style>
  </head>
  <body ng-app="myapp" ng-controller="mycntrl">
    <h1>Angular JS Login Form</h1>
    <form name="loginForm" ng-submit="login()">
      <label>Username:</label>
      <input type="text" ng-model="userName" required />
      <span class="error-message" ng-show="loginForm.userName.$error.required">
        Username is required</span>
      
        <br /><br />
      <label>Password:</label>
      <input type="password" ng-model="password" required />
      <span class="error-message" ng-show="loginForm.password.$error.required"
        >Password is required</span
      >
      <br /><br />
      <button type="submit" ng-disabled="loginAttempts >= 3">Login</button>
    </form>
    <span class="error-message" ng-show="loginFailed"
      >Incorrect username or password!</span
    >
  </body>
</html>
''')