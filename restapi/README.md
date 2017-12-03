# REST API sample

An python script to let me understand what ```REST API``` is and
how to use ```Flask-SQLAlchemy``` and ```Flask-RESTful```.


1... Run ```restapi.py``` or ```restful.py```

```sh
>py restapi.py
 * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: xxx-xxx-xxx
```

2... Open the other terminal and Check Database
```sh
>curl -i http://127.0.0.1:8000/sqlalc/
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 40
Server: Werkzeug/0.11.4 Python/3.5.3
Date: Sun, 03 Dec 2017 13:02:54 GMT

{
  "data": [],
  "r": "GET success"
}
```

3... ```PUT``` with id = '1'... then ```fail```, because id can't be given when ```PUT```.
```sh
>curl -i http://127.0.0.1:8000/sqlalc/1/Taro/Hage -X PUT
HTTP/1.0 403 FORBIDDEN
Content-Type: application/json
Content-Length: 49
Server: Werkzeug/0.11.4 Python/3.5.3
Date: Sun, 03 Dec 2017 13:03:14 GMT

{
  "id": "1",
  "r": "PUT fail, no id found"
}
```

4... ```PUT``` with id = '-'... then ```success```
```sh
> curl -i http://127.0.0.1:8000/sqlalc/-/Taro/Hage -X PUT
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 76
Server: Werkzeug/0.11.4 Python/3.5.3
Date: Sun, 03 Dec 2017 13:03:32 GMT

{
  "id": 1,
  "looks": "Hage",
  "name": "Taro",
  "r": "PUT success"
}
```

5... ```PUT``` one more. 
```sh
>curl -i http://127.0.0.1:8000/sqlalc/-/Jiro/MottoHage -X PUT
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 81
Server: Werkzeug/0.11.4 Python/3.5.3
Date: Sun, 03 Dec 2017 13:03:43 GMT

{
  "id": 2,
  "looks": "MottoHage",
  "name": "Jiro",
  "r": "PUT success"
}
```

6... Check Database
```sh
>curl -i http://127.0.0.1:8000/sqlalc/
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 196
Server: Werkzeug/0.11.4 Python/3.5.3
Date: Sun, 03 Dec 2017 13:03:50 GMT

{
  "data": [
    {
      "id": 1,
      "looks": "Hage",
      "name": "Taro"
    },
    {
      "id": 2,
      "looks": "MottoHage",
      "name": "Jiro"
    }
  ],
  "r": "GET success"
}
```

7... ```GET``` with id = '1'
```sh
>curl -i http://127.0.0.1:8000/sqlalc/1/-/-
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 76
Server: Werkzeug/0.11.4 Python/3.5.3
Date: Sun, 03 Dec 2017 13:04:04 GMT

{
  "id": 1,
  "looks": "Hage",
  "name": "Taro",
  "r": "GET success"
}
```

8... or ```GET``` with name = 'Taro'
```sh
>curl -i http://127.0.0.1:8000/sqlalc/-/Taro/-
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 76
Server: Werkzeug/0.11.4 Python/3.5.3
Date: Sun, 03 Dec 2017 13:04:17 GMT

{
  "id": 1,
  "looks": "Hage",
  "name": "Taro",
  "r": "GET success"
}
```

9... ```DELETE``` with id = '1'
```sh
>curl -i http://127.0.0.1:8000/sqlalc/1/-/- -X DELETE
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 28
Server: Werkzeug/0.11.4 Python/3.5.3
Date: Sun, 03 Dec 2017 13:04:29 GMT

{
  "r": "DELETE success"
}
```

10... Check Database
```sh
>curl -i http://127.0.0.1:8000/sqlalc/
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 121
Server: Werkzeug/0.11.4 Python/3.5.3
Date: Sun, 03 Dec 2017 13:04:34 GMT

{
  "data": [
    {
      "id": 2,
      "looks": "MottoHage",
      "name": "Jiro"
    }
  ],
  "r": "GET success"
}
```
