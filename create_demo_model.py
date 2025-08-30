import tensorflow as tf
import numpy as np

# Create a simple demo model that works
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(224, 224, 3)),
    tf.keras.layers.Conv2D(32, 3, activation='relu'),
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Save demo model
model.save('kidney_stone_model.h5')
print("✅ Demo model created: kidney_stone_model.h5")
print("Start backend: python3 backend.py")