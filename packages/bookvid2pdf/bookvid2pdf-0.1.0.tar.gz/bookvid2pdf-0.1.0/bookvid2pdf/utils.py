import os
import sys
import cv2
import pytesseract
import numpy as np
from scipy.signal import find_peaks
from fpdf import FPDF
from tqdm import tqdm


def set_tesseract_cmd(tesseract_path: str):
    pytesseract.pytesseract.tesseract_cmd = tesseract_path


if sys.platform == "win32":
    set_tesseract_cmd(r"C:\Program Files\Tesseract-OCR\tesseract.exe")


def calculate_blurriness(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()


def read_video(video_path, stride: int = 5):
    video = cv2.VideoCapture(video_path)
    frames = []
    i = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break
        if i % stride == 0:
            frames.append(frame)
        i += 1
    video.release()
    return frames


def get_page(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = (blurred > 128).astype(np.uint8)

    contours, _ = cv2.findContours(
        edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    x, y, w, h = gray.shape[0], gray.shape[1], 0, 0
    tot_area = x * y
    tot_area_frac = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        area_frac = area / tot_area
        if area_frac > 0.25:
            tot_area_frac += area_frac
            x1, y1, w1, h1 = cv2.boundingRect(cnt)
            x_new = min(x1, x)
            y_new = min(y1, y)
            w = max(x1 + w1, x + w) - x_new
            h = max(y1 + h1, y + h) - y_new
            x, y = x_new, y_new
    if w == 0 or h == 0:
        return frame, 0
    return frame[y : y + h, x : x + w], tot_area_frac


def smooth_values(values, window_size=5):
    kernel = np.ones(window_size) / window_size
    return np.convolve(values, kernel, mode="same")


def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation=inter)

    return resized


def create_pdf(frames, selected_frames, output_path):
    pdf = FPDF()
    for index in selected_frames:
        page = get_page(frames[index])[0]
        p_h, p_w, _ = page.shape
        frame = (
            image_resize(page, width=720)
            if p_h / p_w < 16 / 9
            else image_resize(page, height=1280)
        )
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        width, height, _ = frame.shape

        # px to mm
        width, height = float(width * 0.264583), float(height * 0.264583)

        pdf.add_page()
        pdf.image(
            x=0,
            y=0,
            w=height,
            h=width,
            type="",
            link="",
            name=cv2.imencode(".jpg", frame)[1].tobytes(),
        )
    pdf.output(output_path)


def get_text(page):
    gray = cv2.cvtColor(page, cv2.COLOR_BGR2GRAY)
    return pytesseract.image_to_string(gray)


def get_optimality(frame):
    page, tot_area_frac = get_page(frame)
    if tot_area_frac < 0.5:
        return 0
    len_text = 500 + len(get_text(page))
    blur = calculate_blurriness(page)

    return max(0, (len_text - blur) * tot_area_frac)


def vid2pdf(video_path: str, output_path: str = "output.pdf", log: bool = False):
    """Convert the video of the pages of a book being turned to a PDF of the book.

    Args:
        video_path (str): Path to the video file.
        output_path (str, optional): Path to the output PDF file. Defaults to "output.pdf".
        log (bool, optional): Boolean indicating whether the stages of the conversion should be printed to stdout. Defaults to False.
    """
    if not log:
        f = open(os.devnull, "w")
        sys.stdout = f

    print("Reading video...")
    frames = read_video(video_path)

    print("Calculating Blurriness...")
    optimality_values = [get_optimality(frame) for frame in tqdm(frames)]

    print("Selecing Frames...")
    peaks, _ = find_peaks(smooth_values(optimality_values, 5), width=3)

    print("Creating PDF...")
    create_pdf(frames, peaks, output_path)

    sys.stdout = sys.__stdout__
