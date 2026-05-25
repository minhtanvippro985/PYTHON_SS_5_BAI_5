
raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-099 "

while True:

    print("\n===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====")
    print("1. Hiển thị chuỗi mã vạch gốc")
    print("2. Giải mã, làm sạch và in báo cáo kiểm kê")
    print("3. Tra cứu nhanh theo đuôi Serial")
    print("4. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    
    match choice:
        
        case "1":
            print("\n--- CHUỖI MÃ VẠCH GỐC ---")
            print(raw_batch)
            print("-------------------------")
            
        case "2":
            products = raw_batch.split(";")
            
            print("\n===== BÁO CÁO KIỂM KÊ =====")
            print("MÃ SP | XUẤT XỨ | NĂM SX | SERIAL | TRẠNG THÁI")
            print("--------------------------------------------------")
            
            total_products = len(products)
            success_count = 0
            
            for prod in products:
                prod_clean = prod.strip().upper()
                
                # nếu chuỗi rỗng thì bỏ qua
                if not prod_clean:
                    total_products -= 1
                    continue
                    
                # tách mã sản phẩm thành 4 phần bằng dấu '-'
                prod_info_parts = prod_clean.split("-")
                
                if len(prod_info_parts) != 4:
                    print(f"{prod_clean} | N/A | N/A | N/A | Lỗi định dạng - Reject")
                    continue
                    
                prod_type, country, year, serial = prod_info_parts
                
                
                full_year = f"20{year}"
                
                # validate serial
                if serial.isdigit():
                    status = "Pass"
                    success_count += 1
                else:
                    status = "Lỗi Serial - Reject"
                    
              
                print(f"{prod_clean} | {country} | {full_year} | {serial} | {status}")
                
            print("--------------------------------------------------")
            print(f"Tổng kết: Đã giải mã thành công {success_count} sản phẩm hợp lệ / Tổng số {total_products} sản phẩm.")
            print("==========================================")
            
        
        case "3":
          
            search_tail = input("Nhập 2 số cuối của Serial cần tìm: ").strip()
            # nhập 2 số cuối của serial 
            if len(search_tail) != 2 or not search_tail.isdigit():
                print("Vui lòng nhập chính xác 2 ký tự số!")
                continue
                
            products = raw_batch.split(";")
            found = False
            
            print(f"\n--- KẾT QUẢ TÌM KIẾM ĐUÔI '{search_tail}' ---")
            for prod in products:
                prod_clean = prod.strip().upper()
                prod_info_parts = prod_clean.split("-")
                
                if len(prod_info_parts) == 4:
                    serial = prod_info_parts[3]
                    # lấy 2 ký tự cuối của serial bằng [-2:]
                    if serial[-2:] == search_tail:
                        print(f"Tìm thấy: {prod_clean} (Loại: {prod_info_parts[0]}, Xuất xứ: {prod_info_parts[1]}, Năm: 20{prod_info_parts[2]}, Serial: {serial})")
                        found = True
                        
            if not found:
                print("Không tìm thấy sản phẩm phù hợp.")
            print("-------------------------------------")


        case "4":
            print("\nĐóng ca kiểm kho. ")
            break

        case _:
            print("Vui lòng nhập số từ 1-4!")