1.) Error:403-forbidden:

    Problem(403) Description:
        -Today i created an Access Tokens and tested it with POSTMAN to make a request to an endpoint but i got a 403 forbidden This error,this took me 3 hours of debugging as a result of wrong configuration and syntax Error in settings.REST_FRAMEWORK,

    Solution(403):
        -i configured settings.REST_FRAMEWORK correctly with right syntax


2.) Error:401-unauthorized:

    Problem(401) Description:
        -i created a user registeration endpoint('/user/register/') which creates a user on my database but whenever i try to access token endpoint ('/token') with user's credential ("username","password"),i get a 401 unauthorized error(invalid credentials),this took me 2 hours of debugging.

    solution: 
        check if user was created properly with create_user or create_superuser

3.) Error:non ISO-8859-1 code point:
    problem Description:
        -This Error occured while working with Role Base Access Control system,i was using fetch-api(react.js) to send a request to a token endpoint which was successful,and i console it out on the client side after extending access_token's lifetime from the backend,in console the token length was a little bit shorter compared to the response given to me on my Network tab in browser dev tools,i attached the shorter token response from console to my headers to make an authenticated request to my backend endpoint this is how i got "(Error:Failed to execute 'fetch' on 'Window': Failed to read the 'headers' property from 'RequestInit': String contains non ISO-8859-1 code point.)"

    Insights:
        Token from console:"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90e…EyIn0.3hEc7ewLyU_bqLBqL8IbyXHMCitj9D_sLqFERYybI7s"
        Token from devtool>Network>Response :"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc4MDc0NDQzLCJpYXQiOjE3NzgwNzA4NDMsImp0aSI6Ijk0MzQxYjM1ODIzYTRmNjFhYzRjMTVjYWE4OGU5N2YwIiwidXNlcl9pZCI6IjEyIn0.3hEc7ewLyU_bqLBqL8IbyXHMCitj9D_sLqFERYybI7s"
    
    solution:
        i use the token from devtool>Network>Response and request went successful
.
4.)Error: Cannot destructure property 'basename' of useContext(...) as it is null

    Cause:
    `Header` and `Footer` used `Link` from React Router outside `<BrowserRouter>`.

    Why it happened:
    `Link` needs Router Context from `<BrowserRouter>`. Without it, `useContext()` returns `null`.

    Fix:
    Wrap the entire app (`Header`, `Routes`, and `Footer`) inside one `<BrowserRouter>` in `main.jsx/main.tsx`.

