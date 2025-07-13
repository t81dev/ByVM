# Contributing to ByVM

Welcome! 👋 We’re thrilled you want to contribute to the Binary Virtual Machine (ByVM). This document will guide you through the contribution process.

## 🧠 Philosophy
ByVM is recursive, symbolic, and modular by design. We value:
- **Simplicity**: Keep the core binary VM minimal.
- **Extensibility**: Use FFI for complex features.
- **Clarity**: Document your work (literate programming encouraged).

## 🚀 How to Contribute

### 🛠 Setup
1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR-USERNAME/byvm.git
   cd byvm
Create a branch for your work:
git checkout -b feature/my-feature
Build and run tests:
make
make test

## 📦 Code Contributions
Core VM: edit src/core/
Symbolic/meta layer: edit src/symbolic/
FFI plugins: edit src/ffi/ or examples/

## ✅ Commit Guidelines
Use clear commit messages:
[core] Add recursive bitwise AND operation
[ffi] Initial Python binding
[docs] Add architecture diagram
Write tests for new features.

## 📄 Documentation
Update docs/ for architecture or API changes.
For .cweb files, ensure code and narrative remain in sync.

## 🗨 Communication
Open an issue to discuss big changes before starting.
Join discussions on roadmap items in docs/roadmap.md.

##📝 License

By contributing, you agree that your contributions will be licensed under the MIT License.


