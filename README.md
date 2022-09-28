<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Project Title</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/YoloFTW/pylorris.svg)](https://github.com/YoloFTW/pylorris/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/YoloFTW/pylorris.svg)](https://github.com/YoloFTW/pylorris/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Few lines describing your project.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Usage](#usage)

- [Authors](#authors)

## 🧐 About <a name = "about"></a>

PyLoris is a tool for testing if a website is vulnerable to attacks that implement filling the target webservers maximum concurrent connection pool to try and deny additional
connection attempts from clients.

### Installing

For Installation With PyPI

```sh
$ pip install PyLoris
```

## 🎈 Usage <a name="usage"></a>

```python
from PyLoris import SlowLoris

SlowLorisTest = SlowLoris("your-site.com", 2)

SlowLorisTest.start()

print(SlowLorisTest.vulnerable)
```
## ✍️ Authors <a name = "authors"></a>

- [@YoloFTW](https://github.com/YoloFTW)


