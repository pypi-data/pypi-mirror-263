# MOGdevice ‒ moglabs device class

This is an unofficial repository. It uses the [Python drivers](https://www.moglabs.com/support/software/connection/mogdevice_py_v1.2.zip) from the [MOGLabs website](https://www.moglabs.com) and turned it into a installable package.

[![PyPI](https://img.shields.io/pypi/v/mogdevice?color=blue)](https://pypi.org/project/mogdevice/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Basic functionality for MOGLabs devices

You can import a class that allows for communication with MOGLabs devices by running

```python
from mogdevice import MOGDevice
```

and connecting to a device by running

```python
dev = MOGDevice("IP_ADDRESS_OF_DEVICE")
```

## High-level class for MOGLabs QRF

Based on the `MOGDevice` class, this package provides a higher level class for the 
Quad RF Synthesizer (QRF) that implements a subset of the commands as methods and
properties. Connect to a device with

```python
from mogdevice.qrf import QRF
qrf = QRF("IP_ADDRESS_OF_DEVICE")
```


## Authors

Copyright (c) 2017 - present, MOG Laboratories Pty Ltd, Australia.
Copyright (c) 2024, Bastian Leykauf
