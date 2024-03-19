def transform_bbox(annotation, image_shape, transform_func):
    # Transform bounding box coordinates based on image transformation
    transformed_bbox = transform_func(annotation, image_shape)
    
    label,x1, y1, x2, y2 = transformed_bbox
    width = x2 - x1
    width_norm=width/image_shape[0]
    height = y2 - y1
    height_norm=height/image_shape[1]
    x_center = x1 + width / 2
    x_center_norm = x_center/image_shape[0]
    y_center = y1 + height / 2
    y_center_norm = y_center/image_shape[1]
    
    transformed_annotation = f"{label} {x_center_norm} {y_center_norm} {width_norm} {height_norm}"
    
    return transformed_annotation
