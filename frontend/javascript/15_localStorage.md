
# Working with `localStorage` in JavaScript

`localStorage` is a Web API that allows you to store key-value pairs in a web browser with no expiration time. The data is saved across browser sessions and persists even after closing the browser.

---

##  Basic Usage

### 1. Store a value

```javascript
localStorage.setItem('username', 'JohnDoe');
```

### 2. Retrieve a value

```javascript
const username = localStorage.getItem('username');
console.log(username); // Outputs: JohnDoe
```

### 3. Remove a specific item

```javascript
localStorage.removeItem('username');
```

### 4. Clear all localStorage entries

```javascript
localStorage.clear();
```

---

##  Notes

- All data is stored as strings. Objects must be serialized using `JSON.stringify()`.
- You can check how much storage is used in the browser DevTools under Application > Local Storage.
- Maximum storage size varies by browser, but is usually around 5MB per origin.

---

##  Working with Objects

```javascript
const user = {
    name: 'Jane',
    age: 30,
    role: 'admin'
};

// Save to localStorage
localStorage.setItem('user', JSON.stringify(user));

// Retrieve from localStorage
const storedUser = JSON.parse(localStorage.getItem('user'));
console.log(storedUser.name); // Outputs: Jane
```

---

##  Security Considerations

- Data stored in localStorage is not encrypted.
- Never store sensitive information like passwords or tokens.
- Accessible via JavaScript on the same origin—be aware of XSS vulnerabilities.

---

##  Check if a Key Exists

```javascript
if (localStorage.getItem('username')) {
    console.log('User is logged in');
} else {
    console.log('No user found');
}
```

---

## Limitations

- Only supports string keys and values.
- Synchronous API — can block the main thread if used excessively.
- No automatic expiration — use `sessionStorage` if you want the data to clear after the tab closes.

---

##  When to Use

- Remembering user preferences
- Persisting theme or UI settings
- Storing non-sensitive data between sessions

---

# Working with `sessionStorage` in JavaScript

`sessionStorage` is a Web API that allows you to store key-value pairs **temporarily** in a web browser. The data is saved per tab or window and is **cleared automatically** when the tab or window is closed.

---

## Basic Usage

### 1. Store a value

```javascript
sessionStorage.setItem('sessionId', 'ABC123');
```

### 2. Retrieve a value

```javascript
const sessionId = sessionStorage.getItem('sessionId');
console.log(sessionId); // Outputs: ABC123
```

### 3. Remove a specific item

```javascript
sessionStorage.removeItem('sessionId');
```

### 4. Clear all sessionStorage entries

```javascript
sessionStorage.clear();
```

---

## Notes

- All data is stored as strings.
- Objects must be serialized with `JSON.stringify()` before storing.
- Data is **not shared** between tabs or windows.
- `sessionStorage` is **cleared automatically** when the tab or browser is closed.

---

## Working with Objects

```javascript
const user = {
    name: 'Alice',
    age: 25,
    role: 'editor'
};

// Save to sessionStorage
sessionStorage.setItem('user', JSON.stringify(user));

// Retrieve from sessionStorage
const storedUser = JSON.parse(sessionStorage.getItem('user'));
console.log(storedUser.role); // Outputs: editor
```

---

## Security Considerations

- `sessionStorage` is not secure — avoid storing sensitive data like passwords or tokens.
- It's accessible from JavaScript, so always sanitize inputs and guard against XSS attacks.

---

## Check if a Key Exists

```javascript
if (sessionStorage.getItem('sessionId')) {
    console.log('Session is active');
} else {
    console.log('No session found');
}
```

---

## When to Use

- Store temporary form data
- Maintain state during a single tab session
- Manage multi-step forms
- Store user selections in a session (e.g., temporary filters)

---