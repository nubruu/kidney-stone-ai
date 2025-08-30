import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB0, ResNet50
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

class KidneyStoneDetector:
    def __init__(self, data_path, img_size=(224, 224), batch_size=32):
        self.data_path = data_path
        self.img_size = img_size
        self.batch_size = batch_size
        self.models = {}
        
    def create_data_generators(self):
        # Data augmentation for training
        train_datagen = ImageDataGenerator(
            rescale=1./255,
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            brightness_range=[0.8, 1.2],
            validation_split=0.3  # 70% train, 30% for val+test
        )
        
        val_test_datagen = ImageDataGenerator(
            rescale=1./255,
            validation_split=0.5  # Split the 30% into 15% val, 15% test
        )
        
        # Training data (70%)
        self.train_generator = train_datagen.flow_from_directory(
            self.data_path,
            target_size=self.img_size,
            batch_size=self.batch_size,
            class_mode='binary',
            subset='training',
            classes=['Normal', 'stone']
        )
        
        # Validation data (15%)
        self.val_generator = val_test_datagen.flow_from_directory(
            self.data_path,
            target_size=self.img_size,
            batch_size=self.batch_size,
            class_mode='binary',
            subset='training',
            classes=['Normal', 'stone']
        )
        
        # Test data (15%)
        self.test_generator = val_test_datagen.flow_from_directory(
            self.data_path,
            target_size=self.img_size,
            batch_size=self.batch_size,
            class_mode='binary',
            subset='validation',
            classes=['Normal', 'stone'],
            shuffle=False
        )
        
    def create_model(self, base_model_name='efficientnet'):
        if base_model_name == 'efficientnet':
            base_model = EfficientNetB0(weights='imagenet', include_top=False, input_shape=(*self.img_size, 3))
        else:
            base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(*self.img_size, 3))
        
        # Freeze base model layers
        base_model.trainable = False
        
        # Add custom classification head
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        x = Dense(128, activation='relu')(x)
        x = Dropout(0.5)(x)
        predictions = Dense(1, activation='sigmoid')(x)
        
        model = Model(inputs=base_model.input, outputs=predictions)
        model.compile(
            optimizer=Adam(learning_rate=0.001),
            loss='binary_crossentropy',
            metrics=['accuracy']
        )
        
        return model
    
    def train_model(self, model_name='efficientnet', epochs=20):
        model = self.create_model(model_name)
        
        # Callbacks
        callbacks = [
            tf.keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True),
            tf.keras.callbacks.ReduceLROnPlateau(factor=0.5, patience=3)
        ]
        
        # Train model
        history = model.fit(
            self.train_generator,
            epochs=epochs,
            validation_data=self.val_generator,
            callbacks=callbacks
        )
        
        # Fine-tuning
        model.layers[0].trainable = True
        model.compile(
            optimizer=Adam(learning_rate=0.0001),
            loss='binary_crossentropy',
            metrics=['accuracy']
        )
        
        history_fine = model.fit(
            self.train_generator,
            epochs=10,
            validation_data=self.val_generator,
            callbacks=callbacks
        )
        
        self.models[model_name] = model
        return model, history
    
    def evaluate_model(self, model, model_name):
        # Predictions
        predictions = model.predict(self.test_generator)
        y_pred = (predictions > 0.5).astype(int)
        y_true = self.test_generator.classes
        
        # Metrics
        print(f"\n{model_name.upper()} Results:")
        print(classification_report(y_true, y_pred, target_names=['Normal', 'Stone']))
        
        # ROC-AUC
        auc = roc_auc_score(y_true, predictions)
        print(f"ROC-AUC: {auc:.4f}")
        
        # Confusion Matrix
        cm = confusion_matrix(y_true, y_pred)
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                   xticklabels=['Normal', 'Stone'], yticklabels=['Normal', 'Stone'])
        plt.title(f'{model_name} - Confusion Matrix')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.savefig(f'{model_name}_confusion_matrix.png')
        plt.show()
        
        return auc
    
    def save_best_model(self):
        best_model_name = max(self.models.keys(), 
                            key=lambda x: self.evaluate_model(self.models[x], x))
        best_model = self.models[best_model_name]
        best_model.save(f'best_kidney_stone_model_{best_model_name}.h5')
        print(f"Best model ({best_model_name}) saved!")
        return best_model_name

def main():
    # Initialize detector
    detector = KidneyStoneDetector('Kidney Ultrasound Images Stone and No Stone')
    
    # Create data generators
    detector.create_data_generators()
    
    # Train both models
    print("Training EfficientNetB0...")
    detector.train_model('efficientnet', epochs=20)
    
    print("Training ResNet50...")
    detector.train_model('resnet50', epochs=20)
    
    # Evaluate and save best model
    detector.save_best_model()

if __name__ == "__main__":
    main()