import os

# 獲取當前資料夾路徑
current_folder_path = os.getcwd()

# 使用 os.listdir() 函式取得當前資料夾內所有的項目（包括檔案和資料夾）
all_items = os.listdir(current_folder_path)

# 過濾出只是資料夾的項目
folders = [item for item in all_items if os.path.isdir(
    os.path.join(current_folder_path, item))]

# 列印出所有資料夾的名稱
print("當前資料夾內的資料夾：")
for folder in folders:
    if folder.startswith(".") or folder.startswith("0"):
        continue
    else:
        os.rename(folder, "0" + folder)
        

