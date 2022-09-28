
<h3 align="center">PyLoris</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/YoloFTW/pylorris.svg)](https://github.com/YoloFTW/pylorris/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/YoloFTW/pylorris.svg)](https://github.com/YoloFTW/pylorris/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

## 📝 Table of Contents

- [About](#about)

- [Usage](#usage)

- [Authors](#authors)

</br>

## 🧐 About <a name = "about"></a>

PyLoris is a tool for testing if a website is vulnerable to attacks that implement filling the target webservers maximum concurrent connection pool to try and deny additional
connection attempts from clients.

</br>

## Installing

For Installation With PyPI

```sh
pip install PyLoris
```

</br>

## 🎈 Usage <a name="usage"></a>

Basic usage

```python
from PyLoris import SlowLoris

SlowLorisTest = SlowLoris("your-site.com", number_of_open_socket_to_test)

SlowLorisTest.start()

#returns true or false
print(SlowLorisTest.vulnerable)
```
</br>

To get the number of times a socket was closed

```python
#returns int of closed sockets
print(SlowLorisTest.closedSockets)
```
</br>

To get the number of times a socket was responsive

```python
#returns int of responsive sockets
print(SlowLorisTest.responsiveSockets)
```


## ✍️ Authors <a name = "authors"></a>

- [@YoloFTW](https://github.com/YoloFTW)


