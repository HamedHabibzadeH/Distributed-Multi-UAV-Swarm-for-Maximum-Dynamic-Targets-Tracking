import os

# لیست پوشه‌هایی که باید ساخته شوند
directories = [
    "configs",
    "src/marl_uav/env",
    "src/marl_uav/sensors",
    "scripts"
]

# لیست فایل‌ها (به همراه محتوای اولیه خالی یا اختیاری)
files = {
    "configs/default.yaml": "",
    "src/marl_uav/__init__.py": "",
    "src/marl_uav/env/__init__.py": "",
    "src/marl_uav/env/entities.py": "",
    "src/marl_uav/env/world.py": "",
    "src/marl_uav/sensors/__init__.py": "",
    "src/marl_uav/sensors/sim_camera.py": "",
    "scripts/run_sim_debug.py": ""
}

# ساخت پوشه‌ها
for dir_path in directories:
    os.makedirs(dir_path, exist_ok=True)
    print(f"پوشه ایجاد شد: {dir_path}")

# ساخت فایل‌ها
for file_path, content in files.items():
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"فایل ایجاد شد: {file_path}")

print("\n ساختار پروژه با موفقیت ایجاد شد!")
