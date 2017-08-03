# Image Upscale Dataset Generator

This script generates dataset used in example subjective comparison of image upscale methods with [Subjectify.us] platform described in [this video][youtube].

The script downscales images from `input` directory and then upscales (back to original size) with the following methods:

* Nearest-neighbor
* Bilinear
* Bicubic

Upscaled images are stored in `output` directory.

## Requirements

This script uses OpenCV2 Python bindings.

```
pip install opencv-python
```

[Subjectify.us]: http://subjectify.us/
[youtube]: https://www.youtube.com/watch?v=PiQNkXmSJ2I
