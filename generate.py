'''Generate dataset for simple comparison of image upscale methods with Subjectify.us.'''

import os

import cv2


INPUT = 'input/'
OUTPUT = 'output/'
TEST_CASES = ['lena', 'cameraman']
SCALES = [2, 3, 4]
METHODS = {
    'Nearest-neighbor': cv2.INTER_NEAREST,
    'Bilinear': cv2.INTER_LINEAR,
    'Bicubic': cv2.INTER_CUBIC,
}

for test_case in TEST_CASES:
    # Ensure output directory for current test-case.
    if not os.path.exists(os.path.join(OUTPUT, test_case)):
        os.makedirs(os.path.join(OUTPUT, test_case))

    ground_truth = cv2.imread(os.path.join(INPUT, test_case + '.png'))
    # Save ground-truth result {test_case_name}/ground-truth.png.
    cv2.imwrite(
        os.path.join(
            OUTPUT,
            '%s/Ground-truth.png' % test_case),
        ground_truth)

    for scale in SCALES:
        # Downscale ground-truth image.
        downscaled = cv2.resize(
            ground_truth,
            (0, 0),
            fx=1.0/scale,
            fy=1.0/scale,
            interpolation=cv2.INTER_AREA)
        # Try to recover original image with various upscale methods.
        for method_name, method_id in METHODS.items():
            upscaled = cv2.resize(
                downscaled,
                (0, 0),
                fx=scale,
                fy=scale,
                interpolation=method_id)

            # Save result as {test_case_name}/{method_name}@upscale={scale}.png.
            cv2.imwrite(
                os.path.join(
                    OUTPUT,
                    '%s/%s@upscale=%d.png' % (test_case, method_name, scale)),
                upscaled)
