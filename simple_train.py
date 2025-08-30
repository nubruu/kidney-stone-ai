import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Sequential

# Disable GPU to avoid mutex issues
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# Set threading to avoid mutex lock issues
tf.config.threading.set_inter_op_parallelism_threads(1)
tf.config.threading.set_intra_op_parallelism_threads(1)

def create_simple_model():
    model = Sequential([
        EfficientNetB0(weights='imagenet', include_top=False, input_shape=(224, 224, 3)),
        GlobalAveragePooling2D(),
        Dropout(0.3),
        Dense(128, activation='relu'),
        Dropout(0.2),
        Dense(1, activation='sigmoid')
    ])
    
    # Freeze base model
    model.layers[0].trainable = False
    
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    return model

def main():
    print("Creating simple kidney stone detection model...")
    
    # Check if dataset exists
    dataset_path = "Kidney Ultrasound Images Stone and No Stone"
    if not os.path.exists(dataset_path):
        print(f"Dataset not found at: {dataset_path}")
        print("Please ensure the dataset folder exists with Normal/ and stone/ subfolders")
        return
    
    # Simple data generator
    datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2
    )
    
    try:
        # Load data
        train_generator = datagen.flow_from_directory(
            dataset_path,
            target_size=(224, 224),
            batch_size=16,
            class_mode='binary',
            subset='training',
            classes=['Normal', 'stone']
        )
        
        val_generator = datagen.flow_from_directory(
            dataset_path,
            target_size=(224, 224),
            batch_size=16,
            class_mode='binary',
            subset='validation',
            classes=['Normal', 'stone']
        )
        
        # Create and train model
        model = create_simple_model()
        print("Training model...")
        
        history = model.fit(
            train_generator,
            epochs=5,  # Reduced epochs for quick training
            validation_data=val_generator,
            verbose=1
        )
        
        # Save model
        model.save('kidney_stone_model.h5')
        print("✅ Model saved as 'kidney_stone_model.h5'")
        print("You can now start the backend: python3 backend.py")
        
    except Exception as e:
        print(f"Training failed: {e}")
        print("Try running with fewer resources or check dataset structure")

if __name__ == "__main__":
    main()