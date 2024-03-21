# VisTabNet
This package introduces VisTabNet - Vision Transformer-based Tabular Data Classifier. 

## Usage
```python
from vistabnet import VisTabNetClassifier

X_train, y_train, X_test, y_test = ... # Load your data here. Y should be label encoded, not one-hot encoded.

model = VisTabNetClassifier(input_features=X_train.shape[1], classes=len(np.unique(y_train)), device="cuda:1")
model.fit(X_train, y_train, eval_X=X_test, eval_y=y_test)

y_pred = model.predict(X_test)
acc = balanced_accuracy_score(y_test_, y_pred)
print(f"Balanced accuracy: {acc}")
```

## Installation
```bash
pip install vistabnet
```