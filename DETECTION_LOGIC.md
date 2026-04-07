# Detection Logic - Two Class System

## Overview

The system now uses a simplified two-class detection approach:
1. **Normal Surface** - No defects detected
2. **Fracture Defect** - Fractures detected with bounding boxes

## How It Works

### Detection Process

1. **Model Inference**: The model still detects all 4 original classes internally:
   - OK
   - Surface_Normal
   - Natural_Veining
   - Fracture_Defect

2. **Post-Processing Filter**: 
   - Only `Fracture_Defect` detections are kept
   - All other detections are filtered out
   - If NO fractures found → classify as `Normal_Surface`

3. **Visualization**:
   - Fractures: Red bounding boxes with confidence scores
   - Normal Surface: No bounding boxes, just classification label

### Code Changes

#### app.py - detect() method
```python
# Only add fracture defects to detections list
if class_name == "Fracture_Defect":
    has_fracture = True
    detections.append({...})

# If no fractures detected, return Normal Surface classification
if not has_fracture:
    detections.append({
        "class_id": -1,
        "class_name": "Normal_Surface",
        "confidence": 1.0,
        "bbox": None  # No bounding box
    })
```

#### app.py - draw_detections() method
```python
# Skip if no bbox (Normal Surface classification)
if det["bbox"] is None:
    continue

# Only draw fracture defects
if class_name == "Fracture_Defect":
    # Draw red bounding box
```

## API Response Format

### With Fractures Detected
```json
{
  "detections": [
    {
      "class_id": 3,
      "class_name": "Fracture_Defect",
      "confidence": 0.95,
      "bbox": [100, 150, 300, 400]
    },
    {
      "class_id": 3,
      "class_name": "Fracture_Defect",
      "confidence": 0.87,
      "bbox": [500, 200, 650, 380]
    }
  ],
  "image": "data:image/jpeg;base64,...",
  "total_defects": 2
}
```

### No Fractures Detected (Normal Surface)
```json
{
  "detections": [
    {
      "class_id": -1,
      "class_name": "Normal_Surface",
      "confidence": 1.0,
      "bbox": null
    }
  ],
  "image": "data:image/jpeg;base64,...",
  "total_defects": 0
}
```

## UI Updates

### Legend
- Removed: OK, Surface Normal, Natural Veining
- Kept: Normal Surface (green), Fracture Defect (red)

### Detection List
- Shows "Normal Surface" when no fractures
- Shows "Fracture Defect" entries with confidence for each fracture
- Green background for Normal Surface
- Red background for Fracture Defect

### Statistics
- Total Detections: Count of all detection entries
- Defects: Count of fractures only

## Benefits

1. **Simplified UX**: Users only care about fractures vs normal
2. **Clear Visualization**: Only problematic areas are highlighted
3. **Reduced Noise**: No boxes for non-critical detections
4. **Binary Decision**: Easy pass/fail quality control

## Model Unchanged

⚠️ **Important**: The underlying model is NOT retrained or modified. It still detects all 4 classes internally. We only filter the output in post-processing.

## Future Enhancements

Potential improvements:
- Add confidence threshold adjustment
- Show count of filtered detections (optional)
- Add severity levels for fractures
- Export detection reports
- Batch processing mode
