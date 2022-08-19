import cv2
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, help='video path', default='./data/Video_003.avi')
parser.add_argument('--output', type=str, help='output folder', default='./data')
args = parser.parse_args()

print('Loading file {}.'.format(args.input))
capture = cv2.VideoCapture(args.input)


def resize_image(image, size, keep_aspect_ratio=False):
    if not keep_aspect_ratio:
        resized_frame = cv2.resize(image, size)
    else:
        h, w = image.shape[:2]
        scale = min(size[1] / h, size[0] / w)
        resized_frame = cv2.resize(image, None, fx=scale, fy=scale)
    return resized_frame

if not capture.isOpened():
    print('Unable to open: ' + args.input)
    exit(0)

frame_number = 0


while True:
    ret, frame = capture.read()
    if frame is None:
        break

    scaled = resize_image(frame,(240,320),True)

    localpath = os.path.join(args.output,f"frame{frame_number}.png")
    cv2.imwrite(localpath, scaled)

    frame_number += 1

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()
