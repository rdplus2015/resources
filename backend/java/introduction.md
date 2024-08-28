
# Java

## Introduction to Java

- **Java SE** (Standard Edition): The core platform for general-purpose applications.
- **Java EE** (Enterprise Edition): Extensions for enterprise applications.
- **JVM** (Java Virtual Machine): Executes Java bytecode on any platform.
- **JDK** (Java Development Kit): Includes JRE + development tools.
- **JRE** (Java Runtime Environment): Executes Java applications.

## Java Versions

- **OpenJDK**: The open-source implementation of Java SE, free to use.
- **Oracle JDK**: Oracle's version, including commercial features.
- **Java Corretto**: Amazon's free, open-source distribution of the JDK, optimized for AWS.
- **Latest LTS Versions**: Java 11, Java 17.
- **Java 22 & others**: Available in OpenJDK, offering new language features.

## Installation

### Windows/Linux/Mac

1. **Download OpenJDK**: 
   - Visit [AdoptOpenJDK](https://adoptopenjdk.net/) or [Oracle JDK](https://www.oracle.com/java/technologies/javase-downloads.html).
   - Visit Amazon for  [Amazon corretto 17](https://docs.aws.amazon.com/corretto/latest/corretto-17-ug/generic-linux-install.html)
   - Download the appropriate installer.

2. **Install**:
   - Follow the installation instructions.
   - Set the `JAVA_HOME` environment variable.
   - Add Java to your system's PATH.

### Verify Installation

```bash
java -version
```

## Virtual Environments with SDKMAN

- **SDKMAN**: A tool to manage parallel versions of multiple SDKs, including Java.

### Installation

```bash
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
```

### Usage

- **List Available Java Versions**:
    ```bash
    sdk list java
    ```

- **Install a Version**:
    ```bash
    sdk install java 11.0.11-open
    ```

- **Switch Between Versions**:
    ```bash
    sdk use java 11.0.11-open
    ```

## Summary of Java vs. JavaFX

- **Swing**: Older, stable, widely used for enterprise applications.
- **JavaFX**: Modern, supports rich UI features like CSS and multimedia.

### When to Use

- **Swing**: Simple GUIs, legacy systems.
- **JavaFX**: Modern applications with rich graphics.

---

This cheatsheet provides a quick overview of the essential Java concepts, including installation and usage tips for managing different Java versions.