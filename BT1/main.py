from fastapi import FastAPI

# PHÂN TÍCH LỖI:
# Endpoint được khai báo là "/products/product_id".
# FastAPI hiểu "product_id" là một chuỗi cố định, không phải Path Parameter.
# Vì vậy API chỉ nhận được URL:
#     GET /products/product_id
# Khi frontend gọi:
#     GET /products/1
# hoặc
#     GET /products/2
# sẽ không có endpoint nào khớp nên FastAPI trả về 404 Not Found.
#
# Cách sửa:
# Cần đặt tên biến trong dấu {}:
#     @app.get("/products/{product_id}")
# để FastAPI lấy giá trị product_id trực tiếp từ URL.

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop Dell", "price": 15000000},
    {"id": 2, "name": "Chuột Logitech", "price": 350000},
    {"id": 3, "name": "Bàn phím cơ", "price": 1200000}
]

@app.get("/products/{product_id}")
def get_product_detail(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    return {
        "message": f"Không tìm thấy sản phẩm có id = {product_id}"
    }