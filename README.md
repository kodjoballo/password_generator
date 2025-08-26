# 🔑 Password Generator
## 📌 Description

This is a customizable password generator that creates strong, random passwords based on user preferences.
Users can choose:

Minimum password length

Whether to include numbers

Whether to include special characters

### 🛠️ Requirements

Python 3.x

### ▶️ How to Run

```js
python.exe password_generator.py
```

or from any python interpreter

### 🎮 Example Usage

```js
What is the wanted length of the password:? 12
Do you want the password to include numbers: y
Do you want the password to include special character: y

Your password is @n8%LxP9k!2Q
```


### Screenshot

<p align="center">

![image alt](https://github.com/kodjoballo/password_generator/blob/main/password_generator.png?raw=true)

</p>



### 🚀 Suggested Improvements

Ensure variety

Currently, the password could theoretically miss numbers or symbols if user wants them, but your while-loop logic covers this nicely ✅.

Still, you can guarantee at least 1 digit & 1 special character by inserting them explicitly before filling the rest.

Hide password length restriction

Maybe enforce a minimum length like 8 characters (for security best practice).

Add strength evaluation

After generating, show whether the password is weak, medium, or strong.

Option to generate multiple passwords

Sometimes users want a list of 5–10 random passwords.

Clipboard support (advanced)

Use pyperclip to copy the password directly.

### code source ☺️👇
[code source](https://github.com/kodjoballo/password_generator/blob/main/password_generator.py)
