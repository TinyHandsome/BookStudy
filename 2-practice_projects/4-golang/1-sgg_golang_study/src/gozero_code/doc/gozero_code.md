### 1. N/A

1. route definition

- Url: /from/:name
- Method: GET
- Request: `Request`
- Response: `Response`

2. request definition



```golang
type Request struct {
	Name string `path:"name"`
}
```


3. response definition



```golang
type Response struct {
	Message string `json:"message"`
}
```

### 2. N/A

1. route definition

- Url: /user
- Method: GET
- Request: `-`
- Response: `Response`

2. request definition



3. response definition



```golang
type Response struct {
	Message string `json:"message"`
}
```

