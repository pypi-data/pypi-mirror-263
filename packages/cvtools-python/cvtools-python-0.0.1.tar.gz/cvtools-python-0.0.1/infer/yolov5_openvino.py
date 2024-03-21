"""
this file is to demonstrate how to use openvino to do inference with yolov5 model exported from onnx to openvino format
"""

from typing import List

import cv2
import numpy as np
import time
from pathlib import Path
from openvino.runtime import Core


def build_model(model_path: str) -> cv2.dnn_Net:
    """
    build the model with opencv dnn module
    Args:
        model_path: the path of the model, the model should be in onnx format

    Returns:
        the model object
    """
    # load the model
    core = Core()
    model = core.read_model(model_path)
    for device in core.available_devices:
        print(device)
    compiled_model = core.compile_model(model=model, device_name="AUTO")
    # output_layer = compiled_model.output(0)
    return compiled_model


def inference(image: np.ndarray, model: cv2.dnn_Net) -> np.ndarray:
    """
    inference the model with the input image
    Args:
        image: the input image in numpy array format, the shape should be (height, width, channel),
        the color channels should be in GBR order, like the original opencv image format
        model: the model object

    Returns:
        the output data of the model, the shape should be (1, 25200, nc+5), nc is the number of classes
    """
    # image preprocessing, include resize, normalization, channel swap like BGR to RGB, and convert to blob format
    # get a 4-dimensional Mat with NCHW dimensions order.
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (INPUT_WIDTH, INPUT_HEIGHT), swapRB=True, crop=False)

    output_layer = model.output(0)
    outs = model([blob])[output_layer]

    return outs


def xywh_to_xyxy(bbox_xywh, image_width, image_height):
    """
    Convert bounding box coordinates from (center_x, center_y, width, height) to (x_min, y_min, x_max, y_max) format.

    Parameters:
        bbox_xywh (list or tuple): Bounding box coordinates in (center_x, center_y, width, height) format.
        image_width (int): Width of the image.
        image_height (int): Height of the image.

    Returns:
        tuple: Bounding box coordinates in (x_min, y_min, x_max, y_max) format.
    """
    center_x, center_y, width, height = bbox_xywh
    x_min = max(0, int(center_x - width / 2))
    y_min = max(0, int(center_y - height / 2))
    x_max = min(image_width - 1, int(center_x + width / 2))
    y_max = min(image_height - 1, int(center_y + height / 2))
    return x_min, y_min, x_max, y_max


def wrap_detection(
        input_image: np.ndarray,
        output_data: np.ndarray,
        labels: List[str],
        confidence_threshold: float = 0.8
) -> (List[int], List[float], List[List[int]]):
    # the shape of the output_data is (25200,5+nc),
    # the first 5 elements are [x, y, w, h, confidence], the rest are prediction scores of each class

    image_width, image_height, _ = input_image.shape
    x_factor = image_width / INPUT_WIDTH
    y_factor = image_height / INPUT_HEIGHT

    # transform the output_data[:, 0:4] from (x, y, w, h) to (x_min, y_min, x_max, y_max)
    # output_data[:, 0:4] = np.apply_along_axis(xywh_to_xyxy, 1, output_data[:, 0:4], image_width, image_height)

    indices = cv2.dnn.NMSBoxes(output_data[:, 0:4].tolist(), output_data[:, 4].tolist(), 0.6, 0.4)

    # print(indices)
    raw_boxes = output_data[:, 0:4][indices]
    raw_confidences = output_data[:, 4][indices]
    raw_class_prediction_probabilities = output_data[:, 5:][indices]

    criteria = raw_confidences > confidence_threshold
    raw_class_prediction_probabilities = raw_class_prediction_probabilities[criteria]
    raw_boxes = raw_boxes[criteria]
    raw_confidences = raw_confidences[criteria]

    bounding_boxes, confidences, class_ids = [], [], []
    for class_prediction_probability, box, confidence in zip(raw_class_prediction_probabilities, raw_boxes,
                                                             raw_confidences):
        # find the least and most probable classes' indices and their probabilities
        # min_val, max_val, min_loc, mac_loc = cv2.minMaxLoc(class_prediction_probability)
        most_probable_class_index = np.argmax(class_prediction_probability)
        label = labels[most_probable_class_index]
        confidence = float(confidence)
        x, y, w, h = box
        left = int((x - 0.5 * w) * x_factor)
        top = int((y - 0.5 * h) * y_factor)
        width = int(w * x_factor)
        height = int(h * y_factor)
        bounding_box = [left, top, width, height]
        bounding_boxes.append(bounding_box)
        confidences.append(confidence)
        class_ids.append(most_probable_class_index)

    return class_ids, confidences, bounding_boxes


coco_class_names = ["Ascaris Egg",
        "Liver Fluke Egg",
        "Aided",
        "Hookworm Egg",  #钩虫卵
        "Pinworm Egg",  #蛲虫卵
        "WhipwormEgg",  #鞭虫卵
        "TapewormEgg",  # 带绦虫卵
        "SchistosomaEgg",  #血吸虫卵
        "FasciolopsisEgg" , #姜片虫卵
        "LungFlukeEgg",
        "Trichina",
        "AscarisQC",
        "LiverFlukeQC",
        "HookwormQC",
        "WhipwormQC"]
# generate different colors for coco classes
colors = np.random.uniform(0, 255, size=(len(coco_class_names), 3))

INPUT_WIDTH = 1280
INPUT_HEIGHT = 1280
CONFIDENCE_THRESHOLD = 0.8
NMS_THRESHOLD = 0.8


def video_detector(video_src):
    cap = cv2.VideoCapture(video_src)

    # 3. inference and show the result in a loop
    while cap.isOpened():
        success, frame = cap.read()
        start = time.perf_counter()
        if not success:
            break

        # image preprocessing, the trick is to make the frame to be a square but not twist the image
        row, col, _ = frame.shape  # get the row and column of the origin frame array
        _max = max(row, col)  # get the max value of row and column
        input_image = np.zeros((_max, _max, 3), dtype=np.uint8)  # create a new array with the max value
        input_image[:row, :col, :] = frame  # paste the original frame  to make the input_image to be a square

        # inference
        output_data = inference(input_image, net)  # the shape of output_data is (1, 25200, 85)

        # define coco dataset class names dictionary

        # 4. wrap the detection result
        class_ids, confidences, boxes = wrap_detection(input_image, output_data[0], coco_class_names)

        # wrap_detection(input_image, output_data[0], coco_class_names) ##

        # 5. draw the detection result on the frame
        for (class_id, confidence, box) in zip(class_ids, confidences, boxes):
            color = colors[int(class_id) % len(colors)]
            label = coco_class_names[int(class_id)]

            # cv2.rectangle(frame, box, color, 2)

            # print(type(box), box[0], box[1], box[2], box[3], box)
            xmin, ymin, width, height = box
            cv2.rectangle(frame, (xmin, ymin), (xmin + width, ymin + height), color, 2)

            cv2.putText(frame, str(label), (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        # 6. show the frame
        frame = cv2.resize(frame,(640,640))
        cv2.imshow("frame", frame)
        cv2.waitKey(0)

        # # 7. press 'q' to exit
        # if cv2.waitKey(1) == ord('q'):
        #     break

    # 8. release the capture and destroy all windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # there are 4 steps to use opencv dnn module to inference onnx model exported by yolov5 and show the result

    # 1. load the model
    model_path = Path("./runs/train/low_m_1_16/weights/best.xml")
    # model_path = Path("weights/POT_INT8_openvino_model/yolov5s_int8.xml")
    net = build_model(str(model_path))
    # 2. load the video capture
    video_source = 0
    # video_source = 'rtsp://admin:aoto12345@192.168.8.204:554/h264/ch1/main/av_stream'
    video_detector('./images/006.jpg')

    exit(0)
