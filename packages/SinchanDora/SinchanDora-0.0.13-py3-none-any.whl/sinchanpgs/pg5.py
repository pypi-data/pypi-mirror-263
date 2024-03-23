def sayhello5():
    print('''<!DOCTYPE html>
<html>
  <head>
    <title>Student Details Application</title>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
    <script>
      var app = angular.module("myapp", []);
      app.controller("mycntrl", function ($scope) {
        $scope.studData = [];

        $scope.generateData = function () {
          $scope.studData = [];
          for (var i = 1; i <= $scope.num; i++) {
            var cgpa = Math.random() * 10;
            var stud = {
              SLNO: i,
              NAME: "Student-" + i,
              CGPA: cgpa.toFixed(2),
            };
            $scope.studData.push(stud);
          }
        };
      });
    </script>
  </head>
  <body ng-app="myapp">
    <h1>Student Details Application</h1>
    <div ng-controller="mycntrl">
      Enter the Number of Students to Generate the Data:
      <input type="number" ng-model="num" />
      <button ng-click="generateData()">Generate</button><br />
      <table border="1">
        <tr>
          <th>SLNO</th>
          <th>NAME</th>
          <th>CGPA</th>
        </tr>
        <tr ng-repeat="student in studData">
          <td>{{student.SLNO}}</td>
          <td>{{student.NAME}}</td>
          <td>{{student.CGPA}}</td>
        </tr>
      </table>
      <br />
      Number of Students = {{studData.length}}
    </div>
  </body>
</html>
''')