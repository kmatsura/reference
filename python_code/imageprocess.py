import numpy as np
'''
img file should be read by cv2
'''

class Imageprocess:
    def __init__(self, img):
        self.img = img

    def rgb2bgr(self):
        img = self.img
        red = img[:, :, 2].copy()
        blue = img[:, :, 0].copy()
        img2 = img.copy()
        img2[:, :, 2] = blue
        img2[:, :, 0] = red
        return img2

    def gray(self):
        img = self.img
        b = img[:, :, 0].copy()
        g = img[:, :, 1].copy()
        r = img[:, :, 2].copy()
        gray = 0.0722 * b + 0.7152 * g + 0.2126 * r
        gray = gray.astype(np.uint8)
        return gray

    def binalization(self, th=128):
        img = self.img
        img[img < th] = 0
        img[img >= th] = 255
        return img

    def rgb2hsv(self):
        img = self.img.copy() / 255.
        hsv = np.zeros_like(img, dtype=np.float32)
        max_v = np.max(img, axis=2).copy()
        min_v = np.min(img, axis=2).copy()
        min_arg = np.argmin(img, axis=2)
        hsv[..., 0][np.where(max_v == min_v)] = 0
        ind = np.where(min_arg == 0)
        hsv[..., 0][ind] = 60 * (img[..., 1][ind] - img[..., 2][ind]) / (max_v[ind] - min_v[ind]) + 60
        ind = np.where(min_arg == 2)
        hsv[..., 0][ind] = 60 * (img[..., 0][ind] - img[..., 1][ind]) / (max_v[ind] - min_v[ind]) + 180
        ind = np.where(min_arg == 1)
        hsv[..., 0][ind] = 60 * (img[..., 2][ind] - img[..., 0][ind]) / (max_v[ind] - min_v[ind]) + 300
        hsv[..., 1] = max_v.copy() - min_v.copy()
        hsv[..., 2] = max_v.copy()
        return hsv

    def transpose_hue(self, hsv):
        hsv = hsv.copy()
        hsv[..., 0] = (hsv[..., 0] + 180) % 360 
        return hsv

    def hsv2rgb(self, hsv):
        img = self.img.copy() / 255.
    
        max_v = np.max(img, axis =2).copy()
        min_v = np.min(img, axis = 2).copy()
    
        out = np.zeros_like(img)
    
        H = hsv[..., 0]
        S = hsv[..., 1]
        V = hsv[..., 2]
    
        C = S
        H_ = H / 60.0
        X = C * (1 - np.abs(H_ % 2 - 1))
        Z = np.zeros_like(H)
    
        vals = [[Z, X, C], [Z, C, X], [X, C, Z], [C, X, Z], [C, Z, X], [X, Z, C]]
    
        for i in range(6):
            ind = np.where((i <= H_) & (H_ < (i + 1)))
            for j in range(3):
                out[..., j][ind] = (V - C)[ind] + vals[i][j][ind]
        out[np.where(max_v == min_v)] = 0
        out = np.clip(out, 0, 1)
        out = (out * 255).astype(np.uint8)
    
        return out