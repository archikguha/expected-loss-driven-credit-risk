
from sklearn.calibration import CalibratedClassifierCV

def calibrate(model, X, y):
    cal = CalibratedClassifierCV(model, method="sigmoid")
    cal.fit(X, y)
    return cal
