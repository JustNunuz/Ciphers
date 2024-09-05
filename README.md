# Ciphers Repository

Welcome to the **Ciphers Repository**! This repository contains a collection of cryptographic cipher implementations, both **symmetric** and **asymmetric** encryption algorithms. It serves as a comprehensive resource for those learning about cryptography or looking for references when implementing these algorithms in real-world scenarios.

## Overview of Encryption

Encryption is the process of converting **plaintext** into **ciphertext**, making it unreadable without the corresponding decryption algorithm. It is a critical component of information security, ensuring that sensitive data is protected from unauthorized access while maintaining its **confidentiality**, **integrity**, and **authenticity**.

## Types of Ciphers

Ciphers are categorized based on their functionality and characteristics. Below are the key types of ciphers you’ll find in this repository:

### 1. **Symmetric Ciphers**
- Use the **same key** for both encryption and decryption.
- Common algorithms: **AES**, **DES**, **Blowfish**.

### 2. **Asymmetric Ciphers**
- Use a pair of keys: one for encryption (**public key**) and one for decryption (**private key**).
- Common algorithms: **RSA**, **ElGamal**.

### 3. **Hash Functions**
- Produce a fixed-size output (hash) from input data of any size, commonly used for data integrity verification.
- Common algorithms: **SHA-256**, **MD5**.

### 4. **Block Ciphers**
- Encrypt data in **fixed-size blocks** (e.g., 128 bits for AES).
- Common algorithms: **AES**, **DES**.

### 5. **Stream Ciphers**
- Encrypt data one bit or byte at a time, ideal for streaming data.
- Common algorithms: **RC4**, **ChaCha20**.

---

## Cipher Implementations in this Repository

This repository contains the following cipher implementations:

| Folder           | Content                     | Type of Cipher   |
| ---------------- | --------------------------- | ---------------- |
| Two Way Cipher   | **Fernet Cipher**            | Symmetric Cipher |
