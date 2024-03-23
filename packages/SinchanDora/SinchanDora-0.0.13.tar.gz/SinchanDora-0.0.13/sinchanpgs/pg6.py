def sayhello6():
    print('''<!DOCTYPE html>
<html>
  <title>TO DO Application</title>
  <head>
    <script
      type="text/javascript"
      src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"
    ></script>
    <script>
      var app = angular.module("myapp", []);
      app.controller("mycntrl", function ($scope) {
        $scope.tasks = [
          { title: "Task-1", completed: true, editing: false },
          { title: "Task-2", completed: false, editing: false },
          { title: "Task-3", completed: false, editing: false },
        ];

        $scope.addTask = function () {
          if ($scope.newTask) {
            var t = {
              title: $scope.newTask,
              completed: false,
              editing: false,
            };
            $scope.tasks.push(t);
          } else {
            alert("Please enter the task to add");
          }
        };

        $scope.edit = function (task) {
          task.editing = true;
        };

        $scope.noedit = function (task) {
          task.editing = false;
        };

        $scope.delete = function (task) {
          var index = $scope.tasks.indexOf(task);
          $scope.tasks.splice(index, 1);
        };
      });
    </script>
  </head>
  <body ng-app="myapp">
    <h1>TO DO APPLICATION</h1>
    <div ng-controller="mycntrl">
      Enter the name of the Task: <input type="text" ng-model="newTask" />
      <button ng-click="addTask()">Add Task</button> <br />
      <br />
      <table border="1">
        <tr>
          <th>SLNO</th>
          <th>Status</th>
          <th>Task</th>
          <th>Edit</th>
          <th>Delete</th>
        </tr>
        <tr ng-repeat="task in tasks">
          <td>{{$index+1}}</td>
          <td><input type="checkbox" ng-model="task.completed" /></td>
          <td>
            <span ng-show="!task.editing">{{task.title}}</span>
            <input
              type="text"
              ng-show="task.editing"
              ng-model="task.title"
              ng-blur="noedit(task)"
            />
          </td>
          <td><button ng-click="edit(task)">Edit</button></td>
          <td><button ng-click="delete(task)">Delete</button></td>
        </tr>
      </table>
    </div>
  </body>
</html>
''')