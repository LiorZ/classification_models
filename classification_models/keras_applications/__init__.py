import tensorflow.keras
from .keras_applications.keras_applications import *

set_keras_submodules(
    backend=tensorflow.keras.backend,
    layers=tensorflow.keras.layers,
    models=tensorflow.keras.models,
    engine=tensorflow.keras.engine,
    utils=tensorflow.keras.utils,
)
