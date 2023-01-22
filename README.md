>Problem Statement : 

Create a simple http server (with Nodejs or any language) and make it respond with answer to calendar questions like below :

- add, 6 days to today return the date

- add, 6 weeks to today return the date

- subtract, 187 days from 12-jan-2019 return the date
>Solution :

**Used REST API protocols**

- **Backend Framework = Django**



REST API --> 

You can add / sub ->, minute , hour , days , weeks , months

- To add to the date.
` GET : /add/?week=<int>&days=<int>&month=<int>&hour=<int>&min=<int>&date=<date>`

- To sub to the date.
`GET : /sub/?week=<int>&days=<int>&month=<int>&hour=<int>&min=<int>&date=<date>`

### **I am not using POST as there is no saving into database is needed .** 

## GET : /sub
- To subtract from the given date , here date is a query_param
>``GET : http://localhost:8000/sub/?week=6&days=5&month=1&hour=3&min=30&date=12-jan-2019``
 Returns (with date, hr , min , sec) # "2018-10-25 20:30:00"

>`GET : http://localhost:8000/sub/?week=6&days=5&month=1&date=12-jan-2019`
Returns (date only , as there is no hr ,minute as a param) "2018-10-26"

- To subtract .from current date , as here date as a query_param is not present
```
`GET : http://localhost:8000/sub/?min=30&hour=3&days=5&week=6&month=1`

`GET : http://localhost:8000/sub/?min=30&hour=3&days=5&week=6`

`GET : http://localhost:8000/sub/?min=30&hour=3&days=5&week=6&month=1`
```

## GET : /add
- To add from the given date , here date is a query_param
```
GET : http://localhost:8000/add/?week=6&days=5&month=1&hour=3&min=30&date=12-jan-2019
- Returns (with hr , min , sec) # "2019-03-28 03:30:00" 
```

`GET : http://localhost:8000/add/?week=6&days=5&month=1&date=12-jan-2019`
` "2019-03-28"`

- To add .from current date , as here date as a query_param is not present
```
`GET : http://localhost:8000/add/?min=30&hour=3&days=5&week=6&month=1`
`GET : http://localhost:8000/add/?min=30&hour=3&days=5&week=6`
`GET : http://localhost:8000/add/?min=30&hour=3&days=5&week=6&month=1`
```

- Gives today's date
`GET : http://localhost:8000`
