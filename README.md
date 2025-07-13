# 📖 **README.md**

````markdown
# 🖤 ByVM: Binary Virtual Machine

ByVM is a lightweight, recursive **binary virtual machine** designed for experimentation with symbolic computation, meta-programming, and FFI (Foreign Function Interfaces). Inspired by previous ternary-based architectures, ByVM reimagines the core as a binary system to align with modern hardware.

---

## 🚀 Features

- 🧠 **Minimal Binary Core**: Stack, registers, memory, and a simple instruction set.
- 🔌 **C FFI Support**: Call external C functions directly from ByVM programs.
- 🪜 **Recursive Structure**: Stack operations (`PUSH`/`POP`) prepare for higher-order symbolic layers.
- 📖 **Literate Programming**: Core implemented in `.cweb`.

---

## 🏗 Example Program

```assembly
LOAD R0, 42          ; Load 42 into register 0
CALL_FFI 0x01        ; Call external C function 1
CALL_FFI 0x02        ; Call external C function 2
HALT                 ; Stop execution
````

Expected output:

```
[C FFI] Hello from C function!
[C FFI] Value in Register 0: 42
```

---

## 📦 Build Instructions

### 🛠 Prerequisites

* GCC or Clang
* `ctangle` and `cweave` for literate programming

### 🖥 Build and Run

```bash
# Tangle the literate source into C
ctangle src/core/vm.cweb

# Compile the binary VM
gcc vm.c -o byvm

# Run ByVM
./byvm
```

---

## 🌐 Project Structure

```
byvm/
├── src/core/         # Core VM (.cweb literate programming)
├── examples/         # Sample programs and plugins
├── docs/             # Architecture and design notes
├── tests/            # Unit tests
```

---

## 🛤 Roadmap

✅ Minimal binary VM core
✅ Stack operations (`PUSH`/`POP`)
✅ C-only FFI layer
🔜 Python FFI (embed Python interpreter)
🔜 Symbolic meta-layer design
🔜 Dynamic plugin loading

---

## 📝 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## ✨ Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to contribute.

````

---

# 📄 **LICENSE (MIT)**  

```text
MIT License

Copyright (c) 2025 t81dev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
````
