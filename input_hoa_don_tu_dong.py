from sqlalchemy import create_engine, text
import pymysql
import datetime

# MySQL Database Connection Details
host = "localhost"
port = 3306
database = "REALMof"
username = "trongthuc"
password = "Trongthuc1708"

# Create Engine for SQLAlchemy
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# Function to insert user input into MySQL
def auto_input_insert_mysql_db():
    # Auto-generate values
    today = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    nguoi_tao_don = "Thức"

    # User Input with Choices
    size_options = {1: "S", 2: "M", 3: "L", 4: "FreeSize"}
    platform_options = {1: "Facebook", 2: "Instagram", 3: "Shopee"}

    # Get input from user
    ma_don_hang = input("Enter MA_DON_HANG: ")
    platform = int(input("Choose PLATFORM (1: Facebook / 2: Instagram / 3: Shopee): "))
    ten_khach_hang = input("Enter TEN_KHACH_HANG: ")
    sdt = input("Enter SDT (Phone Number): ")
    ngay_sinh_nhat = input("Enter NGAY_SINH_NHAT (YYYY-MM-DD) or leave empty: ") or None
    dia_chi = input("Enter DIA_CHI: ")
    thanh_pho = input("Enter THANH_PHO: ")
    sku = input("Enter SKU: ")
    ten_san_pham = input("Enter TEN_SAN_PHAM: ")
    size = int(input("Choose SIZE (1: S / 2: M / 3: L / 4: FreeSize): "))
    so_luong = int(input("Enter SO_LUONG: "))
    gia_tri_don = float(input("Enter GIA_TRI_DON: "))
    hinh_thuc_thanh_toan = input("Enter HINH_THUC_THANH_TOAN: ")
    tinh_trang_thanh_toan = input("Enter TINH_TRANG_THANH_TOAN: ")
    ghi_chu = input("Enter GHI_CHU (Optional): ") or None

    # Map user choices to actual values
    platform_value = platform_options.get(platform, "Unknown")
    size_value = size_options.get(size, "Unknown")

    # Create SQL INSERT query
    insert_query = """
    INSERT INTO REALM_of_sale_feb (
        NGAY_TAO, MA_DON_HANG, PLATFORM, TEN_KHACH_HANG, SDT, 
        NGAY_SINH_NHAT, DIA_CHI, THANH_PHO, NGUOI_TAO_DON, 
        SKU, TEN_SAN_PHAM, SIZE, SO_LUONG, GIA_TRI_DON, 
        HINH_THUC_THANH_TOAN, TINH_TRANG_THANH_TOAN, GHI_CHU
    ) VALUES (
        :ngay_tao, :ma_don_hang, :platform, :ten_khach_hang, :sdt, 
        :ngay_sinh_nhat, :dia_chi, :thanh_pho, :nguoi_tao_don, 
        :sku, :ten_san_pham, :size, :so_luong, :gia_tri_don, 
        :hinh_thuc_thanh_toan, :tinh_trang_thanh_toan, :ghi_chu
    )
    """

    # Prepare Data Dictionary
    data = {
        "ngay_tao": today,
        "ma_don_hang": ma_don_hang,
        "platform": platform_value,
        "ten_khach_hang": ten_khach_hang,
        "sdt": sdt,
        "ngay_sinh_nhat": ngay_sinh_nhat,
        "dia_chi": dia_chi,
        "thanh_pho": thanh_pho,
        "nguoi_tao_don": nguoi_tao_don,
        "sku": sku,
        "ten_san_pham": ten_san_pham,
        "size": size_value,
        "so_luong": so_luong,
        "gia_tri_don": gia_tri_don,
        "hinh_thuc_thanh_toan": hinh_thuc_thanh_toan,
        "tinh_trang_thanh_toan": tinh_trang_thanh_toan,
        "ghi_chu": ghi_chu,
    }

    # Insert Data into MySQL
    try:
        with engine.connect() as connection:
            connection.execute(text(insert_query), data)
            connection.commit()
            print("\n✅ Data inserted successfully into MySQL!")
    except Exception as e:
        print(f"❌ Error inserting data: {e}")

# Run the function
auto_input_insert_mysql_db()

