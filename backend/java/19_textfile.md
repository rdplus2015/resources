# Text Files **Processing** in Java — The Essentials


## Why files?

- Memory is cleared at the end of a program: to **persist** data, we use **files** (disk, USB drive).
- A **text file** contains **character strings**; each line ends with a **line break**. Readable, simple, but bulky for large datasets.


## Typical cycle

1. **Open** the file → create a _stream_.
2. **Process** → read/write.
3. **Close** → free resources (important: I/O is **slow** vs CPU).

## Stream notion (Streams)

- **Input** to read, **Output** to write.
- For **characters**, we use the `Reader` / `Writer` hierarchies (package `java.io`).

---

## Key classes (characters)

### `FileReader`

- **Reads** characters from a file.
- `new FileReader(String fileName)` → throws `FileNotFoundException` if absent.
- `int read()` → code of the character read, **-1** at end of file.
- `close()` to close.

### `BufferedReader`

- **Filter** that **buffers** a `Reader`.
- `new BufferedReader(new FileReader(...))`
- `String readLine()` → **null** at end of file; reads **one line** at a time (handy). 

### `FileWriter`

- **Writes** characters to a file.
- `new FileWriter(String)` (**overwrites**) ; `new FileWriter(String, true)` (**append**).
- `void write(int c)` ; `close()`. 

### `BufferedWriter`

- **Filter** that **buffers** a `Writer`.
- `new BufferedWriter(new FileWriter(...))`
- `void write(String s)` ; `void newLine()` for a **portable** line break ; `close()`. 【7†source】

> **Tip**: use **try-with-resources** to close automatically.

---

## Ready‑to‑use examples

### 1) Read a file and print each line

```java
import java.io.*;

public class LireFichier {
  public static void main(String[] args) throws IOException {
    try (BufferedReader in = new BufferedReader(new FileReader("test.txt"))) {
      String ligne;
      while ((ligne = in.readLine()) != null) {
        System.out.println(ligne);
      }
    }
  }
}
```


### 2) Write lines entered from the keyboard (append = false → overwrite)

```java
import java.io.*;
import javax.swing.JOptionPane;

public class EcrireFichier {
  public static void main(String[] args) throws IOException {
    try (BufferedWriter out = new BufferedWriter(new FileWriter("result.txt", false))) {
      String s;
      while (true) {
        s = JOptionPane.showInputDialog(null, "Entrez une phrase (\"fin\" pour arrêter) :");
        if (s == null || "fin".equalsIgnoreCase(s)) break;
        out.write(s);
        out.newLine();
      }
    }
  }
}
```


### 3) Copy a file **line by line**

```java
import java.io.*;

public class CopierFichier {
  public static void main(String[] args) throws IOException {
    try (BufferedReader in  = new BufferedReader(new FileReader("test.txt"));
         BufferedWriter out = new BufferedWriter(new FileWriter("result.txt"))) {
      String ligne;
      while ((ligne = in.readLine()) != null) {
        out.write(ligne);
        out.newLine();
      }
      System.out.println("Copie avec succès");
    }
  }
}
```


---

##  Read/Write » head (cursor)

- At the **start**, positioned **at the beginning** of the file (or **at the end** if opened in append).
- Each `readLine()` or `newLine()` **advances** the position.
- To **return to the beginning**, **close** then **reopen** the file. 【7†source】

---

## Summary table

| Action / Mode | **Read**                 | **Write (overwrite)**         | **Write (append)**            |
| ------------- | ------------------------ | ----------------------------- | ----------------------------- |
| Open          | `new FileReader("f")`    | `new FileWriter("f", false)`  | `new FileWriter("f", true)`   |
| Character     | `in.read()`              | `out.write(int)`              | `out.write(int)`              |
| **Buffer**    | `new BufferedReader(in)` | `new BufferedWriter(out)`     | `new BufferedWriter(out)`     |
| **Line**      | `readLine()`             | `write(String)` + `newLine()` | `write(String)` + `newLine()` |
| Close         | `in.close()`             | `out.close()`                 | `out.close()`                 |

---

## Best practices (beyond the slides)

- **Try/catch** exceptions (or `throws`) and prefer **try-with-resources**.
- **Encoding**: for explicit UTF‑8, use `new InputStreamReader(new FileInputStream(f), StandardCharsets.UTF_8)` or `Files.newBufferedReader(...)`.
- **Performance**: buffer (`BufferedReader/Writer`) to limit disk access.
- **Portability**: `newLine()` manages the line break depending on the OS.

---