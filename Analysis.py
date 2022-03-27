import matplotlib.pyplot as plt
import cv2
if __name__ == '__main__':
    cap = cv2.VideoCapture("/Users/prasannasmac/Documents/Capstone/testvideo.mp4")
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(length)

    x = ['With Edge', 'Without Edge']
    y = [10, 394]
    plt.ylabel('No. of frames')
    plt.title('Payload Reduction')
    plt.bar(x, y, width=0.2, color='green')
    plt.savefig("/Users/prasannasmac/Documents/Capstone/graph.png")