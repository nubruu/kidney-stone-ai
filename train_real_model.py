import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout, BatchNormalization
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
import os

# Disable GPU issues on Mac
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
tf.config.threading.set_inter_op_parallelism_threads(1)
tf.config.threading.set_intra_op_parallelism_threads(1)

def create_model():
    model = Sequential([
        EfficientNetB0(
            weights='imagenet',
            include_top=False,
            input_shape=(224, 224, 3)
        ),
        GlobalAveragePooling2D(),
        BatchNormalization(),
        Dropout(0.5),
        Dense(256, activation='relu'),
        BatchNormalization(),
        Dropout(0.3),
        Dense(128, activation='relu'),
        Dropout(0.2),
        Dense(1, activation='sigmoid')
    ])
    
    # Freeze base model initially
    model.layers[0].trainable = False
    
    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss='binary_crossentropy',
        metrics=['accuracy', 'precision', 'recall']
    )
    
    return model

def train_model():
    dataset_path = "Kidney Ultrasound Images Stone and No Stone"
    
    if not os.path.exists(dataset_path):
        print(f"❌ Dataset not found: {dataset_path}")
        print("Please ensure dataset exists with Normal/ and stone/ folders")
        return
    
    # Check dataset size
    normal_count = len(os.listdir(os.path.join(dataset_path, "Normal")))
    stone_count = len(os.listdir(os.path.join(dataset_path, "stone")))
    
    print(f"📊 Dataset Info:")
    print(f"   Normal images: {normal_count}")
    print(f"   Stone images: {stone_count}")
    print(f"   Total: {normal_count + stone_count}")
    
    if normal_count + stone_count < 100:
        print("⚠️  Small dataset detected. Consider adding more images for better results.")
    
    # Data generators with strong augmentation
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=30,
        width_shift_range=0.3,
        height_shift_range=0.3,
        shear_range=0.2,
        zoom_range=0.3,
        horizontal_flip=True,
        brightness_range=[0.7, 1.3],
        fill_mode='nearest',
        validation_split=0.2
    )
    
    val_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2
    )
    
    # Load data
    train_generator = train_datagen.flow_from_directory(
        dataset_path,
        target_size=(224, 224),
        batch_size=16,
        class_mode='binary',
        subset='training',
        classes=['Normal', 'stone'],
        shuffle=True
    )
    
    val_generator = val_datagen.flow_from_directory(
        dataset_path,
        target_size=(224, 224),
        batch_size=16,
        class_mode='binary',
        subset='validation',
        classes=['Normal', 'stone'],
        shuffle=False
    )
    
    # Create model
    model = create_model()
    print("🧠 Model created with EfficientNetB0 backbone")
    
    # Callbacks
    callbacks = [
        EarlyStopping(
            monitor='val_accuracy',
            patience=10,
            restore_best_weights=True,
            verbose=1
        ),
        ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=5,
            min_lr=1e-7,
            verbose=1
        ),
        ModelCheckpoint(
            'kidney_stone_model.h5',
            monitor='val_accuracy',
            save_best_only=True,
            verbose=1
        )
    ]
    
    print("🚀 Starting training...")
    
    # Phase 1: Train with frozen backbone
    history1 = model.fit(
        train_generator,
        epochs=20,
        validation_data=val_generator,
        callbacks=callbacks,
        verbose=1
    )
    
    print("🔓 Unfreezing backbone for fine-tuning...")
    
    # Phase 2: Fine-tune with unfrozen backbone
    model.layers[0].trainable = True
    model.compile(
        optimizer=Adam(learning_rate=0.0001),  # Lower learning rate
        loss='binary_crossentropy',
        metrics=['accuracy', 'precision', 'recall']
    )
    
    history2 = model.fit(
        train_generator,
        epochs=15,
        validation_data=val_generator,
        callbacks=callbacks,
        verbose=1
    )
    
    # Evaluate model
    print("📊 Evaluating model...")
    val_loss, val_acc, val_prec, val_rec = model.evaluate(val_generator, verbose=0)
    f1_score = 2 * (val_prec * val_rec) / (val_prec + val_rec) if (val_prec + val_rec) > 0 else 0
    
    print(f"✅ Training Complete!")
    print(f"   Validation Accuracy: {val_acc:.3f}")
    print(f"   Validation Precision: {val_prec:.3f}")
    print(f"   Validation Recall: {val_rec:.3f}")
    print(f"   F1 Score: {f1_score:.3f}")
    
    print(f"💾 Model saved as: kidney_stone_model.h5")
    print(f"🚀 Start backend: python3 simple_backend.py")

if __name__ == "__main__":
    train_model()