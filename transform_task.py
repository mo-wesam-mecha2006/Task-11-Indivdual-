import math

def transform_obstacles():
    # 1. إدخال مصفوفة النقاط ثلاثية الأبعاد المكتشفة في إطار الكاميرا
    points = [[2.0, 0.0, -0.2], [3.5, 1.0, -0.3], [1.5, -0.8, -0.1]]
    
    # 2. إزاحات الترجمة (tx, ty, tz) بالمتر
    tx, ty, tz = 0.5, 0.0, 0.2
    
    # 3. زاوية الميل (Pitch) حول محور Y وتحويلها إلى راديان
    theta_deg = -15.0
    theta_rad = math.radians(theta_deg)
    
    cos_t = math.cos(theta_rad)
    sin_t = math.sin(theta_rad)
    
    print("--- Transformed Obstacles (Base Frame) ---")
    
    # 4. استخدام حلقة تكرارية لحساب الإحداثيات الجديدة لكل نقطة
    for i, pt in enumerate(points, start=1):
        x_cam, y_cam, z_cam = pt
        
        # تطبيق معادلات الدوران والترجمة
        x_base = cos_t * x_cam + sin_t * z_cam + tx
        y_base = y_cam + ty
        z_base = -sin_t * x_cam + cos_t * z_cam + tz
        
        # طباعة النتائج مقربة إلى منزلين عشريين
        print(f"Obstacle {i}: [{x_base:.2f}, {y_base:.2f}, {z_base:.2f}]")

if __name__ == "__main__":
    transform_obstacles()