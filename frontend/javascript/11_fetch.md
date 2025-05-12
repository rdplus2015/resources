
#  Fetch in JavaScript

##  Introduction

- `fetch` is used both on the browser and server side to contact a server (make HTTP requests).
- The `fetch()` method allows making HTTP calls to retrieve resources and uses Promises.
- The first parameter is usually a string representing the URL of the resource to fetch.
- The second parameter is an options object that specifies the method, headers, body, etc.

---

##  Basic Usage

```js
fetch('https://jsonplaceholder.typicode.com/posts?_limit=10')
.then(res => {
    console.log(res); // Once we contact the server, this logs the response object (a Promise)
});
```

```js
fetch('https://jsonplaceholder.typicode.com/posts?_limit=10')
.then(res => {
    console.log(res.text()); // `.text()` is a method on the response object: returns the body as a textual Promise
});
```

```js
fetch('https://jsonplaceholder.typicode.com/posts?_limit=10')
.then(res => res.text())
.then(body => {
    console.log(body); // We retrieve the response (resolve the Promise with text) and log the body
});
```

```js
fetch('https://jsonplaceholder.typicode.com/posts?_limit=10')
.then(res => res.json())
.then(body => {
    console.log(body); // Same as above, but we want JSON data (auto-parsed)
});
```

---

##  Function Example to Fetch Users

```js
async function fecthuser() {
    /*
    - Retrieves asynchronously
    - The second parameter is an object with extra options to normalize the HTTP request
    */
    const r = await fetch('https://jsonplaceholder.typicode.com/posts?_lcimit=10', {
        method: 'GET',
        headers: {
            'Accept': 'application/json', // What we expect to receive
        }
    });

    if (r.ok === true) {
        return r.json();
    }
    throw new Error('Impossible de contacter le serveur');
}

fecthuser().then(users => console.log(users));
```

---

##  Function Example to Send Users (POST)

```js
async function fecthuser() {
    /*
    - Sends asynchronously
    - The second parameter is an object with HTTP info
    */
    const r = await fetch('https://jsonplaceholder.typicode.com/posts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' // What we send
        },
        body: JSON.stringify({
            'title': 'mon article',
        })
    });

    if (r.ok === true) {
        return r.json();
    }
    throw new Error('Impossible de contacter le serveur');
}
```

---

##  JSON Note

- The `JSON` object is available in browsers and contains two useful methods:
    - `JSON.parse()`: Takes a JSON string and returns the JavaScript object.
    - `JSON.stringify()`: Takes an object and returns the equivalent JSON string.

---

##  Cancel a Fetch Request with AbortController

```js
/*
- If one request finishes, the other is aborted.
- This can be useful in some situations.
*/
const a = new AbortController();

Promise.race([
    fetch('https://jsonplaceholder.typicode.com/posts?_limit=10&_delay=3000', {
        signal: a.signal,
    }),
    fetch('https://jsonplaceholder.typicode.com/users?_limit=5', {
        signal: a.signal,
    }),
])
.then(res => res.json())
.then(body => {
    a.abort(); // Abort remaining request
    console.log(body);
});
```