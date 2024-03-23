def sayhello1():
    print('''<!DOCTYPE html>
    <head>
        <title>1</title>
        <script type ="text/javascript" 
        src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"
    >
    </script>
    <script>
        var app=angular.module("myapp",[])
        app.controller('mycntrl',function($scope){
            $scope.fname="abhi";
            $scope.lname="shek";
        });
    </script>
    <style>
    </head>

<body ng-app="myapp">
    <h1>Abhishek</h1>
    <div class="a" ng-controller="mycntrl">
        Enter first name:<input type="text" ng-model="fname"><br/>
        Enter last name:<input type="text" ng-model="lname"><br/>
        full name:{{fname+" "+lname}}
    </div>
</body>
</html>''')