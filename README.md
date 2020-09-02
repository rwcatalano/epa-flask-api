# EPA Flask API Server

### Access the environment
<p>Load the python environment</p>
<p>For windows us the .bat extension otherwise you can omit</p>
```
server/env/Scripts> activate.bat
```
<p>This will load your python environment and denote your bash with (env) server/env/Scripts</p>
<p>It is important to note that you must run the API Server and Client within the specified python environment</p>

### Start the flask api server
<p>The server is stored in a separate github repo to allow for parallel development between client and server</p>
<p>API server will run at http://127.0.0.1:5000</p>
```
server> python app.py
```

### Running tests
<p>Tests have been created for logic within the api.</p>
<p>Executing the command below will run the following tests:</p>
<ol>
  <li>test_triangle_area():</li>
  <li>test_triangle_area_float():</li>
  <li>test_triangle_area_negative():</li>
  <li>test_triangle_hypotenuse():</li>
  <li>test_triangle_hypotenuse_float():</li>
  <li>test_triangle_hypotenuse_negative():</li>
  <li>test_time_seconds():</li>
  <li>test_time_seconds_nagative():</li>
  <li>test_recursive_string():</li>
</ol>
```
server> pytest
```

### Running the client
<p>The client will load at http://127.0.0.1:8080</p>
<p>The client can be pulled here: https://github.com/rwcatalano/epa-vue-client</p>

<p>The client consists of 4 views that implement components to do the heavy lifting.</p>
<p>The client makes calls to the api located in the server using named parameters in the url.</p>

<ol>
  <li>Area - Calcuates the area of a triangle using the formula: 1.5 (base * height)</li>
  <li>Hypotenuse - Calculates the longest edge of a triangle using the Pythagorean Theorem</li>
  <li>Seconds - Calculates the seconds with multiple calls of a function that multiples a value by 60</li>
  <li>Recursion - Recursively calls itself based on the iteration count specified.</li>
</ol>

```
client> npm run serve
```

