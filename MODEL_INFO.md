# Marble Defect Detection Model

## Model Information

**Model ID**: 701058d2-1084-4d21-8120-8e1ce47198c6  
**Model Version**: fast-n-easy trained model [04072026-13:13]  
**Model Type**: OpenVINO IR Format  
**Created**: April 7, 2026  

### Model Files
- `saved_model.xml` - Model architecture definition
- `saved_model.bin` - Model weights
- `saved_model.onnx` - ONNX format (portable)

### Model Specifications
- **Input Type**: float32
- **Output Type**: float32
- **Framework**: OpenVINO
- **Task**: Object Detection for Quality Control

## Classes

The model detects 4 classes:

| Class ID | Class Name | Defect ID | Description |
|----------|------------|-----------|-------------|
| 0 | ok | - | No defects detected (good marble) |
| 1 | Surface_Normal | 432883 | Normal surface variations |
| 2 | Natural_Veining | 432884 | Natural veining patterns in marble |
| 3 | Fracture_Defect | 432916 | Fracture or crack defects |

## Dataset Structure

Your current dataset is organized as:

```
Dataset/
└── Snapshot-04-07-202614_08-1775567362584/
    ├── train/
    │   ├── Images/          # Training images (.jpg)
    │   ├── Annotations/     # Training labels (.xml - Pascal VOC format)
    │   └── Segmentations/   # (empty)
    ├── dev/
    │   ├── Images/          # Validation images (.jpg)
    │   ├── Annotations/     # Validation labels (.xml)
    │   └── Segmentations/   # (empty)
    └── NoSplit/
        ├── Images/          # Unsplit images (102 files)
        ├── Annotations/     # Unsplit annotations
        └── Segmentations/   # (empty)
```

## How to Increase Dataset and Retrain

### Step 1: Add More Data

1. **Collect new images** of marble samples with various defects
2. **Annotate images** using tools like:
   - LabelImg (for Pascal VOC XML format)
   - CVAT
   - Roboflow
   - VGG Image Annotator (VIA)

3. **Save annotations** in Pascal VOC XML format matching your existing structure:
   ```xml
   <annotation>
     <filename>image_name.jpg</filename>
     <object>
       <name>Fracture_Defect</name>
       <bndbox>
         <xmin>100</xmin>
         <ymin>150</ymin>
         <xmax>300</xmax>
         <ymax>400</ymax>
       </bndbox>
     </object>
   </annotation>
   ```

4. **Place files** in the appropriate folders:
   - Add to `train/Images/` and `train/Annotations/` (80% of data)
   - Add to `dev/Images/` and `dev/Annotations/` (20% of data)

### Step 2: Prepare Training Environment

#### Option A: Using Original Platform (Recommended)
If you have access to the original training platform:
1. Upload your expanded dataset
2. Select "fast-n-easy" training preset
3. Configure classes (keep the same 4 classes)
4. Start training
5. Export as OpenVINO format

#### Option B: Train with YOLOv8 + Convert to OpenVINO

**Install dependencies:**
```bash
pip install ultralytics openvino-dev
```

**Create data.yaml:**
```yaml
path: ./Dataset/Snapshot-04-07-202614_08-1775567362584
train: train/Images
val: dev/Images

nc: 4
names:
  0: ok
  1: Surface_Normal
  2: Natural_Veining
  3: Fracture_Defect
```

**Convert Pascal VOC to YOLO format:**
```python
# You'll need to convert XML annotations to YOLO txt format
# Each line: class_id center_x center_y width height (normalized 0-1)
```

**Train the model:**
```bash
yolo detect train data=data.yaml model=yolov8n.pt epochs=100 imgsz=640
```

**Convert to OpenVINO:**
```bash
yolo export model=runs/detect/train/weights/best.pt format=openvino
```

#### Option C: Train with PyTorch Detection Framework

**Install Detectron2 or MMDetection:**
```bash
pip install torch torchvision
pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu118/torch2.0/index.html
```

**Configure training:**
- Use Faster R-CNN or RetinaNet
- Set 4 classes
- Point to your Pascal VOC dataset
- Train for 50-100 epochs

**Convert to OpenVINO:**
```bash
# Export to ONNX first
python export_to_onnx.py

# Convert ONNX to OpenVINO
mo --input_model model.onnx --output_dir openvino_model
```

### Step 3: Training Best Practices

1. **Balance your dataset**: Ensure each class has sufficient examples
2. **Data augmentation**: Use rotation, flip, brightness adjustments
3. **Validation**: Monitor validation metrics to avoid overfitting
4. **Hyperparameters**:
   - Learning rate: 0.001 - 0.01
   - Batch size: 8-16 (depending on GPU memory)
   - Epochs: 50-150
   - Image size: 640x640 or maintain original aspect ratio

### Step 4: Evaluate Model Performance

After training, test on validation set:
- Check mAP (mean Average Precision)
- Review confusion matrix
- Test on real production samples
- Compare with previous model version

### Step 5: Deploy Updated Model

1. Replace old model files with new ones
2. Keep the same class mapping (dm.json)
3. Update meta.json with new version info
4. Test inference pipeline
5. Monitor performance in production

## Notes

- Keep the same 4 classes to maintain compatibility
- Maintain Pascal VOC XML annotation format
- Recommended: At least 100+ images per class for good performance
- Consider adding more "Fracture_Defect" examples if that's critical
- Back up your original model before replacing
