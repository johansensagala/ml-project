import tflite_support.metadata as metadata_fb
from pathlib import Path

path_model = "model.tflite"

# Membaca metadata model
model_path = Path(path_model)
model_buffer = model_path.read_bytes()

# Mendapatkan versi TensorFlow Lite dari metadata
model_meta = metadata_fb.ModelMetadata.GetRootAsModelMetadata(model_buffer, 0)
tflite_version = model_meta.Version()

print(f"Versi TensorFlow Lite: {tflite_version}")