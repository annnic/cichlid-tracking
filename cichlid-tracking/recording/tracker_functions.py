# Functions which are used for fish tracking

import yaml
import numpy as np
import cv2
import os
import datetime


def roi_input():
    """input function for 1. asking how many ROIs"""
    while True:
        roi_nums = input("How many ROIs would you like to select?: ")
        try:
            rois = int(roi_nums)
            print("Will do", roi_nums, "region/s of interest")
            return rois
        except ValueError:
            print("Input must be an integer")


# load yaml configuration file
def load_yaml(rootdir, name):
    """ (str, str) -> (dict)
    finds name.yaml file in given dir and opens and returns it as a  dict"""
    try:
        filename = (rootdir + "/" + name + ".yaml")
        print(filename)
        with open(filename) as file:
            params = yaml.load(file, Loader=yaml.FullLoader)
            print(params)
            return params
    except:
        print("couldn't find " + name + ".yaml in folder: " + rootdir)
        params = {}
        return params

    # if len(glob.glob(rootdir + "/" + name + "*" + ".yaml")) != 1:
    #     print("too many or too few roi files in folder:" + params["folder"])
    # else:
    #     with open(glob.globrootdir + "/" + name + "*" + ".yaml")[0]) as file:
    #         rois = yaml.load(file, Loader=yaml.FullLoader)
    #         print(rois)


def define_roi_still(image_input, folder_path):
    roi_num = roi_input()
    image = np.array(image_input, copy=True)
    # rr = np.arange(4 * roi_num).reshape(roi_num, 4)
    scalingF = 1
    dict_file = {"cam_ID": "na"}
    height, width = image.shape
    if roi_num == 0:
        dict_file["roi_0"] = tuple([0, 0, width, height])
    else:
        for roi in range(roi_num):
            frameRS = cv2.resize(image, (int(width / scalingF), int(height / scalingF)))
            rr = cv2.selectROI(("Select ROI" + str(roi)), frameRS)
            # output: (x,y,w,h)
            dict_file["roi_" + str(roi)] = tuple(i * scalingF for i in rr)
            # add in ROIs
            start_point = (rr[0], rr[1])
            end_point = (rr[0] + rr[2], rr[1] + rr[3])
            cv2.rectangle(image, start_point, end_point, 220, 2)
            cv2.destroyAllWindows()
        print(dict_file)

    with open(os.path.join(folder_path, "roi_file.yaml"), "w") as file:
        documents = yaml.dump(dict_file, file)

    print("File has now been saved in specified folder as roi_file.yaml")


def background_vid(videofilepath, nth_frame, percentile):
    """ (str, int, int, int)
     This function will create a median image of the defined area"""
    try:
        cap = cv2.VideoCapture(videofilepath)
    except:
        print("problem reading video file, check path")
        return

    counter = 0
    gatheredFramess = []
    while (cap.isOpened()):
        ret, frame = cap.read()
        if frame is None:
            break
        if counter % nth_frame == 0:
            print("Frame {}".format(counter))
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # settings with Blur settings for the video loop
            gatheredFramess.append(image)
        counter += 1

    background = np.percentile(gatheredFramess, int(percentile), axis=0).astype(dtype=np.uint8)
    cv2.imshow('Calculated Background from {} percentile'.format(percentile), background)

    # background = np.percentile(frameMedian, 90, axis=0).astype(dtype=np.uint8)
    # cv2.imshow('Calculated background', background)

    date = datetime.datetime.now().strftime("%Y%m%d")
    vid_name = videofilepath[0:-4]
    # vid_name = os.path.split(videofilepath)[1][0:-4]
    # vid_folder_path = os.path.split(videofilepath)[0]
    cv2.imwrite('{}_per{}_background.png'.format(vid_name, percentile), background)

    cap.release()
    cv2.destroyAllWindows()
    return background


def print_roi(roi_path, video_path):
    rois = load_yaml(roi_path, "roi_file")

    try:
        cap = cv2.VideoCapture(video_path)
    except:
        print("problem reading video file, check path")
        return False

    while (cap.isOpened()):
        ret, frame = cap.read()
        if frame is None:
            break

        for roi in range(0, len(rois) - 1):
            # for the frame define an ROI and crop image
            curr_roi = rois["roi_" + str(roi)]
            # add in ROIs
            start_point = (curr_roi[0], curr_roi[1])
            end_point = (curr_roi[0] + curr_roi[2], curr_roi[1] + curr_roi[3])
            cv2.rectangle(frame, start_point, end_point, 220, 2)
            cv2.imshow('Roi printed on video frame', frame)
        return frame