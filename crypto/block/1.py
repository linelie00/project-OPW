import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from Crypto.Cipher import AES
from Crypto.Util import Counter
from PIL import Image, ImageTk
import numpy as np
import os

# 데이터 패딩 함수
def pad(data):
    while len(data) % 16 != 0:
        data += b' '
    return data

# AES ECB 이미지 암호화
def encrypt_image_ecb(image_path, key):
    img = Image.open(image_path).convert('RGB')
    img_data = np.array(img)
    cipher = AES.new(key, AES.MODE_ECB)
    data = img_data.tobytes()
    padded_data = pad(data)
    encrypted = cipher.encrypt(padded_data)
    encrypted_img = np.frombuffer(encrypted[:len(data)], dtype=np.uint8).reshape(img_data.shape)
    return img, Image.fromarray(encrypted_img)

# AES CTR 파일 암호화/복호화
def encrypt_decrypt_file_ctr(file_path, key, nonce):
    with open(file_path, 'rb') as f:
        data = f.read()
    ctr = Counter.new(128, initial_value=int.from_bytes(nonce, byteorder='big'))
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    result = cipher.encrypt(data)
    return result

# ECB 이미지 암호화 실행
def run_ecb():
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.bmp")])
    if not img_path:
        return
    key_str = simpledialog.askstring("비밀키 입력", "16바이트 AES 키를 입력하세요:")
    print(f"[ECB] 입력한 키: '{key_str}' / 글자 수: {len(key_str)} / 바이트 수: {len(key_str.encode())}")
    if not key_str or len(key_str.encode()) != 16:
        messagebox.showerror("오류", "16바이트 키를 입력해야 합니다.")
        return
    key = key_str.encode()

    original_img, encrypted_img = encrypt_image_ecb(img_path, key)

    # 새 창에 이미지 출력
    img_window = tk.Toplevel()
    img_window.title("AES-ECB 이미지 암호화 결과")

    original_tk = ImageTk.PhotoImage(original_img.resize((256, 256)))
    encrypted_tk = ImageTk.PhotoImage(encrypted_img.resize((256, 256)))

    tk.Label(img_window, text="원본 이미지").grid(row=0, column=0)
    tk.Label(img_window, image=original_tk).grid(row=1, column=0)
    tk.Label(img_window, text="ECB 암호화 이미지").grid(row=0, column=1)
    tk.Label(img_window, image=encrypted_tk).grid(row=1, column=1)

    # 이미지가 유지되도록 참조 저장
    img_window.original_img = original_tk
    img_window.encrypted_img = encrypted_tk

# CTR 파일 암복호화 실행
def run_ctr():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    key_str = simpledialog.askstring("비밀키 입력", "16바이트 AES 키를 입력하세요:")
    nonce_str = simpledialog.askstring("Nonce 입력", "16바이트 Nonce 값을 입력하세요:")
    if not key_str or len(key_str.encode()) != 16 or not nonce_str or len(nonce_str.encode()) != 16:
        messagebox.showerror("오류", "키와 Nonce는 각각 16바이트여야 합니다.")
        return
    key = key_str.encode()
    nonce = nonce_str.encode()

    result = encrypt_decrypt_file_ctr(file_path, key, nonce)
    save_path = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("Binary files", "*.bin")])
    if save_path:
        with open(save_path, 'wb') as f:
            f.write(result)
        messagebox.showinfo("완료", f"결과 파일이 저장되었습니다:\n{save_path}")

# GUI 메인
root = tk.Tk()
root.title("AES 암호화 도구")

tk.Label(root, text="AES 암호화 프로그램", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="1. AES128-ECB 이미지 암호화", command=run_ecb, width=40, height=2).pack(pady=5)
tk.Button(root, text="2. AES128-CTR 파일 암/복호화", command=run_ctr, width=40, height=2).pack(pady=5)

root.mainloop()
