def calculate_price(V: int, S: int) -> int:
    """
    Tính giá trị đơn hàng sau chiết khấu và phí vận chuyển.
    V: tổng giá trị đơn hàng (1_000_000 <= V <= 10_000_000)
    S: trạng thái khách hàng (1: New, 2: Regular, 3: VIP)
    """

    # Validate input
    if not (1_000_000 <= V <= 10_000_000) or S not in [1, 2, 3]:
        return None  # không hợp lệ

    discount = 0

    if S in [1, 2]:  # New hoặc Regular
        if V < 5_000_000:
            discount = 0.05
        else:
            discount = 0.10
    elif S == 3:  # VIP
        if V < 5_000_000:
            discount = 0.10
        else:
            discount = 0.15

    # Tính giá sau chiết khấu
    final_price = V - round(V * discount)

    # Thêm phí vận chuyển
    if (V < 5_000_000) and (S in [1, 2]):
        final_price += 50_000  # phí vận chuyển

    return final_price
