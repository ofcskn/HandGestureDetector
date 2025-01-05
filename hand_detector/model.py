import onnxruntime as ort

class HandModel:
    """Handles loading and inference of the hand detection model."""
    def __init__(self, model_path):
        self.model_path = model_path
        self.session = self._load_model()

    def _load_model(self):
        """Loads the ONNX model."""
        try:
            return ort.InferenceSession(self.model_path)
        except Exception as e:
            raise RuntimeError(f"Failed to load model: {e}")

    def predict(self, inputs):
        """Runs inference on the provided inputs."""
        try:
            return self.session.run(None, inputs)
        except Exception as e:
            raise RuntimeError(f"Inference failed: {e}")
